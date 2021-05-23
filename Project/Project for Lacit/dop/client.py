"""
Клиент демонстрирующий работу с сервисами.
"""

from urllib.request import urlopen, Request  # для отправки запросов сервисам
import json  # для конвертации данных

# Функции


def newmodels():

    newmodels={}

    try:
        with open(r'models\models.txt', 'tr') as filewithmodels:
            id = 1
            for model in filewithmodels:
                newmodels[id] = model.split(' ')[0]
                id += 1
    except IOError:
        print('Файл model.txt недоступен, команда List не может работать коректно')
    return newmodels


def Learn(filename):
    try:
        samples={'x': [],
                 'y': []}
        with open(filename, 'tr')as filewithdata:
            for note in filewithdata:
                x1, x2, y=note.split(' ')
                samples['x'].append([x1, x2])
                samples['y'].append(y)

        data = json.dumps(samples).encode('utf-8')

        req = Request(dictconst['ADDRFORLEARN'],
                      headers={'Contest-Type': 'application/json'},
                      data=data,
                      method='POST')

        try:
            with urlopen(req) as resp:
                resp_bytes = resp.read()
                resp_str=resp_bytes.decode('utf-8')
                print(resp_str)
        except IOError:
            print('Ответ от сервера не получен.')
    except IOError:
        print('Ваш файл не доступен')


def Use(model_id, filename):
    try:
        with open(filename, 'tr') as filewithx:
            x=[]
            for xi in filewithx:
                x1, x2=xi.split(' ')
                x.append([x1, x2])
        batch = {'id': model_id,
                 'x': x}

        data = json.dumps(batch).encode('utf-8')

        req = Request(dictconst['ADDRFORAPPLY'],
                      headers={'Contest-Type': 'application/json'},
                      data=data, method='POST')

        with urlopen(req) as resp:
            resp_bytes = resp.read()
        resp_str = resp_bytes.decode('utf-8')

        print('Резудьтат:', json.loads(resp_str))
    except IOError:
        print('Ваш файл недоступен')
##

# Загрузка настроек и данных


models={}

dictconst={}

try:

    with open(r'dop\config.txt', 'tr')as config:
        const=config.readlines()
        for note in const:
            value=note.split(' ')
            dictconst[value[0]]=value[1]
except IOError as e:
    print('Файл config.txt недоступен, команда List не может работать коректно')

command=['ls', 'lr', 'u', 'q']
##

print("""
Клиент имеет следующие команды:
    1 ls показывает список обученых моделей
    2 lr обучает модель
    3 u использует одну из моделей
    4 q завершает работу
""")

# Главная функция
while True:
    comand=input('>>>')
    models=newmodels()
    if comand in command:
        if comand =='ls':

            print(models)
        elif comand=='lr':
            filename=input('''Формат данных в файле
( 
x11 x12 y1
x21 x22 y2
.........
xn1 xn2 yn
)
x = [-1,1]
y = [ 0 or 1 or 2]
Введите имя txt файла (filename.txt) : ''')
            Learn(filename)
        elif comand=='u':
            id=int(input('Введите номер модели в списке (1,2,3): '))
            filename = input('''Формат данных в файле
(  
x11 x12 
x21 x22 
.........
xn1 xn2 yn
)
x = [-1,1]
Введите имя txt файла (filename.txt) : ''')
            Use(models[id], filename)
        elif comand=='q':
             exit(0)
    else:
        print(f'Команду {comand} клиент не подерживает.\n Список досьупных команда:{command}')
##
