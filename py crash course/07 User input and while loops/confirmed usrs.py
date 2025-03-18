
# confirmed usrs

unconfirmedUsers = ['Jim','Bim','Bob','Bab']
confirmedUsers = []

while unconfirmedUsers:
    currentUser = unconfirmedUsers.pop()
    print(f"Validating {currentUser}")
    confirmedUsers.append(currentUser)

for user in confirmedUsers:
    print(f"{user} has been confirmed")