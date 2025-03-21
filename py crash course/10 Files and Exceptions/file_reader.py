
with open('pi_digit.txt') as file_object:
    contents = file_object.read()
    # print(contents)
    print(contents.rstrip())

# 2nd bit
print()
filename = 'pi_digit.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# 3rd bit
print()
filename = 'pi_digit.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())