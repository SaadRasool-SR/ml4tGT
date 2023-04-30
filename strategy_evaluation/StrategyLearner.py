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
import random  		  	   		  		 			  		 			     			  	 	  	   		  		 			  		 			     			  	 
import pandas as pd  		  	   		  		 			  		 			     			  	 
import util as ut
import numpy as np
import RTLearner as rt
import BagLearner as bl
import indicators as idn
from datetime import timedelta   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
class StrategyLearner(object):  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    A strategy learner that can learn a trading policy using the same indicators used in ManualStrategy.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		  		 			  		 			     			  	 
        If verbose = False your code should not generate ANY output.  		  	   		  		 			  		 			     			  	 
    :type verbose: bool  		  	   		  		 			  		 			     			  	 
    :param impact: The market impact of each transaction, defaults to 0.0  		  	   		  		 			  		 			     			  	 
    :type impact: float  		  	   		  		 			  		 			     			  	 
    :param commission: The commission amount charged, defaults to 0.0  		  	   		  		 			  		 			     			  	 
    :type commission: float  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    # constructor  		  	   		  		 			  		 			     			  	 
    def __init__(self, verbose=False, impact=0.0, commission=0.0):  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        Constructor method  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        self.verbose = verbose  		  	   		  		 			  		 			     			  	 
        self.impact = impact  		  	   		  		 			  		 			     			  	 
        self.commission = commission
        self.window = 365
        self.lookfoward_period = 7
        self.price_threshold = 0.02  # 1.5%
        self.leaf = 20
        self.bag_size = 20
        self.learner = learner = bl.BagLearner(learner = rt.RTLearner, kwargs = {"leaf_size":self.leaf}, bags = self.bag_size, boost = False, verbose = False)


    def author(self):
        return('srasool7')
  		  	   		  		 			  		 			     			  	 
    # this method should create a QLearner, and train it for trading  		  	   		  		 			  		 			     			  	 
    def add_evidence(  		  	   		  		 			  		 			     			  	 
        self,  		  	   		  		 			  		 			     			  	 
        symbol="IBM",  		  	   		  		 			  		 			     			  	 
        sd=dt.datetime(2008, 1, 1),  		  	   		  		 			  		 			     			  	 
        ed=dt.datetime(2009, 1, 1),  		  	   		  		 			  		 			     			  	 
        sv=10000,  		  	   		  		 			  		 			     			  	 
    ):  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        Trains your strategy learner over a given time frame.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
        :param symbol: The stock symbol to train on  		  	   		  		 			  		 			     			  	 
        :type symbol: str  		  	   		  		 			  		 			     			  	 
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		  		 			  		 			     			  	 
        :type sd: datetime  		  	   		  		 			  		 			     			  	 
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		  		 			  		 			     			  	 
        :type ed: datetime  		  	   		  		 			  		 			     			  	 
        :param sv: The starting value of the portfolio  		  	   		  		 			  		 			     			  	 
        :type sv: int  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
        # add your code to do learning here  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
        # example usage of the old backward compatible util function  		  	   		  		 			  		 			     			  	 
        syms = [symbol]
        sd_b = sd - timedelta(days = self.window)		  	   		  		 			  		 			     			  	 
        dates = pd.date_range(sd_b, ed)  		  	   		  		 			  		 			     			  	 
        prices_all = ut.get_data(syms, dates)  # automatically adds SPY  		  	   		  		 			  		 			     			  	 
        prices_stock = prices_all[syms]  # only portfolio symbols  		  	   		  		 			  		 			     			  	  		  	   		  		 			  		 			     			  	 
        if self.verbose:  		  	   		  		 			  		 			     			  	 
            print(prices_stock)

        # getting indicators
        skt_data_copy = prices_stock.copy()
        ema = idn.ema_crossover(stock_data = skt_data_copy, symbol=symbol)
        skt_data_copy = prices_stock.copy()
        momentum = idn.momentum(stock_data = skt_data_copy, symbol=symbol, days=5)
        skt_data_copy = prices_stock.copy()
        bbpt = idn.bb_pct(stock_data = skt_data_copy,symbol=symbol,days = 20)


        # combining df
        ema_df = ema[['ema_ratio',]]
        momentum_df = momentum[['momentum']]
        bbpt_df = bbpt[['Bollinger_bands_%']]
        indicator_dataframe = pd.concat((ema_df, momentum_df, bbpt_df), axis = 1)
        indicator_dataframe = indicator_dataframe[indicator_dataframe.index >= sd]
        indicator_dataframe = indicator_dataframe[:-self.lookfoward_period]

        x_train = indicator_dataframe.values

        #print(indicator_dataframe)

        y_train = []
        prices_stock = prices_stock[prices_stock.index >= sd]
        for i in range(prices_stock.shape[0] - self.lookfoward_period):
            price_ratio = ((prices_stock.loc[prices_stock.index[i + self.lookfoward_period],symbol] - prices_stock.loc[prices_stock.index[i],symbol])/prices_stock.loc[prices_stock.index[i],symbol])
            if price_ratio > (self.price_threshold + self.impact):
                y_train.append(1)  # long
            elif price_ratio < (self.price_threshold + self.impact):
                y_train.append(-1) # short
            else:
                y_train.append(0)

        y_train = np.array(y_train)

        # Training
        self.learner.add_evidence(x_train, y_train)
  		 			     			  	 
    # this method should use the existing policy and test it against new data  		  	   		  		 			  		 			     			  	 
    def testPolicy(  		  	   		  		 			  		 			     			  	 
        self,  		  	   		  		 			  		 			     			  	 
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

        syms = [symbol]
        sd_b = sd - timedelta(days = self.window)		  	   		  		 			  		 			     			  	 
        dates = pd.date_range(sd_b, ed)  		  	   		  		 			  		 			     			  	 
        prices_all = ut.get_data(syms, dates)  # automatically adds SPY  		  	   		  		 			  		 			     			  	 
        prices_stock = prices_all[syms]  # only portfolio symbols  		  	   		  		 			  		 			     			  	  		  	   		  		 			  		 			     			  	 
        if self.verbose:  		  	   		  		 			  		 			     			  	 
            print(prices_stock)

        # getting indicators
        skt_data_copy = prices_stock.copy()
        ema = idn.ema_crossover(stock_data = skt_data_copy, symbol=symbol)
        skt_data_copy = prices_stock.copy()
        momentum = idn.momentum(stock_data = skt_data_copy, symbol=symbol, days=5)
        skt_data_copy = prices_stock.copy()
        bbpt = idn.bb_pct(stock_data = skt_data_copy,symbol=symbol,days = 20)


        # combining df
        ema_df = ema[['ema_ratio',]]
        momentum_df = momentum[['momentum']]
        bbpt_df = bbpt[['Bollinger_bands_%']]
        indicator_dataframe = pd.concat((ema_df, momentum_df, bbpt_df), axis = 1)
        indicator_dataframe = indicator_dataframe[indicator_dataframe.index >= sd]

        x_test = indicator_dataframe.values

        # quering learner to get y_test for x_test
        y_test = self.learner.query(x_test)
        trades = pd.DataFrame(columns = ['Order','Shares'],index = indicator_dataframe.index)
        trades.loc[:] = 0

        flag=0
        for i in range(0,indicator_dataframe.shape[0]-1):
            if flag==0:
                if y_test[i]>0:
                    trades.loc[trades.index[i],'Shares'] = 1000
                    trades.loc[trades.index[i],'Order'] = 'BUY'
                    flag = 1
                elif y_test[i]<0:
                    trades.loc[trades.index[i],'Shares'] = -1000
                    trades.loc[trades.index[i],'Order'] = 'SELL'
                    flag = -1

            elif flag==1:
                if y_test[i]<0:
                    trades.loc[trades.index[i],'Shares']=-2000
                    trades.loc[trades.index[i],'Order'] = 'SELL'
                    flag=-1
                elif y_test[i]==0:
                    trades.loc[trades.index[i],'Shares']=-1000
                    trades.loc[trades.index[i],'Order'] = 'Do Nothing'
                    flag = 0

            else:
                if y_test[i]>0:
                    trades.loc[trades.index[i],'Shares']=2000
                    trades.loc[trades.index[i],'Order'] = 'BUY'
                    flag=1
                elif y_test[i]==0:
                    trades.loc[trades.index[i],'Shares']=1000
                    trades.loc[trades.index[i],'Order'] = 'Do Nothing'
                    flag=0

        if flag==-1:
            trades.loc[trades.index[indicator_dataframe.shape[0]-1],'Shares'] = 1000
            trades.loc[trades.index[indicator_dataframe.shape[0]-1],'Order'] = 'BUY'
        elif flag==1:
            trades.loc[trades.index[indicator_dataframe.shape[0]-1],'Shares']=-1000
            trades.loc[trades.index[indicator_dataframe.shape[0]-1],'Order'] = 'SELL'

        trades['Symbol'] = symbol
        trades = pd.DataFrame(trades['Shares'])
        return trades

        # creating trades df



  		  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    print("One does not simply think up a strategy")  		  	   		  		 			  		 			     			  	 
