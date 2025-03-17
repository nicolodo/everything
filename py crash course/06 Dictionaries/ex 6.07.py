
#7 people
def ex7():
    josh = {
        'fname': 'Josh',
        'lname': 'Davey',
        'city': 'Ipswich',
        'age': 25 }

    rafaele = {
        'fname': 'rafaele',
        'lname': 'avino',
        'city': 'naples',
        'age': 23
    }

    Sammy = {
        'fname': 'samuel',
        'lname': 'osborne',
        'city': 'ipswich',
        'age': 25
    }

    people = [Sammy,josh,rafaele]

    for person in people:
        # print(person)
        # for name, v in person.items():
            # print(f"{name} is {str(v['age'])} years old and lives in {v['city']}")
        print(f"{person['fname']} is {person['age']} years, and lives in {person['city']}")

# pets 8

def ex8():
    jeb = {
        'animal':'sheep',
        'owner':'jeb',
        'name': 'jeb'
    }

    bob = {
        'animal':'cat',
        'owner': 'carmichael',
        'name': 'bob'
    }

    phil = {
        'animal': 'fish',
        'owner': 'frederik',
        'name': 'phil'
    }

    pets = [jeb,bob,phil]

    for pet in pets:
        print(f"{pet['name']} is a {pet['animal']} owned by {pet['owner']}")

ex8()