# Someone created a list of all lyrics in the old red codex in .txt format
# Convert it to jekyll format by adding the front matter
# and renaming the files to .md

import os
import re

# Get all the files in the directory
files = os.listdir('rodex')

# Loop through the files
for file in files:
    filename = file.split('.')[0]
    # Open the file
    with open('rodex/' + file, 'r') as f:
        # Read the file
        data = f.read()
        # add two spaces to the end of each line (if the line is not empty)
        data = re.sub(r'^(?!\s*$).+', r'\g<0>  ', data, flags=re.MULTILINE)

        # add the front matter
        data = f'---\nlayout: song\ntitle: {filename}\npage: 404\n---\n\n' + data

        # Write the file
        with open('output/' + filename + '.md', 'w') as f:
            f.write(data)
            print(f'Converted {file}')

