""""""  		  	   		  		 			  		 			     			  	 
"""  		  	   		  		 			  		 			     			  	 
Template for implementing StrategyLearner  (c) 2016 Tucker Balch  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  		 			  		 			     			  	 
Atlanta, Georgia 30332  		  	   		  		 			  		 			     			  	 
All Rights Reserved  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
Template code for CS 4646/7646  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  		 			  		 			     			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		  		 			  		 			     			  	 
and other users of this template code are advised not to share it with others  		  	   		  		 			  		 			     			  	 
or to make it available on publicly viewable websites including repositories  		  	   		  		 			  		 			     			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		  		 			  		 			     			  	 
or edited.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
We do grant permission to share solutions privately with non-students such  		  	   		  		 			  		 			     			  	 
as potential employers. However, sharing with other current or future  		  	   		  		 			  		 			     			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  		 			  		 			     			  	 
GT honor code violation.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
-----do not edit anything above this line---  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
Student Name: Tucker Balch (replace with your name)  		  	   		  		 			  		 			     			  	 
GT User ID: tb34 (replace with your User ID)  		  	   		  		 			  		 			     			  	 
GT ID: 900897987 (replace with your GT ID)  		  	   		  		 			  		 			     			  	 
"""  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
import datetime as dt
from datetime import timedelta  	   		  		 			  		 			     			  	 
import random  		  	   		  		 			  		 			     			  	 		  	   		  		 			  		 			     			  	 
import pandas as pd  		  	   		  		 			  		 			     			  	 
from util import get_data
import indicators as idn
import matplotlib.pyplot as plt
	   		  		 			  		 			     			  	 
	   		  		 			  		 			     			 		  	   		  		 			  		 			     			  	 
	  	   		  		 			  		 			     			  	 		  	   		  		 			  		 			     			  	
def author(): 
  return 'srasool7' # replace tb34 with your Georgia Tech username.

	
                                                                                                                                 
