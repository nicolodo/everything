def ex10():
    players = ['cherles','marina','michael','florence','ellie']
    print(players)
    print("here are the first 3 players on my team:")
    for player in players[:3]:
        print(player)

    print(players[:3])
    point = round(len(players)/2)
    print(players[point-1:point+2])
    print(players[-3:])

def ex11():
    pizzas = ['hawaian','cheese and tomato','pecans','pencils']
    friend_pizzas = pizzas[:]
    pizzas.append('beans')
    friend_pizzas.append('microbes')
    for pizza in pizzas:
        print(f"I like {pizza} pizza")
    for pizza in friend_pizzas:
        print(f"my friend likes: {pizza}")
    print("Gosh I like pizza")

ex11()