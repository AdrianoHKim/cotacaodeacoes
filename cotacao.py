from pandas_datareader import data as web  # import data as web : 'nickname' for data
# import pandas as pd (to read xlsx files)
import matplotlib.pyplot as plt


# date format(MM/DD/YYYY)
cotacao_petr4 = web.DataReader('PETR4.SA', data_source='yahoo', start="01/01/2020", end="01/01/2021")

print(cotacao_petr4)

cotacao_petr4["Close"].plot(figsize=(15, 10))  # ["xxxx"] chose the column to display on graph
plt.show()
