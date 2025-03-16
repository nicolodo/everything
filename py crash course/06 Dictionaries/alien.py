
# alien_0 = {'color':'green','points':5}

# print(alien_0['color'])
# print(alien_0['points'])
# print(alien_0)
# alien_0['x'] = 0
# alien_0['y'] = 25
# print(alien_0)

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# modifying values in memory
alien_0 = {'color':'green'}
print(f"The alien is color {alien_0['color']}")
alien_0['color'] = 'yellow'
print(f"The alien is now color {alien_0['color']}")