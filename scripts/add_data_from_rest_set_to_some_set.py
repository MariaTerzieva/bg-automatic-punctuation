# arguments are:
# sys.argv[1]: the name of the original file
# sys.argv[2]: the name of the data set file to add sentences to: train, dev or test
# sys.argv[3]: the percentage of data (as an int) from the original file that we want to add; data is taken from the rest file
#              the rest file is expected to be in the same directory as the original file
# outcome:
# the data set file we specified as sys.argv[2] has the additional percentage of data (sys.argv[3]) we specified; data is taken from the rest file
# the rest file is adjusted to exclude the data added to the data set file

import sys
import re
import random


input_file_name = sys.argv[1]
set_file_name = sys.argv[2]
rest_file_name = re.sub('\.txt', '_rest.txt', input_file_name)

with open(input_file_name, "r") as input_file, open(rest_file_name, "r") as rest_file:
    input_file_contents = input_file.read().splitlines()
    len_input_file_contents = len(input_file_contents)

    rest_file_contents = rest_file.read().splitlines()
    len_rest_file_contents = len(rest_file_contents)

with open(set_file_name, "a") as set_file:
    number_to_add = int(int(sys.argv[3]) / 100 * len_input_file_contents)

    if len_rest_file_contents > number_to_add:
        additional_data = random.sample(rest_file_contents, number_to_add)
        rest_set = [item for item in rest_file_contents if item not in additional_data]
    else:
        additional_data = rest_file_contents
        rest_set = []

    for sentence in additional_data:
        print(sentence, file=set_file)

with open(rest_file_name, "w") as rest_file:
    for sentence in rest_set:
        print(sentence, file=rest_file)
