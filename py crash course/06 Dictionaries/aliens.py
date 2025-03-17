
# alien0 = {'color':'green','points':5}
# alien1 = {'color':'yellow','points':10}
# alien2 = {'color':'red','points':15}

# aliens = [alien0,alien1,alien2]

# for alien in aliens:
#     print(alien)

#make an empty list for storing aliens
aliens = []

# make 30 green aliens
for alienNo in range(30):
    newAlien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(newAlien)

# modify the first 3 aliens
for alienNo in range(3):
    print(alienNo)
    aliens[alienNo]['color'] = 'yellow'
    aliens[alienNo]['points'] = 10 
    aliens[alienNo]['speed'] = 'medium'

#show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens have been created
print(f"Total Number of aliens: {len(aliens)}")
