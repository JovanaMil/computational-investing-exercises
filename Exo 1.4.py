#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 12:04:50 2024

@author: jovana
"""

import numpy as np
import matplotlib.pyplot as plt

# Updated portfolio values
values = np.array([10.0, 12.5, 8.0, 13.5, 7.5, 15.0])

# Calculating arithmetic and logarithmic returns
arithmetic_returns = (values[1:] - values[:-1]) / values[:-1] 
log_returns = np.log(values[1:] / values[:-1])

# Calculating cumulative arithmetic and cumulative logarithmic returns
cumulative_arithmetic_return = np.cumsum(arithmetic_returns)
cumulative_logarithmic_return = np.exp(np.cumsum(log_returns)) - 1

# Plotting returns and cumulative returns
plt.figure(figsize=(8, 8))

# Plotting arithmetic and logarithmic returns
plt.subplot(2, 1, 1)
plt.plot(arithmetic_returns, label='Arithmetic Returns', marker='o')
plt.plot(log_returns, label='Logarithmic Returns', marker='x')
plt.title('Annual Arithmetic vs. Logarithmic Returns') 
plt.xlabel('Year')
plt.ylabel('Returns') 
plt.legend()
plt.grid(True)

# Plotting cumulative arithmetic and logarithmic returns
plt.subplot(2, 1, 2)
plt.plot(cumulative_arithmetic_return, label='Cumulative Arithmetic Returns', marker='o')
plt.plot(cumulative_logarithmic_return, label='Cumulative Logarithmic Returns', marker='x')
plt.title('Cumulative Arithmetic vs. Logarithmic Returns')
plt.xlabel('Year')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

