# arguments are:
# sys.argv[1]: the name of the original file we want to divide into train, dev, test, rest
# sys.argv[2]: the percentage of data from the original file (as an int) we want the train set to contain
# sys.argv[3]: the percentage of data from the original file (as an int) we want the dev set to contain
# sys.argv[4]: the percentage of data frokm the original file (as an int) we want the test set to contain
# outcome:
# the original file is divided into 4 new files (but the original file is also kept): train, dev, test and rest
# the rest file contains the data from the original file that hasn't been added yet neither to train, nor to dev, nor to test

import sys
import re
import random


input_file_name = sys.argv[1]
train_file_name = re.sub('\.txt', '_train.txt', input_file_name)
dev_file_name = re.sub('\.txt', '_dev.txt', input_file_name)
test_file_name = re.sub('\.txt', '_test.txt', input_file_name)
rest_file_name = re.sub('\.txt', '_rest.txt', input_file_name)

with open(input_file_name,"r") as input_file, open(train_file_name,"w") as train_file, open(dev_file_name,"w") as dev_file, open(test_file_name,"w") as test_file, open(rest_file_name,"w") as rest_file:
    input_file_contents = input_file.read().splitlines()
    len_input_file_contents = len(input_file_contents)

    number_train = int(int(sys.argv[2]) / 100 * len_input_file_contents)
    number_dev = int(int(sys.argv[3]) / 100 * len_input_file_contents)
    number_test = int(int(sys.argv[4]) / 100 * len_input_file_contents)
    number_rest = len_input_file_contents - number_train - number_dev - number_test

    train_set = random.sample(input_file_contents, number_train)
    input_file_contents_minus_train_set = [item for item in input_file_contents if item not in train_set]
    dev_set = random.sample(input_file_contents_minus_train_set, number_dev)
    input_file_contents_minus_train_and_dev_set = [item for item in input_file_contents_minus_train_set if item not in dev_set]
    test_set = random.sample(input_file_contents_minus_train_and_dev_set, number_test)
    rest_set = [item for item in input_file_contents_minus_train_and_dev_set if item not in test_set]

    for sentence in train_set:
        print(sentence, file=train_file)

    for sentence in dev_set:
        print(sentence, file=dev_file)

    for sentence in test_set:
        print(sentence, file=test_file)

    for sentence in rest_set:
        print(sentence, file=rest_file)










