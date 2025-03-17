users = {
    'enrico':{
    'first': 'enrico',
    'last': 'fermi',
    'location':'USA'
    },

    'einstein':{
        'first':'einstein',
        'last':'einstein',
        'location':'USA'
    }
}


for username, user_info in users.items():
    print(f"\nUsername: {username}")
    fullName = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']

    print(f"\tFullname: {fullName}")
    print(f"\tlocation: {location}")