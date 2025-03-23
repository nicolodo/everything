
from pathlib import Path

path = Path('guest.txt')

prompt = "Please enter your name: "
userName = input(prompt)

path.write_text(userName)