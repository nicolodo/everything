
def ex3():
    for x in range(1,20+1,1):
        print(x)

# ex 4.04 one million count
# pause = input("exercise 4.04 is starting press enter to begin")
def ex4():
    for x in range(1,10**6,1):
        print(x)

# sum to a million 
def ex5():
    millionList = list(range(1,10**6+1,1))
    print(f"min value = {min(millionList)}")
    print(f"max val in list: {max(millionList)}")
    print(f"sum of millionList: {sum(millionList)}")

def ex6():
    # odd numbers
    for odd in range(1,20+1,2):
        print(odd)

def ex7():
    # threes, multiples of 3 from 3 to 30
    for three in range(3,30+1,3):
        print(three)

def ex8():
    # cubes, print the first ten cubes
    for cube in range(1,10+1,1):
        print(cube**3)

def ex9():
    # cube comprehension
    cubes = [num**3 for num in range(1,11,1)]
    print(cubes)

# do you like comments?