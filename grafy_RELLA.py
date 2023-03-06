"""
import pylab as pl
from pylab import pi

f = 50
t = pl.linspace(0,0.05,444)
u = 3.3 * pl.cos(2 * pi * f * t)
i = 2.2 * pl.cos(2 * pi * f * t)

pl.plot(t, u, "g:",label="napětí")
pl.plot(t, i, "b-.,",label="proud")
pl.plot(t, u * i, "r--",label="výkon")

pl.grid(1)
pl.title("Výkon střídavého proudu")
pl.xlabel("t [s]")
pl.ylabel("u(t),i(t),p(t)")
pl.legend()


pl.show()

"""

"""
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk





def __init__(self, master-None,cnf-{}, **kw):
    super().__init__(master, cnf, **kw)

    if not"textvariable" in kw:
        self.variable = tk.StringVar()
        self.config(textvariable=self.variable)
    else:
        self.variable = kw["textvariable"]

@property
def value():
    return self.variable.get()

@value.setter
def value(self, new: str):
    self.variable.set(new)

"""

import scipy.interpolate as inp
import pylab as lab

#x= [0, 0.3, 0.5, 0.8, 1,  2,  3 ]
#y= [0, 0.1, 0.5, 1,   3, 10, 30]

x= "0 0.3 0.5 0.8 1  2  3".split()
y= "0 0.1 0.5 1   3 10 30".split()

x = list(map(float, x))
y = list(map(float, y))

spl = inp.CubicSpline(x,y)
newX = lab.linspace (0,3,2000)
newY = spl(newX)
lab.plot(newX,newY,"-")
lab.plot(x,y,"o",color = "red")
lab.show()



