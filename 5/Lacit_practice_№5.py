import  math
print((type(1)== int))
#1
class Sphere:
    def __init__(self):
        self.r = 1
        self.x = 0
        self.y = 0
        self.z = 0
    def __init__(self,r=1):
        if r is float or int:
            self.r=float(r)
            self.x=0
            self.y=0
            self.z=0
    def __init__(self,r=1,x=0,y=0,z=0):
        if ((type(r) == float) or (type(r) == int))and((type(x) == float) or (type(x) == int))and((type(y) == float) or (type(y) == int))and((type(z) == float) or (type(z) == int)):
            self.r = float(r)
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)
    def get_volume(self):
        return (4/3)*math.pi*self.r**3
    def get_square(self):
        return 4*math.pi*self.r**2
    def get_radius(self):
        return self.r
    def get_center(self):
        return (self.x,self.y,self.z)
    def set_radius(self,r):
        if r is float or int:
            self.r=r
    def set_center(self,x,y,z):
        if (x is float or int)and(y is float or int)and(z is float or int):
            self.x=x
            self.y=y
            self.z=z
    def is_point_inside(self,x,y,z):
        if self.x**2+self.y**2+self.z**2==self.r:
            return True
        else:
            return  False
#2,3,4
class Point :
    def __init__(self,x=0,y=0):
        if ((type(x) == float) or (type(x) is int))and ((type(y) is float) or (type(y) is int)):
            self.x=x
            self.y=y
    def getXY(self):
        return [self.x,self.y]
    def Show(self):
        print('x='+str(self.x)+'y='+str(self.y))
    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self,other):
        return Point(self.x - other.x, self.y - other.y)
    def __eq__(self,other):
        if (self.x==other.x)and(self.y==other.y):
            return True
        else:
            return False
    def __mul__(self,other):
        return Point(self.x * other.x,self.y * other.y)
    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)
'''
point1=Point(1,1)
point1XY=point1.getXY()
print(f"x="+str(point1XY[0])+"y="+str(point1XY[1]))
point2=Point(2,2)
point3=point1+point2
print(point3)
print((point1-point2).x)
print((point1*point2).x)
print((point1/point2).x)
print(point1==point1)

'''#5
class Drob :
    def __init__(self,numerator,denominator):
        if ((type(numerator) == float)or(type(numerator) == int))and((type(denominator) == int)or(type(denominator) == float)):
            self.numerator=numerator
            self.denominator=denominator
        else:
            print("Is not int and float")
    def normalize(self):
        if self.numerator > self.denominator:
            self.numerator,self.denominator=self.denominator,self.numerator
        for i in range(1,max(self.numerator,self.denominator)+1):
            if self.numerator%i==0 and self.denominator%i==0:
                self.numerator/=i
                self.denominator/=i
    def __str__(self):
        return str(self.numerator)+'/'+str(self.denominator)
    def denomer(self,other):
        if self.denominator > other.denominator:
            denominator = self.denominator
            otherdenominator = other.denominator
        else:
            denominator = other.denominator
            otherdenominator = self.denominator
        n = denominator
        while denominator % otherdenominator!=0:
            denominator += n
        return denominator
    def __add__(self,other):
        if self.denominator==other.denominator:
            return Drob(self.numerator+other.numerator,self.denominator)
        else:
            denominator=self.denomer(other)
            return Drob((denominator/self.denominator*self.numerator)+(denominator/other.denominator*other.numerator),denominator)
    def __sub__(self,other):
        if self.denominator == other.denominator:
            return Drob(self.numerator - other.numerator, self.denominator)
        else:
            denominator = self.denomer(other)
            return Drob(
                (denominator / self.denominator * self.numerator) - (denominator / other.denominator * other.numerator),
                denominator)
    def __mul__(self,other):
        return Drob(self.numerator*other.numerator,self.denominator*other.denominator)
    def __truediv__(self,other):
        return Drob(self.numerator*other.denominator,self.denominator*other.numerator)
    def __eq__(self,other):
        if self.numerator==other.numerator and self.denominator==other.denominator:
            return True
        else:
            return False
    def __gt__(self,other):
        if self.denominator==other.denominator:
            if self.numerator>other.numerator:
                return True
            else:
                return False
        else:
            d=self.denomer(other)
            if  d/self.denominator*self.numerator>d/other.denominator*other.denominator:
                return True
            else:
                return False
    def __lt__(self,other):
        if self.denominator==other.denominator:
            if self.numerator<other.numerator:
                return True
            else:
                return False
        else:
            d=self.denomer(other)
            if  d/self.denominator*self.numerator<d/other.denominator*other.denominator:
                return True
            else:
                return False
    def __ge__(self,other):
        if self.denominator==other.denominator:
            if self.numerator>=other.numerator:
                return True
            else:
                return False
        else:
            d=self.denomer(other)
            if  d/self.denominator*self.numerator>=d/other.denominator*other.denominator:
                return True
            else:
                return False
    def __le__(self,other):
        if self.denominator==other.denominator:
            if self.numerator<=other.numerator:
                return True
            else:
                return False
        else:
            d=self.denomer(other)
            if  d/self.denominator*self.numerator<=d/other.denominator*other.denominator:
                return True
            else:
                return False

