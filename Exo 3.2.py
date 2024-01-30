#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:37:44 2024

@author: jovana
"""

import pandas as pd
import numpy as np
import yfinance as yf

# Download 10-year treasyry Futures Data
sp500_futures = yf.download('ES=F')['Adj Close']

# Calculate daily Logarithmic Returns
sp500_futures['Log Returns'] = np.log(sp500_futures / sp500_futures.shift(1))

# Annualized Returns and Volatility
annualized_return = sp500_futures['Log Returns'].mean() * 252
annualized_volatility = sp500_futures['Log Returns'].std() * np.sqrt(252)

# Download the 3-month Treasury bill rate as the risk-free rate
SP500_start_date = str(sp500_futures.index[0])[:10]
risk_free_rate_series = yf.download('^IRX', start=SP500_start_date)['Adj Close']
risk_free_rate = risk_free_rate_series.mean() / 100

sp500_futures.head()
risk_free_rate_series.head()

# Calculate Sharpe Ratio
sharpe_ratio = (annualized_return - risk_free_rate) / annualized_volatility

# Print results

print("Annualized Return :", round(annualized_return, 3))
print("Annualized Volatility :", round(annualized_volatility, 3))
print("Risk Free Annual Rate :", round(risk_free_rate, 3))
print("Sharpe Ratio :", round(sharpe_ratio, 3))
