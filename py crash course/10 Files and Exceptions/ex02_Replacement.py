
from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
contents = contents.splitlines()

for line in contents:
    line = line.replace('loops','frootloops')
    print(line)