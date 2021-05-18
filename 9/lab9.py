#1
'''
def f():pass
print(f)

class C:
  def h(self): pass
c = C()
def fun(self):
  print(1)
  return "1"

f.__repr__ = type(c.h)(fun, f)
print(f)

f.__repr__()
'''
#Изменяется dict функции f a при print(f) вызывается метод класса изменить встроеный метод класса но это врде нельзя сделать в этоислучае




#3
import collections

newdict=collections.defaultdict(lambda: 0)
def f():pass
f.__dict__=newdict
print(f.__dict__[1])
#как добраться до стандартного dict
#Скорее всего у них создается свой конструктор

