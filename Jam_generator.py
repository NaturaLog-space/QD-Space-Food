R = (2,1,.5,.00125,.005,.025)

Quantity = int(input('Enter the amount of servings: '))
UnitSize = int(input('Enter the unit size: '))
BatchSize = Quantity*UnitSize
def jam(r,size):
    return r*size
print(jam(R,BatchSize))
