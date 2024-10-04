import pandas as pd
import matplotlib.pyplot as plt

gas = pd.read_csv('gas_proces.csv')

plt.figure(figsize=(8,5))

plt.title('Gas Prices over Time (in USD)', fontdict={'fontweight':'bold', 'fontsize': 18})