import matplotlib.pyplot as plt
import pandas as pd

data ={
    'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'Attempts': [1, 3, 2, 4, 3]
}
df=pd.DataFrame(data)
df.plot(x='Name',y=['Age','Attempts'],kind='bar')
plt.show()