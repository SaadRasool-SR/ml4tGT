import pandas as pd
pd.options.display.max_columns = None
pd.options.display.max_rows = None  
import numpy as np

def author(): 
  return 'srasool7' # replace tb34 with your Georgia Tech username.

def golden_death_cross(stock_data,symbol):
    stock_data['50_sma'] = stock_data[symbol].rolling(50).mean()
    stock_data['200_sma'] = stock_data[symbol].rolling(200).mean()
    stock_data['golden_death_ratio'] = stock_data['50_sma']/stock_data['200_sma']
    stock_data = stock_data.dropna(axis = 0)

    for i in range(len(stock_data)-1):
        curr_50_sma_price = stock_data['50_sma'][i]
        curr_200_sma_price = stock_data['200_sma'][i]
        next_50_sma_price = stock_data['50_sma'][i+1]
        next_200_sma_price = stock_data['200_sma'][i+1]

        if curr_50_sma_price < curr_200_sma_price:
            if next_50_sma_price > next_200_sma_price:
                stock_data.loc[stock_data.index[i],'golden_death_cross'] = 'BUY'
            else:
               stock_data.loc[stock_data.index[i],'golden_death_cross'] = 'NO_SIGNAL'
               

        elif curr_50_sma_price > curr_200_sma_price:
            if next_50_sma_price < next_200_sma_price:
                stock_data.loc[stock_data.index[i],'golden_death_cross'] = 'SELL'
            else:
               stock_data.loc[stock_data.index[i],'golden_death_cross'] = 'NO_SIGNAL'
               

    #stock_data['golden_death_cross'] = stock_data['golden_death_cross'].fillna('NO_SIGNAL')
    return stock_data

def rsi(stock_data, symbol, period):
   price_change = stock_data[symbol].diff()
   up_bound = price_change.clip(lower = 0)
   down_bound = price_change.clip(upper=0) * -1
   sma_up = up_bound.rolling(window = period).mean()
   sma_down = down_bound.rolling(window = period).mean()
   rsi = sma_up/ sma_down
   rsi = 100 - (100/(1+rsi))
   stock_data['rsi'] = rsi
   stock_data.loc[stock_data[stock_data['rsi'] > 70].index,'rsi_signal'] = 'SELL'
   stock_data.loc[stock_data[stock_data['rsi'] < 30].index,'rsi_signal'] = 'BUY'
   stock_data['rsi_signal'] = stock_data['rsi_signal'].fillna('NO_SIGNAL')
   return stock_data
   

def ema_crossover(stock_data,symbol):
  stock_data['ema_12'] = stock_data[symbol].ewm(span = 12, adjust = False).mean()
  stock_data['ema_26'] = stock_data[symbol].ewm(span = 26, adjust = False).mean()

  stock_data['ema_ratio'] = stock_data['ema_12'] / stock_data['ema_26']
  stock_data = stock_data.dropna(axis = 0)
  for i in range(len(stock_data)-1):
    curr_12_ema_price = stock_data['ema_12'][i]
    curr_26_ema_price = stock_data['ema_26'][i]
    next_12_ema_price = stock_data['ema_12'][i+1]
    next_26_ema_price = stock_data['ema_26'][i+1]
    if curr_12_ema_price < curr_26_ema_price:
      if next_12_ema_price > next_26_ema_price:
        stock_data.loc[stock_data.index[i],'ema_crossover_signal'] = 'BUY'

    elif curr_12_ema_price > curr_26_ema_price:
      if next_12_ema_price < next_26_ema_price:
        stock_data.loc[stock_data.index[i],'ema_crossover_signal'] = 'SELL'

  stock_data['ema_crossover_signal'] = stock_data['ema_crossover_signal'].fillna('NO_SIGNAL')

  return stock_data


def momentum(stock_data,symbol,days):
  for i in range(days,stock_data[symbol].shape[0]):
    n_days = i - days
    current_price = stock_data.loc[stock_data.index[i],symbol]
    per_price = stock_data.loc[stock_data.index[n_days],symbol]
    momentum_cal = (current_price / per_price) * 100
    stock_data.loc[stock_data.index[i],'momentum'] = momentum_cal

  for i in range(days,stock_data.shape[0] - 1):
    curr_momentum = stock_data['momentum'][i]
    next_momentum = stock_data['momentum'][i+1]

    if curr_momentum > 100:
       if next_momentum < 100:
          stock_data.loc[stock_data.index[i],'momentum_signal'] = 'SELL'
    elif curr_momentum < 100:
       if next_momentum > 100:
          stock_data.loc[stock_data.index[i],'momentum_signal'] = 'BUY'
  stock_data['momentum_signal'] = stock_data['momentum_signal'].fillna('NO_SIGNAL')
  stock_data = stock_data.dropna(axis = 0)
   
  return stock_data
  

def bb_pct(stock_data,symbol,days=20):

  rolling_mean = stock_data[symbol].rolling(days).mean()
  rolling_std = stock_data[symbol].rolling(days).std()
  upper_band = rolling_mean + rolling_std * 2
  lower_band = rolling_mean - rolling_std * 2
  stock_data['lower_bound'] = lower_band
  stock_data['upper_bound'] = upper_band
  stock_data['rolling_mean'] = rolling_mean
  stock_data['Bollinger_bands_%'] = (stock_data[symbol] - lower_band) / (upper_band - lower_band)
  #stock_data.loc[stock_data[stock_data['Bollinger_bands_%'] <= 0].index,'BB_%_signal'] = 'SELL'
  #stock_data.loc[stock_data[stock_data['Bollinger_bands_%'] >= 1].index,'BB_%_signal'] = 'BUY'
  #stock_data['BB_%_signal'] = stock_data['BB_%_signal'].fillna('NO_SIGNAL')
  stock_data = stock_data.dropna(axis = 0)

  return stock_data
