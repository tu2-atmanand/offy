import re

# define a function to convert the data to the desired format
def convert_data(input_str):
  # split the input string into the pattern and response
  pattern, response = input_str.strip().split('\t')
  # split the pattern into a list of individual words
  patterns = re.split(r'\s*,\s*', pattern)
  # split the response into a list of individual words
  responses = re.split(r'\s*,\s*', response)
  # return the data in the desired format
  return {'patterns': patterns, 'responses': responses}

# read the data from the input file
with open('dialogs.txt', 'r') as input_file:
  data = [convert_data(line) for line in input_file]

# write the data to the output file
with open('output.txt', 'w') as output_file:
  for item in data:
    output_file.write(f"{item['patterns']}\t{item['responses']}\n")
