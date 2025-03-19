
# ex8-13 Cars

def carInfo(manufacturer='hyundai',make='slamami',**carAttributes):
    print(manufacturer,make)
    carAttributes['manufacturer'] = manufacturer
    carAttributes['make'] = make

    return carAttributes

car = carInfo(color='blur',music='blastin',seats='brown')
print(car)