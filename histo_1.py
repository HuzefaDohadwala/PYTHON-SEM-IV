import matplotlib.pyplot as plt
import numpy as np
import random

result = random.sample(range(0,100),10)
result_1 = random.sample(range(1,20),10)

plt.hist(result_1)
plt.show()