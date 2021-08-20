import fileinput
import os
import re


dir_name = os.path.dirname(__file__)
full_file_name = os.path.join(dir_name, "../{0}/Atanas Dalchev Fragments.txt")

file = open(full_file_name.format("raw"), "r")
text = file.read()

text_with_reduced_new_lines = re.sub('(\\n)+', '\\n', text)

with open(full_file_name.format("processed"), "w") as fout:
    print(text_with_reduced_new_lines, file=fout)

# Manual clean up:
# Add missing punctuation.
# Delete non-sentences.
