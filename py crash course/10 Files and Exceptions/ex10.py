
from pathlib import Path

path = Path('Anne of Avonlea.txt')

WORD = 'jam'
print(path)
# print(count(path.read_text()))
print(path.read_text(encoding="utf-8").lower().count('the '))

