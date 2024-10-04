import pandas as pd
import matplotlib.pyplot as plt

fifa = pd.read_csv('./fifa_data.csv')

bins = [40,50,60,70,80,90,100]
plt.figure(figsize=(8,5))

plt.hist(fifa.Overall, bins=bins, color='#abcdfe')

plt.xticks(bins)