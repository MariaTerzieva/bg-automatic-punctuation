# arguments are:
# sys.argv[1] - the name of the output file where files will be merged into one
# sys.argv[2] - sys.argv[number_of_command_line_arguments] - the names of the files we want to merge into one
# outcome:
# we have the merged contents of all the files into the output file (sys.argv[1])

import sys

  
number_of_command_line_arguments = len(sys.argv)
file_names = []

for i in range(2, number_of_command_line_arguments):
    file_names.append(sys.argv[i])
  
with open(sys.argv[1], "w") as output_file: 
    for file_name in file_names:
        with open(file_name) as file:
            output_file.write(file.read())
