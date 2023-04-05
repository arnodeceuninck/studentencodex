# Someone created a list of all lyrics in the old red codex in .txt format
# Convert it to jekyll format by adding the front matter
# and renaming the files to .md

import os
import re

# Get all the files in the directory
files = os.listdir('files')

# Loop through the files
for file in files:
    filename = file.split('.')[0]
    # Open the file
    with open('files/' + file, 'r', encoding='utf-8') as f:
        # Read the file
        data = f.read()

        # each file starts with ---, followed by some lines with data, followed by ---, followed by the lyrics
        # in the lyrics, add two spaces to the end of each line (if the line is not empty and if there are no two spaces at the end)

        lines = data.splitlines()

        output = []

        # find the line with ---
        split_ctr = 0
        for i in range(len(lines)):
            # if the line starts with ---
            if lines[i].startswith('---'):
                split_ctr += 1

            if split_ctr >= 2:
                # if line doesn't end with two spaces and is not empty, add two spaces
                if not lines[i].endswith('  ') and lines[i] != '':
                    lines[i] += '  '

            output.append(lines[i])

        # write lines to file in _antwerpse/output
        with open('output/' + filename + '.md', 'w') as f:
            f.write('\n'.join(output))


