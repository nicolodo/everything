
from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
print(contents)

print()
# print each line seperately
lines = [] 
contents = contents.splitlines()
for line in contents:
    present = line
    lines.append(line)

for line in lines:
    print(line)