# this method should use the existing policy and test it against new data  		  	   		  		 			  		 			     			  	 
def testPolicy(  		  	   		  		 			  		 			     			  	 	  	   		  		 			  		 			     			  	 
    symbol="IBM",  		  	   		  		 			  		 			     			  	 
    sd=dt.datetime(2009, 1, 1),  		  	   		  		 			  		 			     			  	 
    ed=dt.datetime(2010, 1, 1),  		  	   		  		 			  		 			     			  	 
    sv=10000,  		  	   		  		 			  		 			     			  	 
):  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    Tests your learner using data outside of the training data  		  	   		  		 			  		 			     			  	 
                                                                                
    :param symbol: The stock symbol that you trained on on  		  	   		  		 			  		 			     			  	 
    :type symbol: str  		  	   		  		 			  		 			     			  	 
    :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		  		 			  		 			     			  	 
    :type sd: datetime  		  	   		  		 			  		 			     			  	 
    :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		  		 			  		 			     			  	 
    :type ed: datetime  		  	   		  		 			  		 			     			  	 
    :param sv: The starting value of the portfolio  		  	   		  		 			  		 			     			  	 
    :type sv: int  		  	   		  		 			  		 			     			  	 
    :return: A DataFrame with values representing trades for each day. Legal values are +1000.0 indicating  		  	   		  		 			  		 			     			  	 
        a BUY of 1000 shares, -1000.0 indicating a SELL of 1000 shares, and 0.0 indicating NOTHING.  		  	   		  		 			  		 			     			  	 
        Values of +2000 and -2000 for trades are also legal when switching from long to short or short to  		  	   		  		 			  		 			     			  	 
        long so long as net holdings are constrained to -1000, 0, and 1000.  		  	   		  		 			  		 			     			  	 
    :rtype: pandas.DataFrame  		  	   		  		 			  		 			     			  	 
    """

    sd_b = sd - timedelta(days = 365)
    dates = pd.date_range(dt.datetime.strftime(sd_b, '%Y-%m-%d'), dt.datetime.strftime(ed, '%Y-%m-%d'))
    stk_data = get_data([symbol], dates)
    stk_data = stk_data.dropna(axis=0)
    stk_data_2 = get_data([symbol], pd.date_range(dt.datetime.strftime(sd, '%Y-%m-%d'), dt.datetime.strftime(ed, '%Y-%m-%d')))
    stk_data_2 = stk_data_2.dropna(axis=0)

    skt_data_copy = stk_data.copy()
    golden_death_cross = idn.golden_death_cross(stock_data = skt_data_copy, symbol=symbol)
    
    skt_data_copy = stk_data.copy()
    rsi = idn.rsi(stock_data = skt_data_copy, symbol=symbol, period=14)
    skt_data_copy = stk_data.copy()
    ema = idn.ema_crossover(stock_data = skt_data_copy, symbol=symbol)
    skt_data_copy = stk_data.copy()
    momentum = idn.momentum(stock_data = skt_data_copy, symbol=symbol, days=5)
    skt_data_copy = stk_data.copy()
    bbpt = idn.bb_pct(stock_data = skt_data_copy,symbol=symbol,days = 20)

    # combining df
    indicator_dataframe = golden_death_cross[[symbol,'golden_death_ratio']]
    rsi_df = rsi[['rsi','rsi_signal']]
    indicator_dataframe = indicator_dataframe.join(rsi_df)
    ema_df = ema[['ema_ratio', 'ema_crossover_signal']]
    indicator_dataframe = indicator_dataframe.join(ema_df)
    momentum_df = momentum[['momentum', 'momentum_signal']]
    indicator_dataframe = indicator_dataframe.join(momentum_df)
    bbpt_df = bbpt[['Bollinger_bands_%']]
    indicator_dataframe = indicator_dataframe.join(bbpt_df)
    indicator_dataframe = indicator_dataframe[indicator_dataframe.index >= sd]
    indicator_dataframe[symbol] = indicator_dataframe.loc[:,symbol]/indicator_dataframe.loc[indicator_dataframe.index[0],symbol]
    indicator_dataframe['momentum'] = indicator_dataframe.loc[:,'momentum']/indicator_dataframe.loc[indicator_dataframe.index[0],'momentum']
    indicator_dataframe['rsi'] = indicator_dataframe.loc[:,'rsi']/indicator_dataframe.loc[indicator_dataframe.index[0],'rsi']
    indicator_dataframe['golden_death_ratio'] = indicator_dataframe.loc[:,'golden_death_ratio']/indicator_dataframe.loc[indicator_dataframe.index[0],'golden_death_ratio']
    indicator_dataframe['ema_ratio'] = indicator_dataframe.loc[:,'ema_ratio']/indicator_dataframe.loc[indicator_dataframe.index[0],'ema_ratio']
    #indicator_dataframe['Bollinger_bands_%'] = indicator_dataframe.loc[:,'Bollinger_bands_%']/indicator_dataframe.loc[indicator_dataframe.index[0],'Bollinger_bands_%']

    # manual_rules

    # 1) Bollinger_bands_% >= 1  = over bought / sell , <= 0 oversold = buy
    # 2) ema ratio >= 1 , overbought sell, < 1 Sell
    # 3) momentum > 100 buy , sell momentum < 100

    #buy_df = indicator_dataframe[(indicator_dataframe['Bollinger_bands_%'] >= 1) & (indicator_dataframe['ema_ratio'] >= 1) & (indicator_dataframe['momentum'] >= 100)]
    #sell_df = indicator_dataframe[(indicator_dataframe['Bollinger_bands_%'] <= 0) & (indicator_dataframe['ema_ratio'] < 1) & (indicator_dataframe['momentum'] <= 100)]
    
    order_df = pd.DataFrame(columns = ['Order','Shares'], index = stk_data.index)
    #order_df_2 = pd.DataFrame(columns = ['order','shares'], index = pd.date_range(dt.datetime.strftime(sd, '%Y-%m-%d'), dt.datetime.strftime(ed, '%Y-%m-%d')))
    buy_stock = True
    sell_stock = False
    for rows_num in range(1,indicator_dataframe.shape[0]):
        curr_bollinger_band_pct = indicator_dataframe.loc[indicator_dataframe.index[rows_num],'Bollinger_bands_%']
        curr_momentum = indicator_dataframe.loc[indicator_dataframe.index[rows_num],'momentum']
        yesterday_ema = indicator_dataframe.loc[indicator_dataframe.index[rows_num - 1],'ema_ratio']
        curr_ema = indicator_dataframe.loc[indicator_dataframe.index[rows_num],'ema_ratio']
        ema_diff = curr_ema - yesterday_ema
        # print('--------------------------')
        # print(f'date: {indicator_dataframe.index[rows_num]}')
        # print(f'curr_momentum: {curr_momentum}')
        # print(f'curr_ema: {curr_ema}')
        # print(f'ema_diff: {ema_diff}')
        # print(f'curr_bollinger_band_pct: {curr_bollinger_band_pct}')
        # print('--------------------------')

        if curr_bollinger_band_pct < 0.0 and curr_momentum < 1 and ema_diff < 0 and curr_ema < 0.98 and buy_stock:
            order_df.loc[indicator_dataframe.index[rows_num],'Order'] = 'BUY'
            order_df.loc[indicator_dataframe.index[rows_num],'Shares'] = 1000
            #order_df_2.loc[indicator_dataframe.index[rows_num],'order'] = 1
            #order_df_2.loc[indicator_dataframe.index[rows_num],'shares'] = 1000
            buy_stock = False
            sell_stock = True
        
        if curr_bollinger_band_pct > 1.01  and curr_momentum >= 1.02 and ema_diff >= 0 and curr_ema >= 1.02 and sell_stock:
            order_df.loc[indicator_dataframe.index[rows_num],'Order'] = 'SELL'
            order_df.loc[indicator_dataframe.index[rows_num],'Shares'] = -1000
            #order_df_2.loc[indicator_dataframe.index[rows_num],'order'] = -1
            #order_df_2.loc[indicator_dataframe.index[rows_num],'shares'] = 1000
            sell_stock = False
            buy_stock = True

    #order_df = order_df.dropna()

    if order_df.index[-1] != ed:
        if sell_stock:
            order_df.loc[stk_data.index[-1],'Order'] = 'SELL'
            order_df.loc[stk_data.index[-1],'Shares'] = -1000
        else:
            order_df.loc[stk_data.index[-1],'Order'] = 'OUT'
            order_df.loc[stk_data.index[-1],'Shares'] = 0
        
    if order_df.index[0] != sd:
        order_df.loc[stk_data_2.index[1],'Order'] = 'OUT'
        order_df.loc[stk_data_2.index[1],'Shares'] = 0


    order_df['Symbol'] = symbol
    order_df.fillna(0, inplace=True)
    order_df = order_df[order_df.index >= sd]
    order_df = pd.DataFrame(order_df['Shares'])



    # plt.plot(indicator_dataframe['JPM'], color='red',label = 'JPM')
    # plt.plot(indicator_dataframe['Bollinger_bands_%'], color='purple',label = 'Bollinger_bands_%')
    # plt.plot(indicator_dataframe['ema_ratio'], color='black',label = 'ema_ratio')
    # plt.plot(indicator_dataframe['momentum'], color='orange',label = 'momentum')
    # plt.vlines(order_df[order_df['Order']=='BUY'].index,ymin = -0.25,  ymax = 1.5, color='blue',label = 'LONG', linestyle='solid')
    # plt.vlines(order_df[order_df['Order']=='SELL'].index,ymin = -0.25,  ymax = 1.5, color='green',label = 'SHORT', linestyle='solid')
    # plt.grid()
    # plt.title('Insample - JPM')
    # plt.xlabel('Period')
    # plt.ylabel('Normalized Returns')
    # plt.xticks()
    # plt.xticks(fontsize = 8)
    # plt.yticks(fontsize = 8)
    # plt.legend(loc = "lower left")
    # #plt.savefig('./images/'+'Insample_JPM'+'.png')
    # #plt.cla()
    # plt.show()

    
    return order_df
  		  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    print("One does not simply think up a strategy")  		  	   		  		 			  		 			     			  	 
