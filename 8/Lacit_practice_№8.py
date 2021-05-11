import numpy,random
#1
'''
class Person:
    def __init__(self,*args):
        if len(args)==2:
            self.fullName=args[0]
            self.age=args[1]
        elif len(args)==0:
            self.fullName=None
            self.age=None
    def move(self):
        print(f"Такой-то {self.fullName} говорит")
    def talk(self):
        print(f"Такой-то {self.fullName} говорит")
    def getName(self):
        return self.fullName

person1=Person()
person1.move()
person2=Person("Alex",32)
person2.move()
'''
#2
'''
class Phone:
    def __init__(self,*args):
        if len(args)==3:
            self.number=args[0]
            self.model=args[1]
            self.weight=args[2]

            #a=self.__init__(self,args[0],args[1])#это вызов конструктора с 2 параметрами из конструктора с 3
        elif len(args)==2:
            self.number = args[0]
            self.model = args[1]
            self.weight=None
        elif len(args)==0:
            self.number = None
            self.model = None
            self.weight = None

    def receiveCall1(self,name):
        print(f'Звонит {name}')
    def getNumber(self):
        return self.number
    def sendMessage(self,*args):
        for _ in args:
            print(_)
    def receiveCall2(self,name,number):
        print(name ,number)


Phone1=Phone('+3752934343','Huawei','100')
Phone2=Phone('+4234324234','Huawei','120')
Phone3=Phone('+1874358774','Huawei','120')

Phone1.receiveCall1('Alex')
print(Phone1.getNumber(),Phone1.model,Phone1.weight)
Phone2.receiveCall1('Alex')
print(Phone2.getNumber(),Phone2.model,Phone2.weight)
Phone3.receiveCall1('Alex')
print(Phone3.getNumber(),Phone3.model,Phone3.weight)

Phone1.receiveCall2('Alex',Phone2.getNumber())
Phone2.receiveCall2('Alex',Phone3.getNumber())
Phone3.receiveCall2('Alex',Phone1.getNumber())

Phone1.sendMessage(Phone2.getNumber(),Phone3.getNumber())
'''
#3
'''
class matriza:
    __slots__=('matriza','stroks','stolbs')
    def __init__(self,stroks=2,stolbs=2,*matriza):
        self.stroks=stroks
        self.stolbs=stolbs
        if len(matriza)>=stolbs*2:
            self.matriza=numpy.array([[matriza[i] for i in range(stolbs) ],[matriza[i] for i in range(stolbs,stolbs*2)]],  dtype=float)
        else:
            self.matriza=numpy.empty(2,2)
    def add(self,other):
        array=numpy.zeros((2,self.stolbs))

        if self.stolbs==other.stolbs:
            for i in range(self.stroks):
                for j in range(self.stolbs):
                    array[i][j]=self.matriza[i][j]+other.matriza[i][j]
        print(array)
    def mul(self,other):
        array=numpy.zeros((2,self.stolbs))
        for i in range(self.stroks):
            for j in range(self.stolbs):
                array[i][j] = self.matriza[i][j] * other
        print(array)
    def print(self):
        print(self.matriza)
m1=matriza(2,2,1,1,1,1)
print(m1.matriza)
m2=matriza(2,2,2,2,2,2)
print(m2.matriza)
m1.add(m2)
m1.mul(5)
m1.print()

'''
#4
'''
class Reader:
    __slots__=('fullname','id','facultet','date_of_birth','phone')

    def __init__(self,fullname):
        self.fullname=fullname

    def get_fullname(self):
        return self.fullname
    def set_fullname(self,fullname):
        self.fullname=fullname

    def get_id(self):
        return self.id
    def set_id(self,id):
        self.id=id

    def set_facultet(self,facultet):
        self.facultet=facultet
    def get_facultet(self):
        return self.facultet

    def set_date_of_birth(self,date_of_birth):
        self.date_of_birth=date_of_birth
    def get_date_of_birth(self):
        return self.date_of_birth

    def set_phone(self,phone):
        self.phone=phone
    def get_phone(self):
        return self.phone

    def takeBook1(self,num):
        print(f'{self.fullname} взял {num} книги')
    def takeBook2(self,*books):
        print(f'{self.fullname} взял книги:', ' '.join(books))
    def takeBook3(self,*books):
        print(f'{self.fullname} взял книги:', " ".join([i.getname() for i in books]))
    def returnBook1(self,num):
        print(f'{self.fullname} вернул {num} книги')
    def returnBook2(self,*books):
        print(f'{self.fullname} вернул книги:', ' '.join(books))
    def returnBook3(self,*books):
        print(f'{self.fullname} вернул книги:', " ".join([i.getname() for i in books]))

class book:
    __slots__=('author','name')
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name
    
mas=numpy.array([Reader('Петров П.П.'),Reader('Иванов В.В.'),Reader('Антонов А.А.')])
mas[0].takeBook1(2)
mas[1].takeBook2('a','b','c')
mas[2].takeBook3(book('a'),book('b'),book('c'))
mas[0].returnBook1(2)
mas[1].returnBook2('a','b','c')
mas[2].returnBook3(book('a'),book('b'),book('c'))
'''
#5
class project:
    __slots__=('name','cost','strings_need','strings_ready')
    def __init__(self,name,cost,strings_need):
        self.name=name
        self.cost=cost
        self.strings_need=strings_need
        self.strings_ready=0
    def getcost(self):
        return self.cost
    def getstringsneed(self):
        return self.strings_need
    def getstringsready(self):
        return self.strings_ready
    def setstringsready(self,string):
        self.strings_ready=string
    def getname(self):
        return self.name
class programmer:
    __slots__=('fullname','level',)
    def __init__(self,name,level):
        self.fullname=name
        self.level=level
    def getlevel(self):
        return self.level

class manager :
    __slots__=('fullname','programmers','project')
    def __init__(self,name,programmers,project):
        self.fullname = name
        self.programmers=programmers
        self.project=project
    def getproject(self):
        return self.project
    def setproject(self,project):
        self.project=project
    def getprogrammers(self):
        return self.programmers
    def getfullname(self):
        return self.fullname

manag=manager('A'  ,  [ programmer('B',random.randrange(1,4,1)) , programmer('C',random.randrange(1,4,1)) , programmer('D',random.randrange(1,4,1)) ]  ,  project('1' , random.randrange(1,10000,1000) , random.randrange(1,10000,1000)) )
capital=10000
mount=0
while capital>0:
    print(f'Месяц №{mount} \nКапитал {capital}')
    if(manag.getproject().getstringsneed()<=manag.getproject().getstringsready()) :
        capital +=manag.getproject().getcost()
        print(f'Проект {manag.getproject().getname()} закончен')
        manag.setproject(  project('1' , random.randrange(1,10000,1000) , random.randrange(1,10000,1000)) )
        print(f'Начат проект {manag.getproject().getname()}')
    for _ in manag.getprogrammers():
        if _.getlevel()==1:
            manag.getproject().setstringsready(manag.getproject().getstringsready()+100)
            capital-=100
        elif _.getlevel() == 2:
            manag.getproject().setstringsready(manag.getproject().getstringsready() + 200)
            capital -= 200
        elif _.getlevel() == 3:
            manag.getproject().setstringsready(manag.getproject().getstringsready() + 300)
            capital -= 300
    mount += 1
else:
    print('Вы проиграли')

