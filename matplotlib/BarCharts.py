import matplotlib.pyplot as plt

labels = ['A','B','C','D','E']
values = [3,6,9,12,15]

bars = plt.bar(labels,values)
bars[0].set_hatch('/')
bars[1].set_hatch('o')
bars[2].set_hatch('*')
bars[3].set_hatch('o')
bars[4].set_hatch('/')

plt.show()