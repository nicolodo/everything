

filename = 'pi_digit.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

#making a variable of the files contents
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
