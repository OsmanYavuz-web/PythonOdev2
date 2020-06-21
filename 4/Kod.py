from math import *

def f(x):
  return tan(x)

def f1(x):
  return 1/cos(x)**2

x=1.0
h=0.1
for i in range(3):
    f1_simetrik=(f(x+h)-f(x-h))/(2*h)
    print("%.14f" %h,"%.10f" %f1_simetrik)
    h=h/10.0