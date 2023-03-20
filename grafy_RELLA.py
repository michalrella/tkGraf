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

"""

#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import pylab as pl
import os.path

# from tkinter import ttk


class MyEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        if not "textvariable" in kw:
            self.variable = tk.StringVar()
            self.config(textvariable=self.variable)
        else:
            self.variable = kw["textvariable"]

    @property
    def value(self):
        return self.variable.get()

    @value.setter
    def value(self, new: str):
        self.variable.set(new)


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Foo"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="tkGraf")
        self.lbl.pack()

        self.fileFrame = tk.LabelFrame(self, text="Soubor")
        self.fileFrame.pack(padx=5, pady=5, fill="x")
        self.fileEntry = MyEntry(self.fileFrame)
        self.fileEntry.pack(anchor="w", fill="x")
        self.fileBtn = tk.Button(self.fileFrame, text="...", command=self.selectFile)
        self.fileBtn.pack(anchor="e")

        self.dataformatVar = tk.StringVar(value="ROW")
        self.rowRadio = tk.Radiobutton(
            self.fileFrame,
            text="Dada v řádcích",
            variable=self.dataformatVar,
            value="ROW",
        )
        self.rowRadio.pack(anchor="w")
        self.columnRadio = tk.Radiobutton(
            self.fileFrame,
            text="Data ve sloupcích",
            variable=self.dataformatVar,
            value="COLUMN",
        )
        self.columnRadio.pack(anchor="w")

        self.grafFrame = tk.LabelFrame(self, text="Graf")
        self.grafFrame.pack(padx=5, pady=5, anchor="w", fill="x")

        tk.Label(self.grafFrame, text="Titulek").grid(row=0, column=0)
        self.titleEntry = MyEntry(self.grafFrame)
        self.titleEntry.grid(row=0, column=1, sticky=tk.EW)
        tk.Label(self.grafFrame, text="osa X").grid(row=1, column=0)
        self.xEntry = MyEntry(self.grafFrame)
        self.xEntry.grid(row=1, column=1, columnspan=2, sticky=tk.EW)
        tk.Label(self.grafFrame, text="osa Y").grid(row=2, column=0)
        self.yEntry = MyEntry(self.grafFrame)
        self.yEntry.grid(row=2, column=1, sticky=tk.EW)

        tk.Label(self.grafFrame, text="mřížka").grid(row=3, column=0)
        self.gridVar = tk.BooleanVar(value=True)
        self.gridCheck = tk.Checkbutton(self.grafFrame, variable=self.gridVar)
        self.gridCheck.grid(row=3, column=1, sticky="w")

        self.lineVar = tk.StringVar(value="none")
        tk.Label(self.grafFrame, text="čára").grid(row=4, column=0)
        tk.OptionMenu(self.grafFrame, self.lineVar, "none", "-", "--", "-.", ":").grid(
            row=4, column=1, sticky="w"
        )

        self.markerVar = tk.StringVar(value="none")
        tk.Label(self.grafFrame, text="marker").grid(row=5, column=0)
        tk.OptionMenu(
            self.grafFrame, self.markerVar, "none", *tuple("xX+P,.o*1234")
        ).grid(row=5, column=1, sticky="w")

        tk.Button(self, text="Vykreslit", command=self.plot).pack(anchor="w")

        tk.Button(self, text="Quit", command=self.quit).pack(anchor="e")

    def selectFile(self):
        self.fileEntry.value = filedialog.askopenfilename()

    def plot(self):
        if not os.path.isfile(self.fileEntry.value):
            return
        with open(self.fileEntry.value, "r") as f:
            if self.dataformatVar.get() == "ROW":
                x = f.readline().split(";")
                y = f.readline().split(";")
                x = [float(i.replace(",", ".")) for i in x]
                y = [float(i.replace(",", ".")) for i in y]
            elif self.dataformatVar.get() == "COLUMN":
                x = []
                y = []
                while True:
                    line = f.readline()
                    if line == "":
                        break
                    if ";" not in line:
                        continue
                    x1, y1 = line.split(";")
                    x.append(float(x1.replace(",", ".")))
                    y.append(float(y1.replace(",", ".")))

        pl.plot(x, y, linestyle=self.lineVar.get(), marker=self.markerVar.get())
        pl.title(self.titleEntry.value)
        pl.xlabel(self.xEntry.value)
        pl.ylabel(self.yEntry.value)
        pl.grid(self.gridVar.get())
        pl.show()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
