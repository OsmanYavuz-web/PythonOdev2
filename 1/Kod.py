from numpy import *

def trapez (f, a, b, dx):
  n = int((b-a)/dx) 
  s=0.5*(f(a)+f(b))
  for i in range(1,n):
      x=a+i*dx
      s=s+f(x)
  return dx*s

def simpson (f, a, b, dx):
  n = int((b-a)/dx)
  s=f(a)+f(b)
  for i in range(1,n):
    katsayi=2*(i%2+1)
    x=a+i*dx
    s=s+katsayi*f(x)
  return dx*s/3

def f(x):
  return x**2+5*x+1

def Sanal(x):
  return x**3/3+5*x*2/2+x

a=0.0
b=3
dx=0.01

for i in range(16):
  int_trapz = trapez (f, a, b, dx)
  int_simp = simpson (f, a, b, dx)
  int_tam = Sanal(b)-Sanal(a)
  trapz_hata = abs(int_trapz-int_tam)
  simp_hata = abs(int_simp-int_tam)

print("DX: %.16f" % dx, "TRAPEZ: %.6f" % trapz_hata,"SIMPSON: %.6f" % simp_hata )