R = (2,1,.5,.00125,.005,.025)

Quantity = int(input('Enter the amount of servings: '))
UnitSize = int(input('Enter the unit size: '))
BatchSize = Quantity*UnitSize
def jam(r,size):
    temp=[]
    total=0
    for x in r:
        temp.append(x*size)
        total+=(x*size)
    return temp,total
print(jam(R,BatchSize))
