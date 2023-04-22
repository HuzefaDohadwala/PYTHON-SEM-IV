import matplotlib.pyplot as plt
import numpy as np

X=np.array([10,20,30,10,20])
A=['A','B','C','D','E']
plt.pie(X,labels=A)
plt.legend(title='legend')
plt.show()