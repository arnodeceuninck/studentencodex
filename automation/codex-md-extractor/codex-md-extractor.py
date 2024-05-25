import os
import re


input_md = "automation\codex-md-extractor\codex-converted.md" # docx converted to pdf, converted to docx, converted to md
output_directory = "automation\codex-md-extractor\output"

# Remove output directory if it exists
if os.path.exists(output_directory):
    import shutil
    shutil.rmtree(output_directory)
# Create output directory
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Each title got following md syntax: **Title** (eventually with some spaces or '>' characters)
title_pattern = re.compile(r"(\*\*.*\*\*)")

def title_to_filename(title):
    # title.replace("Ã©", "e") # special character (e.g. Ohé kameraad)

    title = title.lower()

    replacements = {"à": "a", "é": "e", "è": "e", "ê": "e", "ë": "e", "î": "i", "ï": "i", "ô": "o", "ö": "o", "ù": "u", "û": "u", "ü": "u", "ç": "c", "œ": "oe", "æ": "ae",
                    # Some special cases
                    "ã©": "e", # Ohé kameraad
                    "ã‡": "c", # Ca ca geschmauset 
                    "ã§": "c",
                    "ã¨": "e", # La mere gaspar
                    "ã¡" : "a", # Te Duinkerk gaat het al verkeerd
                    "ãª" : "e", # Mamma, 'k wil 'n man he
                    "ã¶" : "o", # 's gibt kein schöner leben als studentenleben
                    "ã¤": "a", # hofbräuhaus-lied
                    "ã¼": "u", # trink, trink, bruderlein trink
                    "ã„": "a", # ännchen von tharau
                    "ã\xa0": "a", # chanson a boire,
                    "ã€": "a", # a la claire fontaine
                    "ã‰" : "e", # '**les champs-elysees**'
                    "ã¥": "a", # '**studentsangen**'
                    "ã¢" : "a", # '**antwarpe**'
                    } 
    for accented, non_accented in replacements.items():
        title = title.replace(accented, non_accented)
        
    if "ã" in title:
        raise Exception("ã in title: " + title)

    # take only alphanumeric characters and make them lowercase
    alpha_only = "".join([c if c.isalnum() else "" for c in title]).lower()
    
    return alpha_only

def fix_special_case(content):
    # Some titles split in two parts, so we need to merge them
    # > **What shall we do**
    # >
    # > **with the drunken sailor?**
    special_case_pattern = re.compile(r"> \*\*(.*)\*\*\n>\n> \*\*(.*)\*\*", re.MULTILINE)
    # Replace it with "> **combined**\n"
    content = special_case_pattern.sub(r"> **\1 \2**\n", content) 
    return content


# Create a file per title with the title and its content (everything up to the next title)
with open(input_md, "r") as f:
    content = f.read()
    content = fix_special_case(content)
    songs = re.split(title_pattern, content)[1:]
    # songs contains alternately the title and the content, so we can iterate by 2
    for i in range(0, len(songs), 2):
        title = songs[i]
        song_content = songs[i + 1]
        filename = os.path.join(output_directory, title_to_filename(title) + ".md")
        with open(filename, "w") as f:
            f.write(title + song_content)

# Remove files that do not match any song
# Two cases:
#  - a.md (or any single character): This is of the index pages, not needed
#  - Files that do not contain more than 1 line with letters (e.g. "LIEDERBOEK" has no content, since it is the first page)
files_to_remove = ["alfabetischeindex.md"]
for filename in os.listdir(output_directory):
    single_char_pattern = re.compile(r"^[a-zA-Z]\.md$")
    if single_char_pattern.match(filename):
        files_to_remove.append(filename)
    else:
        with open(os.path.join(output_directory, filename), "r") as f:
            content = f.read()
            lines = content.split("\n")
            # Only keep lines with letters
            lines_with_letters = [line for line in lines if any(c.isalpha() for c in line)]
            if len(lines_with_letters) <= 1:
                files_to_remove.append(filename)

print("Files to remove: ", files_to_remove)
for filename in files_to_remove:
    os.remove(os.path.join(output_directory, filename))


# Now fix the content itself

"""
Remove '>' of lines starting with '>' that do not have an asterix in them (since if it is an actual quote or extra info, there is usually an asterix)
"""
def fix_unnecesary_quotes(content):
    quote_pattern = re.compile(r"^> ([^*].*)$", re.MULTILINE)
    content = quote_pattern.sub(r"\1", content)
    return content

def get_and_remove_title(content):
    title = title_pattern.match(content).group(1)
    content = title_pattern.sub("", content, count=1)
    return title, content

def get_and_remove_page(content, title):
    page_pattern = re.compile(r"^>*\s*~*(\d+\.?)", re.MULTILINE)
    page = page_pattern.match(content)
    # convert to list of strings
    pages = page_pattern.findall(content)
    # filter out all numbers ending with a dot (since it are verse numbers)
    pages = [p for p in pages if not p.endswith(".")]
    # join with comma
    page = "-".join(pages)
    # if no page found, throw exception
    if not page:
        page = get_page_from_index(title)

    for page in pages:
        content = content.replace(page, "")

    # print("Page: ", page)
    return page, content

def get_page_from_index(title):
    title = title.replace("**", "")
    with open(input_md, "r") as f:
        content = f.read()
    
    # escape special characters
    title = re.escape(title)
    pattern = re.compile(rf">? ?{title} (\d+)$", re.MULTILINE)

    page = pattern.search(content)
    if not page:
        print(f"No index match found for {title}")
        return ""
    return page.group(1)

def remove_empty_quotes(content):
    quote_pattern = re.compile(r"^> ?$", re.MULTILINE)
    content = quote_pattern.sub("", content)
    return content

# def fix_lost_bis(content):
#     """
#     If "\]" or "\] (bis)" is the only content of a line, it should be placed on the previous line

# > O land van Artevelde,

# \]

# > De Geuzen houden wacht!

# \] (bis)
#     """
#     bis_pattern = re.compile(r"^(> .*)\n+(\\\] (\\\] (bis)))", re.MULTILINE)
#     content = bis_pattern.sub(r"\1 \2", content)
#     return content


def fix_verse_start(content):
    """
    A verse starts with 1. or 2. or 3. etc. followed by a space
    When keeping it like this, markdown sees this as a list and will restart the index at every verse.
    To avoid this (and keep the indent of all lines the same), we'll escape the dot, such that it becomes
    a normal alinea. (and we make the number bold)
    """
    verse_pattern = re.compile(r"^([R\d]+)\.", re.MULTILINE)
    content = verse_pattern.sub(r"**\1**\\.", content)
    return content


"""
Adds the header, e.g.: 
---
title: Aan het Noordzeestrand 
page: 471
---  
"""
def add_properties(content, title, page):
    header = "---\n"
    header += "title: " + title[2:-2] + "\n"
    header += "page: " + page + "\n"
    header += "---\n"
    return header + content



for filename in os.listdir(output_directory):
    content = ""
    with open(os.path.join(output_directory, filename), "r") as f:
        content = f.read()
    
    content = fix_unnecesary_quotes(content)
    title, content = get_and_remove_title(content)
    page, content = get_and_remove_page(content, title)
    content = remove_empty_quotes(content)
    content = fix_verse_start(content)
    content = add_properties(content, title, page)

    with open(os.path.join(output_directory, filename), "w") as f:
        f.write(content)