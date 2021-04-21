#1
'''
n=11
for i in ([i,j] for i in range(n) for j in range(i,n) if i<j):
    print(i)
'''
#2
'''
n=10
def gen_for_exercise2(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i
for i in gen_for_exercise2(n):
   print(i)
'''
#3
'''
def gen_for_exercise2(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i
def gen_for_exercise1(n):
    for i in range(n):
        for j in range(i,n):
            if i<j:
                yield [i,j]

def gen_for_exercise3(n):
    gen1=gen_for_exercise1(n)
    gen2=gen_for_exercise2(n)
    try:
        yield next(gen1)
        yield next(gen1)
        next(gen2)
        next(gen2)
    except StopIteration as e:
        print('None')
        return None
    for i in gen2:
        yield i
n=2
for i in gen_for_exercise3(n):
    print(i)
'''
#4
'''
n=10
def gen_for_exercise1(n):
    for i in range(n):
        for j in range(i,n):
            if i<j:
                yield [i,j]
def gen_for_exercise4(n):
    for i in gen_for_exercise1(n):
        yield i
for i in gen_for_exercise4(n):
    print(i)

'''
#5

#6
def gen_for_exercise6(x,y):

    try:
        yield [x,y]
        while True:

            flag=yield
            yield [x, y]
            if flag=='south':
                y+=1
                print('y+')
            elif flag=='east:':
                x+=1
                print('x+')
            elif flag=='north':
                y-=1
                print('y-')
            elif flag=='west':
                x-=1
                print('x-')
            print(flag, x, y)

    except StopIteration:
        pass
g=gen_for_exercise6(1,1)
try:
    print(next(g))
    print(next(g))
    g.send('south')
    print(next(g))

    g.send('east')
    print(next(g))

    #g.send('north')
    #g.send('west')

except StopIteration:
    print('Stop')



