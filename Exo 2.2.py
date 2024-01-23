#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:03:22 2024

@author: jovana
"""

# Import libraries
import pandas as pd 
import numpy as np
import yfinance as yf

# Use the ‘yfinance‘ library to download the front month S &P500 futures price data.
sp500_futures = yf.download('ES=F')

# Calculate the daily logarithmic returns of the futures prices.
sp500_futures['Log_Returns'] = np.log(sp500_futures['Adj Close'] / sp500_futures['Adj Close'].shift(1))

# Annualize the mean of the logarithmic returns.
annualized_return = sp500_futures['Log_Returns'].mean() * 252
print("annualized_return:", annualized_return)

