import math

#1

print('№1:')
print("Lacit",end='\n\n')

#2

print('№2:')
print("Четверг\nМарт\nНикита",end='\n\n')

#3

print('№3:')
for i in range(5):
    print((i+1)*"0")

print('',end='\n\n')
#4

print('№4:')
print('''
   *       *       *
    *     * *     *
     *   *   *   *
       *       *
       
''')

#5,6
print('№5,6:')
print("_______\n|4|9|1|\n-------\n|3|5|7|\n-------\n|8|1|6|\n-------",end='\n\n')

#7

print('№7:')
print(1/2+1/4,end='\n\n')

#8

#a=int(input("a="))
#b=int(input("b="))
a=2
b=3
print('№8:')
print((a+4*b)*(a-3*b)+a**2,end='\n\n')

#9

#x=int(input("x="))
x=-2
print('№9:')
print(math.fabs(x)+x**5,end='\n\n')

#10

print('№10:')
x=1.7
print((x+1)**2+3*(x+1),end='\n\n')
x=3
print((x+1)**2+3*(x+1),end='\n\n')

#11

x=-2.34
print('№11:')
print( ( math.fabs(x-5) - math.sin(x) ) / 3 + (x**2 + 2014 )**(1/2) * math.cos(2*x) - 3 ,end='\n\n')

#12

print('№12:')
x=3.6
print(math.e**(x-2) + math.fabs(math.sin(x)) - x**4 * math.cos(1/x) ,end='\n\n')

#13

print('№13:')
a=0.1
b=0.2
x=1
print( (x * x + b) ** (1/5) - ( b*b * (math.sin(x+a))**3 ) / x ,end='\n\n')

#14

print('№14:')
flag=True
while flag:
    mountn = int(input('Input a number mount №'))
    if mountn==1 or mountn==2 or mountn==12:
        print('Winter',end='\n\n')
        flag=False
    elif mountn==3 or mountn==4 or mountn==5:
        print('Spring',end='\n\n')
        flag = False
    elif mountn==6 or mountn==7 or mountn==8:
        print('Summer',end='\n\n')
        flag = False
    elif mountn==9 or mountn==10 or mountn==11:
        print('Autumn',end='\n\n')
        flag = False
    else:
        print("People do not have such a month :)\nTry numbers:1-12")


#15

listforLacit=['1',1,True,1.0]
print(listforLacit)

listforLacit.append('new data')
print(listforLacit)

listforLacit.remove('new data')
print(listforLacit)

listforLacit=listforLacit[::-1]
print(listforLacit)

for i in range(len(listforLacit)):
    print(listforLacit[i])




    #2
L=['a', 1 , -2 , 1.2]
print()
print([i for i in L if (type(i)==int or type(i)==float)and i%2==0],end='\n\n')
print([L[i] for i in range(len(L)) if i%2==0],end='\n\n')
print([i for i in L if (type(i)==int or type(i)==float) and i>0],end='\n\n')
L=[1,3,4,7,9]
m=3
print( [{L[i] for i in range(len(L)) if L[i]%m==j} for l in (list(set(n%m for n in L)),) for j in l] ,end='\n\n')
L={1:2, 'a':3, -1:1, 3:'a'}
print([i+j for i in L.keys() for j in(L[i],) if (type(i)==int or type(i)==float)and(type(j)==int or type(j)==float)])
L=[3,4.1,2]
print([(i,j) for i in L for j in L if i<j],end='\n\n')
L=['a', 1 , -2 , 1.2]
print({k:v for i in range(0,int(len(L)/2+1),2) for k in (L[i],) for v in (L[i+1],)},end='\n\n')



