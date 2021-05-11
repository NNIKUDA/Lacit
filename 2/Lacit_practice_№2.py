#1
'''
a=int(input("Input number a:"))
b=int(input("Input number b:"))
if a==b:
    print('The numbers are equal')
elif a>b:
    print('Number a is greater')
elif b>a:
    print('Number b is greater')

#2
a=float(input("Input number a:"))
b=float(input("Input number b:"))
if a==b:
    print('The numbers are equal')
elif a>b:
    print('Number a is greater')
elif b>a:
    print('Number b is greater')
#3
str=input('Input string: ')
numbers=['1','2','3','4','5','6','7','8','9']
sk=[')',']','}']
l=len(str)
for i in range(l):
    if str[i] in numbers:
        if i!=l:
            if str[i+1]! not in sk:
                if str[i+1]!=' ':
                    str=str[:i+1]+' '+str[i+1:]
print(str)
#4
import math
centralnumber=int(input("Input a central number:"))
a={k:0 for k in range(-centralnumber+1,centralnumber) }

for i in range(-centralnumber+1,centralnumber):
    if i<=0:
        k=i+centralnumber
    else:
        k=i-centralnumber
        k=int(math.fabs(k-1))
    for j in range(k):
        if i<=0:
            if j==0:
                a[j]+=1
            else:
                a[j]+=1
                a[-j]+=1
        else:
            if j==0:
                a[j]-=1
            else:
                a[j]-=1
                a[-j]-=1


    for x in range(-centralnumber+1,centralnumber):
        if a[x]==0:
            print(' ',end='')
        else:
            print(a[x],end='')
    print()

#5
import math
centralnumber=int(input("Input a central number:"))
a={k:centralnumber+1 for k in range(-centralnumber+1,centralnumber) }

for i in range(-centralnumber+1,centralnumber):
    if i<=0:
        k=i+centralnumber
    else:
        k=i-centralnumber
        k=int(math.fabs(k-1))
    for j in range(k):
        if i<=0:
            if j==0:
                a[j]-=1
            else:
                a[j]-=1
                a[-j]-=1
        else:
            if j==0:
                a[j]+=1
            else:
                a[j]+=1
                a[-j]+=1


    for x in range(-centralnumber+1,centralnumber):
        if a[x]==centralnumber+1:
            print(' ',end='')
        else:
            print(a[x],end='')
    print()

#6
import math
centralnumber=int(input("Input a central number:"))
a={k:0 for k in range(-centralnumber+1,centralnumber) }
nn =centralnumber
n = 1
while nn/10>=1:
    nn = nn / 10
    n += 1
print(n)
for i in range(-centralnumber+1,centralnumber):
    if i<=0:
        k=i+centralnumber
    else:
        k=i-centralnumber
        k=int(math.fabs(k-1))
    for j in range(k):
        if i<=0:
            if j==0:
                a[j]+=1
            else:
                a[j]+=1
                a[-j]+=1
        else:
            if j==0:
                a[j]-=1
            else:
                a[j]-=1
                a[-j]-=1


    for x in range(-centralnumber+1,centralnumber):


        if a[x]==0:
            print(' '*n,end='')
        else:

            nn = a[x]
            nx = 1
            while nn/10>=1:
                nn = nn / 10
                nx += 1


            if nx!=n:
                print(str(a[x])+" "*(n-nx),end='')
            else:
                print(str(a[x]) , end='')
    print()

#7
import math
centralnumber=int(input("Input a central number:"))
a={k:centralnumber+1 for k in range(-centralnumber+1,centralnumber) }
n = 1
nn=centralnumber
while nn/10>=1:
    nn = nn / 10
    n += 1
for i in range(-centralnumber+1,centralnumber):
    if i<=0:
        k=i+centralnumber
    else:
        k=i-centralnumber
        k=int(math.fabs(k-1))
    for j in range(k):
        if i<=0:
            if j==0:
                a[j]-=1
            else:
                a[j]-=1
                a[-j]-=1
        else:
            if j==0:
                a[j]+=1
            else:
                a[j]+=1
                a[-j]+=1


    for x in range(-centralnumber+1,centralnumber):
        if a[x] == centralnumber+1:
            print(' ' * n, end='')
        else:

            nn = a[x]
            nx = 1
            while nn / 10 >= 1:
                nn = nn / 10
                nx += 1

            if nx != n:
                print(str(a[x]) + " " * (n - nx), end='')
            else:
                print(str(a[x]), end='')
    print()


#8
clas=int(input('Введите класс - '))
dict={0:[1,2,3,4] ,1:[5,6,7,8,9], 2:[10,11]}
if clas in dict[0] :
    print('Степень первая')
elif clas in dict[1]:
    print('Степень вторая')
elif clas in dict[2]:
    print('Степень третья')
else:
    print('Такого класса нету')

#9
str1=input('Input string: ')
for i in range(len(str1)):
    print(ord(str1[i]))

#10
str1=input('Input string: ')
sum=0
for i in range(len(str1)):
    sum+=ord(str1[i])
print('Сумма:',sum)

#11
dict1={0:3,1:2,2:1}
ks=dict1.keys()
ks=sorted(ks)
for i in range(len(dict1)):
    print(dict1[ks[i]])

#12
listt=[1,2,3,4,5,6,7,8,9,10]
searchx=10
xx=0
while xx<len(listt):

    if listt[xx]==searchx:
        print("Игдекс числа -",xx)
        break
    xx+=1

else:
    print("Числа нет в списке!")

#13
listt=[1,2,3,4,5,6,7,8,9,10]
searchx=11

for i in range(len(listt)):

    if listt[i]==searchx:
        print("Игдекс числа -",i)
        break


else:
    print("Числа нет в списке!")
'''
