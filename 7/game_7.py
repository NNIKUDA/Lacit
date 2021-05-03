import random
print(dir(random))
randnum=random.randrange(1,101,1)
num=int(input('Введите чило (1-100):'))
if randnum==num:
    print('Победа')
else:
    print('Повторите еще раз')

