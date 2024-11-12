import re

# Define the patterns and their respective replacement strings
patterns = [
    (r'TS', '\nTS'),   # replace "foo" with "bar"
    (r'AP', '\nAP'),       # replace any number with "123"
    (r'\n$', ''),
    (r' ', ''),
    (r'O', '0'),
    (r'I', '1'),
    (r'-', '.'),
    (r'0S', '08'),
    (r'0B', '08'),
    (r'0R', '08'),
    (r'T5', 'TS'),
    (r'2S', '25'),
    (r'1S', 'TS'),
    (r'SB0', 'S30'),    
    (r'[^\w\s.-]', ''),
    (r'[^\w\s]$', '')
]

# Read the contents of the file into a string variable
with open('input', 'r') as f:
    content = f.read()

# Perform the replace operations using regular expressions
for pattern, repl in patterns:
    content = re.sub(pattern, repl, content)

# Write the modified string back to the file
with open('output.txt', 'w') as f:
    f.write(content)


with open('output.txt', 'r') as file:
    content = file.read()

# Define the regular expression pattern to match special characters at the end of a line
pattern = re.compile(r'[^\w\s]+$|\n$')

# Remove special characters and extra new line characters from the end of each line
lines = ' '.join([pattern.sub('', line).rstrip('\n')  for line in content.splitlines()]).split()

# Open the output file and write the modified lines
with open('output.txt', 'w') as file:
    file.write('\n'.join(lines))