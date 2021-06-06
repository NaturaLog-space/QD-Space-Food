R = (2,1,.5,.00125,.005,.025)

Quantity = int(input('Enter the amount of servings: '))
UnitSize = int(input('Enter the unit size: '))
BatchSize = Quantity*UnitSize
def jam(r,size):
    temp=[]
    for x in r:
        temp.append(x*size)
    return temp
print(jam(R,BatchSize))
