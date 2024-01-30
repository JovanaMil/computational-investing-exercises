#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:35:15 2024

@author: jovana
"""

import pandas as pd
import numpy as np
import yfinance as yf

# Download 10-year treasyry Futures Data
treasury_future = yf.download('ZN=F')['Adj Close']

# Calculate daily Logarithmic Returns
treasury_future['Log Returns'] = np.log(treasury_future / treasury_future.shift(1))

# Annualized Returns and Volatility
annualized_return = treasury_future['Log Returns'].mean() * 252
annualized_volatility = treasury_future['Log Returns'].std() * np.sqrt(252)

# Download the 3-month Treasury bill rate as the risk-free rate
treasury_start_date = str(treasury_future.index[0])[:10]
risk_free_rate_series = yf.download('^IRX', start=treasury_start_date)['Adj Close']
risk_free_rate = risk_free_rate_series.mean() / 100

# Calculate Sharpe Ratio
sharpe_ratio = (annualized_return - risk_free_rate) / annualized_volatility

# Print results

print("Annualized Return :", round(annualized_return, 3))
print("Annualized Volatility :", round(annualized_volatility, 3))
print("Risk Free Annual Rate :", round(risk_free_rate, 3))
print("Sharpe Ratio :", round(sharpe_ratio, 3))
 
# Interpretation : 
