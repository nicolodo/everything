
from pathlib import Path

try:
    catsPath = Path("cats.txt")
    dogsPath = Path("dogs.txt")
except FileNotFoundError:
    pass
    print("I'm sorry we can't find your pet")
else:
    print(catsPath.read_text())
