from math import *
from tkinter import *
import random

root = Tk()

canv = Canvas(root, width=500, height=500, bg="white")
canv.create_line(250, 500, 250, 0, width=2, arrow=LAST)
canv.create_line(0, 250, 500, 250, width=2, arrow=LAST)

a=-200
b=200
color1='#'+str(random.randrange(100,1000,1))
color2='#'+str(random.randrange(100,1000,1))
aa=a
while aa<b:
    x=aa
    y=x**3-6*x**2+x+5
    canv.create_oval(250+x, 250-y,252+x, 252-y, fill=color1 ,outline=color1)
    aa+=0.01
aa=a
while aa<b:
    x=aa
    y=(x-2)**2-6
    canv.create_oval(250 + x, 250 - y, 252 + x, 252 - y, fill=color2,outline=color2)
    aa += 0.001
canv.pack()
root.mainloop()

