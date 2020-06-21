import matplotlib.pyplot as plt

x=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
y=[27,17,9,3,1,0,1,3,9,17,27]

plt.plot(x, y, color = "b" )
plt.title("$y=x^2-x-3$ Grafiği")
plt.xlabel("x ekseni")
plt.ylabel("y ekseni")
plt.show()