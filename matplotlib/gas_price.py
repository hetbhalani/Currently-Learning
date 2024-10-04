import pandas as pd
import matplotlib.pyplot as plt

gas = pd.read_csv('gas_proces.csv')

plt.figure(figsize=(8,5))

plt.title('Gas Prices over Time (in USD)', fontdict={'fontweight':'bold', 'fontsize': 18})

plt.plot(gas.Year, gas.USA,'b.-', lable='USA')
plt.plot(gas.Year, gas.Canada, 'r.-', lable='Canada')
plt.plot(gas.Year, gas['South Korea'], 'g.-')
plt.plot(gas.Year, gas.Australia, 'y.-')

