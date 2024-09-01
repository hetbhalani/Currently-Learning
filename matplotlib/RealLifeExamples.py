import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

gas = pd.read_csv('./gas_prices.csv')

plt.plot(gas.Year, gas.USA, 'b.-', label='USA')
plt.plot(gas.Year, gas.Canada,'.-', label='Canada')
plt.plot(gas.Year, gas.Germany, '.-', label='Germany')
                              #shorthand
                              
plt.xticks(gas.Year[::3])# gap of 3 years

plt.legend()

plt.show()