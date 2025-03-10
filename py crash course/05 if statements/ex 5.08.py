def ex8to10():
    current_usernames = ['admin','josh','finesbarne','gert','harry']
    new_users = ['Max','Poppy','josh','gert','harry']
    usernames = current_usernames

    # convert to lowercase
    lower_current_users = current_usernames[:]
    for user in range(len(lower_current_users)):
        lower_current_users[user] = lower_current_users[user].lower()

    if usernames:
        for user in usernames:
            if user == 'admin':
                print("Hello Administrator")
            else:
                print(f"Hello {user}!")
    else:
        print("We need to find some users")

    # duplicates test
    if new_users:
        for user in new_users:
            if user.lower() in lower_current_users:
                print(f"username {user} in use")
            else:
                print(f"username {user} available")

def ex11():
    # ordinal numbers
    numbers = [1,2,3,4,5,6,7,8,9]
    suffix = ['th','st','nd','rd','th']
    for n in numbers:
        if n <= 3: 
            print(f"{str(n)}{suffix[n]}")
        else:
            print(f"{str(n)}{suffix[0]}")
ex11()