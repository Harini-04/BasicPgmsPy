'''
#Rightpyramid

def pattern(n):
    for i in range(1,n+1):
        print(""*(n-i),"*" *i)

n=int(input("Enter no:"))
pattern(n)
'''

'''
#Alphabet pattern
for x in range(65,70):
    for y in range(65,x+1):
        print(chr(y),end='')
    print()
''' 
#All Alphabets 
n=int(input("Enter no:"))
ascii=65 
for i in range(n):
    print((n-i-1)*" ",end=" ")
    for j in range(0,i+1):
        print(chr(ascii),end=' ')
        ascii+=1 
    print()