'''
a=Drob(1,2)
b=Drob(2,4)
b.normalize()
print(a)
print(b)
print(a==b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
'''
#6
class Snow:
    def __init__(self,n=1):
        if type(n)==int:
            self.n=n
    def __add__(self,other):
        self.n+=other
        return self
    def __sub__(self,other):
        self.n-=other
        return self
    def __mul__(self,other):
        self.n*=other
        return self
    def __truediv__(self,other):
        self.n/=other
        self.n=round(self.n)
        return self
    def __str__(self):
        return str(self.n)
    def makeSnow(self,arg):
        n=self.n+1
        while n>0:
            for i in range(arg):
                n-=1
                if n>0:
                    print('*',end='')
            print()
'''
a=Snow(5)
a+5
a.makeSnow(4)
'''
#7
class Human:
    default_name='Иван' #статические
    default_age=20
    def __init__(self,name=default_name,age=default_age):
        self.name=name
        self.age=age
        self.__money=0
        self.__property=[]
    def info(self):
        print("Name:",self.name,
              '\nAge:',self.age,
              '\nMoney',self.__money,
              '\nProperty:',self.__property)
    def default_info(self):
        print("Default name:",Human.default_name,
              '\nDefault age:',Human.default_age)
    def __make_deal(self,discrip,price):
        self.__property.append(discrip)
        self.__money-=price
    def earn_money(self,n):
        self.__money+=n
    def buy(self,discrip,price):
        if price<=self.__money:
            self.__make_deal(discrip,price)
        else:
            print('Not money')
    def __iadd__(self,other):
        self.__money+=other
        return self
    def __isub__(self,other):
        self.__money-=other
        return self
    def __imul__(self,other):
        self.__money*=other
        return self
    def __itruediv__(self,other):
        self.__money/=other
        return self
    def __eq__(self,other):
        if(self.age+len(self.name)==other.age+len(other.name)):
            return True
        else:
            return False
    def __gt__(self,other):
        if(self.age+len(self.name)>other.age+len(other.name)):
            return True
        else:
            return False
    def __lt__(self,other):
        if(self.age+len(self.name)<other.age+len(other.name)):
            return True
        else:
            return False
    def __ge__(self,other):
        if(self.age+len(self.name)>=other.age+len(other.name)):
            return True
        else:
            return False      
    def __le__(self,other):
        if(self.age+len(self.name)<=other.age+len(other.name)):
            return True
        else:
            return False  


a=Human('A',10)
a.info()
a.earn_money(10)
a.buy('c',5)
a.info()
a.buy('v',6)
a+=10
a.info()
