from random import randrange


words=['перпендикуляр','файл','экран','ссылка','интернет','баг','дизайнер','тестировщик','техподдержка','документация'] #Список загадываемых слов
flag=1  #Флаг указывает будет ли продолжаться игра
bukvs='йцукенгшщзхъфывапролджэячсмитьбю' #Допустимые символы ввода

#запрос символа
def inputbuk():
    #Функция запрашивает допустимый символ ввода
    b='0'
    while b not in bukvs :
        b=input("Введите букву(маленькую букву русского алфавита): ")
    return b

#отрисовка человека
def painthum(f):
    #Функция отрисовывает человечка  f - количество неправельных ответов
    if f == 0:
        print('''





                
                ''')
    if f == 1:
        print('''
                  
                        
                        
                            
                       
                ____ 
                ''')
    if f == 2:
        print('''
    
                  |      
                  |      
                  |          
                  |     
                __|__ 
                ''')
    if f == 3:
        print('''
                  ________
                  |      
                  |      
                  |          
                  |     
                __|__ 
                ''')
    if f == 4:
        print('''
                  ________
                  |      |
                  |      
                  |          
                  |     
                __|__ 
                ''')
    if f == 5:
        print('''
                  ________
                  |      |
                  |      0
                  |          
                  |     
                __|__ 
                ''')
    if f == 6:
        print('''
                  ________
                  |      |
                  |      0
                  |      |     
                  |     
                __|__ 
                ''')
    if f == 7:
        print('''
                  ________
                  |      |
                  |      0
                  |     /|     
                  |     
                __|__ 
                ''')
    if f == 8:
        print('''
                  ________
                  |      |
                  |      0
                  |     /|\     
                  |     
                __|__ 
                ''')
    if f == 9:
        print('''
                  ________
                  |      |
                  |      0
                  |     /|\     
                  |     / 
                __|__ 
                ''')
    if f == 10:
        print(r'''
                  ________
                  |      |
                  |      0
                  |     /|\     
                  |     / \
                __|__ 
                ''')

#Отрисовка слова
def paintword(numword,bukvs):
    print("                _",end='')
    for i in range(len(words[numword])):
        print("__",end='')
    print()

    print('                |',end='')
    for i in words[numword]:
        if i in bukvs:
            print(i,end='')
            print('|', end='')
        else:
            print('*',end='')
            print('|', end='')
    print()

    print("                -", end='')
    for i in range(len(words[numword])):
        print("--", end='')
    print()

#Главный цикл игры
def game():
    print("Игра началась")
    numrandword=randrange(0,len(words),1)
    fail = 0        #Количество ошибок игрока
    goodbuk = 0     #Количество угаданых букв
    goodbukvs=[]    #Список угаданых букв
    inbukvs=[]    #Список полученых букв которых нет в слове
    paintword(numrandword,goodbukvs)

    while ( goodbuk!=len(words[numrandword]) ) and ( fail!=10 ) :    #Цикл запросов букв
        inbuk=inputbuk()
        if inbuk not in inbukvs :
            if inbuk in words[numrandword]:
                goodbuk+=1
                goodbukvs.append(inbuk)
                inbukvs.append(inbuk)
            else:
                fail+=1
                inbukvs.append(inbuk)
        else:
            print('Вы вводили эту букву')
        print("Ваши буквы:", inbukvs)
        paintword(numrandword, goodbukvs)
        painthum(fail)

    if (fail == 10):
        print("Увы, вы проиграли ,я загадал слово ", words[numrandword])
        answe = input("Хотите сыграть еще?\n (Д/д - да ) ")
        if answe == "Д" or answe == "д":
            return 1
        else:
            return 0
    else:
        print("Вы, вы победили поздравляю слово:",words[numrandword])
        answe = input("Хотите сыграть еще?\n (Д/д - да ) ")
        if answe == "Д" or answe == "д":
            return 1
        else:
            return 0

while(flag==1):
    flag=game()





