# ex 3 print a dictionary of programming terms
# 

terms = {
    'variable': 'a value stored in memory that can be edited',
    'constant': 'a value stored in momory that can not be edited',
    'comment': 'a message in the code for the benefit of the programmer and other readers',
    'boolean': 'a value that is either TRUE or FALSE denoted as 1 or 0',
    'editor': 'the software the code is written in that provides features such as syntax highlighting'
}

def ex3():
    for term in terms:
        print(f"{term}: {terms[term]}\n")

def ex4():
    for k,v in terms.items():
        print(f"{k}: {v}")

# ex5 Rivers

rivers = {
    'Nile': 'Egypt', 
    'Yellow River': 'China', 
    'Missisippi': 'USA'
}

countries = {
    'Egypt': 'This runs through egypt and it regularly floods which helps with food',
    'China': 'This is in china it is quite large I think',
    'USA': 'This American river is navigable and is used for transporting goods by barge'
}

for river, country in rivers.items():
    print(f"The {river} is in {country}")


# ex 6
# uses the code from favourite languages

favorite_languages = {
    'jen': 'python',
    'charles': 'C',
    'Benny': 'Java',
    'House': 'Rust',
    'Mike': 'python'
}

# language = favorite_languages['jen'].title()
# print(f"Jen's favourite language is {language}")

for k,v in favorite_languages.items():
    print(k,':',v)

# who should take the poll list?

shouldTakePoll = ['jen','Mike','Will','Johnson']

for person in shouldTakePoll:
    if person in favorite_languages.keys():
        print(f"{person} thank you for taking the poll")
    else:
        print(f"{persons}")