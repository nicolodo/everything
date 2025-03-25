
import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

with open(filename) as f_obj:
    num2 = json.load(f_obj)
print(numbers)