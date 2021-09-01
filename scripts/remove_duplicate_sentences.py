import sys
import re


sentences_seen = set()
input_file_name = sys.argv[1]
duplicate_sentences_file_name = re.sub('\.txt', '_duplicate_sentences.txt', input_file_name)

with open(input_file_name, "r") as input_file:
    input_file_contents = input_file.read().splitlines()

with open(duplicate_sentences_file_name, "w") as duplicate_sentences_file, open(input_file_name, "w") as input_file:
    for line in input_file_contents:
        if line not in sentences_seen:
            print(line, file=input_file)
            sentences_seen.add(line)
        else:
            print(line, file=duplicate_sentences_file)
