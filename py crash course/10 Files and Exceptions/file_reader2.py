
from pathlib import Path

path = Path('pi_digit.txt')
contents = path.read_text()
print(contents)

# split contents into a list of each line
lines = contents.splitlines()
# build a single string with pi to 30 decimal places
for line in lines:
    print(line) 

