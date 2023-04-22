import matplotlib.pyplot as plt
A=X=['U','V','W','X','Y']
X=['A','B','C','D','E']
Y=[10,20,30,10,20]
Z=[60,50,40,60,20]

plt.bar(X,Y, align='center')
plt.bar(A,Z,align='center')
plt.legend("legend1")
plt.xlabel("letters")
plt.ylabel("numbers")
plt.title("Bar Chart")

plt.show()