
import json

filename = 'numbers.json'
numbers = [2,4,5,7,9]

with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)

# with open(filename) as f_obj:
#     num2 = json.load(f_obj)
#     print(num2)