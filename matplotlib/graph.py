import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [0,1,2,3,4]
y = [0,2,4,6,8]

plt.plot(x,y, label='2x', color='blue', linewidth=2, linestyle='--', marker='.', markersize=10)

x2 = np.arange(0,4.5,.5)
plt.plot(x2[:6], x2[:6]**2, 'r', label='x^2')
plt.plot(x2[5:], x2[5:]**2, 'r--')

plt.title('Our First Graph!', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.xticks([0,1,2,3,4,])
plt.yticks([0,2,4,6,8,10])

plt.legend()
plt.show()