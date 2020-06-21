import sympy as sp
sp.init_printing()

def f(deger):
  x = sp.Symbol('x')
  f = sp.Function('f')
  f = x**2-x-3
  sonuc = f.subs(x, deger)
  print("Sonuç: ", sonuc)

f(1)