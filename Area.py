a=int(input('Enter first side:'))
b=int(input('Enter second side:'))
c=int(input('Entr third side:'))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('The area of the triangle is %0.2f'%area)