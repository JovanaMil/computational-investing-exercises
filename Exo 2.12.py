#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 17:28:21 2024

@author: jovana
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

sp500 = yf.download("ES=F")
treasuries = yf.download("ZN=F")

prices_sp500 = sp500["Adj Close"]
prices_treasuries = treasuries["Adj Close"]
sp500["log_returns"] = np.log(prices_sp500).diff()
treasuries["log_returns"] = np.log(prices_treasuries).diff()

cumulative_returns_sp500 = np.exp(sp500["log_returns"].cumsum()) - 1  #we do -1 do get the percentage
cumulative_returns_treasuries = np.exp(treasuries["log_returns"].cumsum()) - 1

#cumulative_max = cumulative_returns_sp500.cummax()
#drawdowns = (cumulative_max - cumulative_returns_sp500)

portfolio_returns = sp500["log_returns"] * 0.6 + treasuries["log_returns"] * 0.4
portfolio_cumulative_returns = np.exp(portfolio_returns.cumsum()) - 1

plt.plot(cumulative_returns_sp500, label = 'SP500')
plt.plot(cumulative_returns_treasuries, label = 'Treasuries')
plt.plot(portfolio_cumulative_returns, label = 'Portfolio')
#plt.plot(cumulative_max, label = "cumulative_max")
#plt.fill_between(drawdowns.index, drawdowns, color = "red", alpha= 0.3)
plt.legend()
plt.show()

#print(f"Maximum Drawdown: {round((drawdowns.max()),4)}")



# max_drawdown = (sp500['cumulative_returns'].cummax() - sp500['cumulative_returns']).max()