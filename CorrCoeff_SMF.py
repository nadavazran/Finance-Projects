#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 17:33:45 2024

@author: nadavazran
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import seaborn
import yfinance as yf

tickers = ['SPY', 'LULU', 'GD', 'DVN', 'BSX', 'WMT', 'FCX', 'PANW',]

# Define the date range (5 years ending on September 28, 2024)
start_date = "2019-09-28"
end_date = "2024-09-28"

# Loop through each ticker to download data and calculate percentage change
for ticker in tickers:
    # Download the stock data
    data = yf.download(ticker, start=start_date, end=end_date)

    # Calculate percentage change
    data['pct'] = data['Adj Close'].pct_change()

    # Save data to CSV
    csv_file = f'{ticker}.csv'
    data.to_csv(csv_file)
    print(f'{ticker} data saved to {csv_file}')

#  Calculate daily percent change
SPY  = pd.read_csv('SPY.csv');  SPY['pct'] = SPY['Adj Close'].pct_change()
LULU  = pd.read_csv('LULU.csv');  LULU['pct'] = LULU['Adj Close'].pct_change()
GD  = pd.read_csv('GD.csv');  GD['pct'] = GD['Adj Close'].pct_change()
DVN  = pd.read_csv('DVN.csv');  DVN['pct'] = DVN['Adj Close'].pct_change()
BSX  = pd.read_csv('BSX.csv');  BSX['pct'] = BSX['Adj Close'].pct_change()
WMT = pd.read_csv('WMT.csv');  WMT['pct'] = WMT['Adj Close'].pct_change()
FCX = pd.read_csv('FCX.csv');  FCX['pct'] = FCX['Adj Close'].pct_change()
PANW = pd.read_csv('PANW.csv');  PANW['pct'] = PANW['Adj Close'].pct_change()


#  Extract percent change to numpy vectors and delete first entry (nan)
spy  = SPY['pct'].to_numpy(); spy = np.delete(spy, 0)
lulu  = LULU['pct'].to_numpy(); lulu = np.delete(lulu, 0)
gd  = GD['pct'].to_numpy(); gd = np.delete(gd, 0)
dvn  = DVN['pct'].to_numpy(); dvn = np.delete(dvn, 0)
bsx  = BSX['pct'].to_numpy(); bsx = np.delete(bsx, 0)
wmt = WMT['pct'].to_numpy(); wmt = np.delete(wmt, 0)
fcx  = FCX['pct'].to_numpy(); fcx = np.delete(fcx, 0)
panw  = PANW['pct'].to_numpy(); panw = np.delete(panw, 0)


# LULU correlation with SPY
plt.plot(spy, lulu, '.')
plt.grid(True)
plt.xlabel('SPY % Change')
plt.ylabel('LULU % change')

#  Do linear regression calculating the slope (beta) and correlation (stored in r_value)
slope, intercept, r_value, p_value, std_err =  linregress(spy, lulu)

#  Plot regression line
x = np.linspace(-.1, .1)
plt.plot(x, slope * x + intercept, 'k')

#  Print beta and correlation
print('beta = ', slope)
print('Corr = ', r_value)
print('R Squared = ', r_value**2)

#  Plot raw GD Data
plt.plot(spy, gd, '.')
plt.grid(True)
plt.xlabel('SPY % Change')
plt.ylabel('GD % change')

#  Do linear regression calculating the slope (beta) and correlation (stored in r_value)
slope, intercept, r_value, p_value, std_err =  linregress(spy, gd)

#  Plot regression line
x = np.linspace(-.1, .1)
plt.plot(x, slope * x + intercept, 'k')

#  Print beta and correlation
print('beta = ', slope)
print('Corr = ', r_value)
print('R Squared = ', r_value**2)

#  Plot raw DVN Data
plt.plot(spy, dvn, '.')
plt.grid(True)
plt.xlabel('SPY % Change')
plt.ylabel('DVN % change')

#  Do linear regression calculating the slope (beta) and correlation (stored in r_value)
slope, intercept, r_value, p_value, std_err =  linregress(spy, dvn)

#  Plot regression line
x = np.linspace(-.1, .1)
plt.plot(x, slope * x + intercept, 'k')

#  Print beta and correlation
print('beta = ', slope)
print('Corr = ', r_value)
print('R Squared = ', r_value**2)

#  Plot raw BSX Data
plt.plot(spy, bsx, '.')
plt.grid(True)
plt.xlabel('SPY % Change')
plt.ylabel('BSX % change')

#  Do linear regression calculating the slope (beta) and correlation (stored in r_value)
slope, intercept, r_value, p_value, std_err =  linregress(spy, bsx)

#  Plot regression line
x = np.linspace(-.1, .1)
plt.plot(x, slope * x + intercept, 'k')

#  Print beta and correlation
print('beta = ', slope)
print('Corr = ', r_value)
print('R Squared = ', r_value**2)

#  Plot raw FIDU Data
plt.plot(spy, wmt, '.')
plt.grid(True)
plt.xlabel('SPY % Change')
plt.ylabel('WMT % change')

#  Do linear regression calculating the slope (beta) and correlation (stored in r_value)
slope, intercept, r_value, p_value, std_err =  linregress(spy, wmt)

#  Plot regression line
x = np.linspace(-.1, .1)
plt.plot(x, slope * x + intercept, 'k')

#  Print beta and correlation
print('beta = ', slope)
print('Corr = ', r_value)
print('R Squared = ', r_value**2)

#  Plot raw GLD Data
plt.plot(spy, fcx, '.')
plt.grid(True)
plt.xlabel('SPY % Change')
plt.ylabel('FCX % change')

#  Do linear regression calculating the slope (beta) and correlation (stored in r_value)
slope, intercept, r_value, p_value, std_err =  linregress(spy, fcx)

#  Plot regression line
x = np.linspace(-.1, .1)
plt.plot(x, slope * x + intercept, 'k')

#  Print beta and correlation
print('beta = ', slope)
print('Corr = ', r_value)
print('R Squared = ', r_value**2)

#  Plot raw GOOG Data
plt.plot(spy, panw, '.')
plt.grid(True)
plt.xlabel('SPY % Change')
plt.ylabel('PANW % change')

#  Do linear regression calculating the slope (beta) and correlation (stored in r_value)
slope, intercept, r_value, p_value, std_err =  linregress(spy, panw)

#  Plot regression line
x = np.linspace(-.1, .1)
plt.plot(x, slope * x + intercept, 'k')

#  Print beta and correlation
print('beta = ', slope)
print('Corr = ', r_value)
print('R Squared = ', r_value**2)

#  Plot regression line
x = np.linspace(-.1, .1)
plt.plot(x, slope * x + intercept, 'k')

#  Print beta and correlation
print('beta = ', slope)
print('Corr = ', r_value)
print('R Squared = ', r_value**2)

#  Create a data frame made of our percent changes for each underlying
data = [SPY['pct'], LULU['pct'], GD['pct'], DVN['pct'], BSX['pct'], WMT['pct'],  FCX['pct'], PANW['pct']]
headers = ['SPY', 'LULU', 'GD', 'DVN', 'BSX', 'WMT', 'FCX', 'PANW', 'AAPL']
pct_frame = pd.concat(data, axis=1, keys=headers)
plt.show()

#  Use the built in pandas function to calculate correlation
corr_frame = pct_frame.corr()
corr_frame

#  Create a mask to hide upper part of the correlation matrix
mask = np.triu(np.ones_like(corr_frame, dtype=bool))

#  Create heat map
seaborn.heatmap(corr_frame, cmap='rocket_r',annot=True)
plt.show()