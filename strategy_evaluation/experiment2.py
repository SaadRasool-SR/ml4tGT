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
import ManualStrategy as ms
import StrategyLearner as sl 
import matplotlib.pyplot as plt
import marketsim as marketsim
import numpy as np

def author(): 
  return 'srasool7' # replace tb34 with your Georgia Tech username.  
  		  	   		  		 			  		 			     			  	 
def experiment2(symbol):
    np.random.seed(1234567)
    random.seed(1234567)
    cr_port_value = []
    num_trades = []
    impact_value = [0.0, 0.05, 0.1]

    for i in impact_value:
        learner = sl.StrategyLearner(verbose = False, impact = i, commission=0.0)
        learner.add_evidence(symbol = symbol, sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,12,31), sv = 100000) # training phase 
        df_trades_insample_learner = learner.testPolicy(symbol = symbol, sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,12,31), sv = 100000)
        
        df_trades_insample_learner['Symbol'] = symbol
        for i in df_trades_insample_learner.index:
            if df_trades_insample_learner.loc[i,'Shares'] < 0:
                df_trades_insample_learner.loc[i,'Order'] = 'SELL'
                df_trades_insample_learner.loc[i,'Shares'] = abs(df_trades_insample_learner.loc[i,'Shares'])

            elif df_trades_insample_learner.loc[i,'Shares'] > 0:
                df_trades_insample_learner.loc[i,'Order'] = 'BUY'
                df_trades_insample_learner.loc[i,'Shares'] = abs(df_trades_insample_learner.loc[i,'Shares'])
            
            else:
                df_trades_insample_learner.loc[i,'Order'] = 0 
        
        
        port_val_optimal_lr = marketsim.compute_portvals(df_trades_insample_learner,start_val=100000,commission=9.95,impact=0.005)
        port_val_optimal_norm_lr_insample = port_val_optimal_lr /port_val_optimal_lr[0]
        cr = marketsim.get_cr(port_val_optimal_lr)
        

        cr_port_value.append(cr)
        num_trades.append(df_trades_insample_learner[df_trades_insample_learner['Order'] != 0].shape[0])


    plt.plot(impact_value, cr_port_value, color='red',label = 'Cum Return vs impact')
    plt.grid()
    plt.title('Insample Experiment 2 - Cum Return vs Impact : ' + symbol)
    plt.xlabel('Impact')
    plt.ylabel('Cum Return')
    plt.xticks(fontsize = 8)
    plt.yticks(fontsize = 8)
    plt.legend(loc = "lower left")
    plt.savefig('./images/'+'Cum Return vs Impact Experiment 2' + symbol +'.png')
    plt.cla()


    plt.plot(impact_value, num_trades, color='red',label = 'Num Trades vs impact')
    plt.grid()
    plt.title('Insample Experiment 2 - Num Trades vs Impact: ')
    plt.xlabel('Impact')
    plt.ylabel('Num Trades')
    plt.xticks(fontsize = 8)
    plt.yticks(fontsize = 8)
    plt.legend(loc = "lower left")
    plt.savefig('./images/'+'Num Trades vs Impact Experiment 2'+'.png')
    plt.cla()
		  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    print("One does not simply think up a strategy")  		  	   		  		 			  		 			     			  	 
