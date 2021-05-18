import module1 as m1
m1.base.loaddata('names,phones.csv')
def getname(phone):
    if phone in m1.base.database.keys():
        print('Имя владельца телефона - ',m1.base.database[phone])
    else:
        print("Такого телефона нет в базе данных")
getname('1')