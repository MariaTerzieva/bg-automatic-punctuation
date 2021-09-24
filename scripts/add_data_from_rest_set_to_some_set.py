import sys
import re
import random

input_file_name = sys.argv[1]
set_file_name = sys.argv[2]
rest_file_name = re.sub('\.txt', '_rest.txt', input_file_name)

with open(input_file_name,"r") as input_file, open(set_file_name,"a") as set_file, open(rest_file_name,"r") as rest_file:
    input_file_contents = input_file.read().splitlines()
    len_input_file_contents = len(input_file_contents)

    rest_file_contents = input_file.read().splitlines()
    len_rest_file_contents = len(rest_file_contents)

    number_to_add = int(int(sys.argv[3]) / 100 * len_input_file_contents)

    if len_rest_file_contents > number_to_add:
        additional_data = random.sample(rest_file_contents, number_to_add)
        rest_set = [item for item in rest_file_contents if item not in additional_data]
    else:
        additional_data = rest_file_contents
        rest_set = []

    for sentence in additional_data:
        print(sentence, file=set_file)

with open(rest_file_name,"w") as rest_file:
    for sentence in rest_set:
        print(sentence, file=rest_file)
