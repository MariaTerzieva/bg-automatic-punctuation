import sys
import re
import random


input_file_name = sys.argv[1]
train_file_name = re.sub('\.txt', '_train.txt', input_file_name)
dev_file_name = re.sub('\.txt', '_dev.txt', input_file_name)
test_file_name = re.sub('\.txt', '_test.txt', input_file_name)

with open(input_file_name,"r") as input_file, open(train_file_name,"w") as train_file, open(dev_file_name,"w") as dev_file, open(test_file_name,"w") as test_file:
    input_file_contents = input_file.read().splitlines()
    len_input_file_contents = len(input_file_contents)

    number_train = int(int(sys.argv[2]) / 100 * len_input_file_contents)
    number_dev = int(int(sys.argv[3]) / 100 * len_input_file_contents)
    number_test = len_input_file_contents - number_train - number_dev

    train_set = random.sample(input_file_contents, number_train)
    input_file_contents_minus_train_set = [item for item in input_file_contents if item not in train_set]
    dev_set = random.sample(input_file_contents_minus_train_set, number_dev)
    test_set = [item for item in input_file_contents_minus_train_set if item not in dev_set]

    for sentence in train_set:
        print(sentence, file=train_file)

    for sentence in dev_set:
        print(sentence, file=dev_file)

    for sentence in test_set:
        print(sentence, file=test_file)










