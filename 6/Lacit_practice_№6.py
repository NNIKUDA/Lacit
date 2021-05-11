n=10
#1

'''
for i in (str(i)+' '+str(j) for i in range(n) for j in range(i,n) if i<j):
    print(i)
'''
#2
'''

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

for i in gen_for_exercise3(n):
    print(i)
'''
#4

'''
def gen_for_exercise4(n):
    for i in (str(i)+' '+str(j) for i in range(n) for j in range(i,n) if i<j):
        yield i
for i in gen_for_exercise4(n):
    print(i)

'''
#5
'''
def gen_for_exercise5(n):
    for i in (str(i)+" "+str(j) for i in range(n) for j in range(i, n) if i < j):
        for j in i:
            if j in ['0','1','2','3','4','5','6','7','8','9']:
                yield j
for i in gen_for_exercise5(n):
    print(i)

'''
#6
'''
def gen_for_exercise6(x,y):
    while True:
        send= yield [x,y]
        if send=='south':
            y+=1
        if send=='east':
            x+=1
        if send=='north':
            y-=1
        if send=='west':
            x-=1
        if send=='stop':
            break


g=gen_for_exercise6(1,1)
try:
    print(g)
    print(next(g))
    print(g.send('south'))
    print(g.send('east'))
    print(g.send('north'))
    print(g.send('west'))
    print(g.send('stop'))
except StopIteration:
    pass

'''
#7
'''
import  asyncio,datetime

async def read_file(fname):
    f=open(fname,'r')
    n=0
    for char in f.read():
        n+=1
    f.close()
    return n



async def read_file_for_exicise(fname):
    print(datetime.datetime.now())
    a=await read_file(fname)
    print(a,datetime.datetime.now())
    b=await read_file(fname)
    print(b,datetime.datetime.now())
asyncio.run(read_file_for_exicise('f.txt'))


'''