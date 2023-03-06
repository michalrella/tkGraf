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
