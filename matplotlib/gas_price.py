import pandas as pd
import matplotlib.pyplot as plt

gas = pd.read_csv('./gas_prices.csv')

plt.figure(figsize=(8,5))

plt.title('Gas Prices over Time (in USD)', fontdict={'fontweight':'bold', 'fontsize': 18})

plt.plot(gas.Year, gas.USA,'b.-', label='USA')
plt.plot(gas.Year, gas.Canada, 'r.-', label='Canada')
plt.plot(gas.Year, gas['South Korea'], 'g.-')
plt.plot(gas.Year, gas.Australia, 'y.-')

plt.xticks(gas.Year[::3].tolist()+[2011])
# 3 year na gap e data batave
# 2011 batave even if e data ma 6 bhi nai....

plt.xlabel('Year')
plt.ylabel('US Dollars')

plt.legend()

plt.savefig('Gas_price_figure.png', dpi=300)
# save img of graph

plt.show()