
from pathlib import Path

path = Path('guest_book.txt')

# Names = []
Names = ''
active = True

while not active:
    Names += f"jsut \n work\nplease"
    # print("hi")
    break

prompt = "Please enter your name: "
while active:
    name = input(prompt)
    Names += name 
    if name == '':
        break
    # Names.append(name)
    Names += '\n'

print(Names)

path.write_text(Names)
print("finished")