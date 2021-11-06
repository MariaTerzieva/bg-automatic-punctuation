# arguments are:
# sys.argv[1]: the name of the file with mismatched sentences that has been manually edited
#              the original file from which the mismatched sentences were extracted is expected to be in the same directory
# outcome:
# the script replaces the edited sentences from the mismatched sentences file into the original file

import sys
import re


edited_statistics_file_name = sys.argv[1]
original_file_name = re.sub('_mismatched_sentences\.txt', '.txt', edited_statistics_file_name)

with open(edited_statistics_file_name,"r") as edited_statistics_file, open(original_file_name,"r") as original_file:
    original_file_contents = original_file.read().splitlines()
    edited_statistics_file_contents = edited_statistics_file.read().splitlines()
    edited_sentences_dict = {int(split_line[0]): split_line[1] for split_line in [line.split(' : ', 1) for line in edited_statistics_file_contents]}

with open(original_file_name,"w") as original_file:
    for line_number, line in enumerate(original_file_contents):
        if line_number in edited_sentences_dict:
            print(edited_sentences_dict[line_number], file=original_file)
        else:
            print(line, file=original_file)
