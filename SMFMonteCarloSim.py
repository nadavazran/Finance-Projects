#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 12:34:03 2024

@author: nadavazran
"""

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.ticker as mticker

def get_data(stocks, start, end):
    stockData = yf.download(stocks, start, end)
    stockData = stockData['Close']
    returns = stockData.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns, covMatrix

stockList = ['SPY', 'LULU', 'GD', 'DVN', 'BSX', 'WMT', 'FCX', 'PANW', 'AAPL']
stocks = stockList
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=300)
meanReturns, covMatrix = get_data(stocks, startDate, endDate)
print(meanReturns)

weights = np.array([.7143, .0211, .029, .0184, .0488, .0583, .0312, .0384, .0405])
if np.sum(weights) != 1:
    raise ValueError ("The sum of the weights must equal 1!")

print(weights)

#Monte Carlo Sim
smf_sims = 100
T = 3652

meanM = np.full(shape=(T, len(weights)), fill_value=meanReturns)
meanM = meanM.T

portfolio_sims = np.full(shape=(T, smf_sims), fill_value=0.0)

initialSMFPortfolio = 562163.98

for m in range (0,smf_sims):
    Z = np.random.normal(size=(T, len(weights)))
    L = np.linalg.cholesky(covMatrix)
    dailyReturns = meanM + np.inner(L, Z)
    portfolio_sims[:,m] = np.cumprod(np.inner(weights, dailyReturns.T)+1)*initialSMFPortfolio
    plt.plot(portfolio_sims)
    plt.ylabel('Portfolio value ($')
    plt.xlabel('Days')
    plt.title('Monte Carlo Sim of SMF Portfolio')
    
    def dollar_formatter(x,pos):
        return f'${int(x):,}'
    plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(dollar_formatter))
    plt.show()
    
    #Value at Risk and Conditional Value at Risk of SMF Portfolio
    def mcVaR(returns, alpha=5):
        """ Input: pandas series of returns
            Output: percentile on return distribution to a given confidence level alpha
        """
        if isinstance(returns, pd.Series):
            return np.percentile(returns, alpha)
        else:
            raise TypeError("Expected a pandas data series")
            
    def mcCVaR(returns, alpha=5):
        """ Input: pandas series of returns
            Output: CVaR or Expected shortfall to a given confidence level alpha
        """
        if isinstance(returns, pd.Series):
            belowVaR = returns <= mcVaR(returns, alpha=alpha)
            return returns[belowVaR].mean()
        else:
            raise TypeError("Expected a pandas data series")
    
    portfolioResults = pd.Series(portfolio_sims[-1,:])
    
    VaR = initialSMFPortfolio - mcVaR(portfolioResults, alpha=5)
    CVaR = initialSMFPortfolio - mcCVaR(portfolioResults, alpha =5)
    
print('VaR ${}'.format(round(VaR,2)))
print('CVaR ${}'.format(round(CVaR,2)))