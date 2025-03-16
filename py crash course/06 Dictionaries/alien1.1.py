
alien = {'x': 0, 'y': 25, 'speed': 'medium'}
print(f"original position: {alien['x']}")

# move the alien to the right
# determine how far to move the alien based on its current speed
if alien['speed'] == 'medium':
    xInc = 2

# the new position is the old position plus the increment
alien['x'] = alien['x'] + xInc

print(f"the new position is {alien['x']}")

# removing key value pairs
alien = {'color': 'green', 'points': 5}
print(alien)

del alien['points']
print(alien)