import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

labels = ['A','B','C']
values = [3,6,9]

bars = plt.bar(labels,values)
bars[0].set_hatch('/')
bars[1].set_hatch('o')
bars[2].set_hatch('*')

plt.show()