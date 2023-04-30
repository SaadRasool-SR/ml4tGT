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

def experiment_1(symbol):
    np.random.seed(1234567)
    random.seed(1234567)

    #INSAMPLE
    ######### Manual Strategy
    df_trades_insample_ms = ms.testPolicy(symbol= symbol, sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,12,31), sv = 1000000)
    
    df_trades_insample_ms['Symbol'] = symbol
    for i in df_trades_insample_ms.index:
        if df_trades_insample_ms.loc[i,'Shares'] < 0:
            df_trades_insample_ms.loc[i,'Order'] = 'SELL'
            df_trades_insample_ms.loc[i,'Shares'] = abs(df_trades_insample_ms.loc[i,'Shares'])

        elif df_trades_insample_ms.loc[i,'Shares'] > 0:
            df_trades_insample_ms.loc[i,'Order'] = 'BUY'
            df_trades_insample_ms.loc[i,'Shares'] = abs(df_trades_insample_ms.loc[i,'Shares'])
        
        else:
            df_trades_insample_ms.loc[i,'Order'] = 0 
    

    
    port_val_optimal_ms = marketsim.compute_portvals(df_trades_insample_ms,start_val=100000,commission=9.95,impact=0.005)
    benchmark = {
        'Symbol':[symbol,symbol],
        'Order':['BUY','SELL'],
        'Shares':[1000, 1000]        
    }
    #port_val_optimal
    df_benchmark_insample = pd.DataFrame(benchmark, index = [dt.datetime(2008, 1, 2),dt.datetime(2009, 12, 31)])
    port_val_benchmark_insample = marketsim.compute_portvals(df_benchmark_insample, start_val=100000, commission=9.95, impact=0.005)
    port_val_optimal_norm_insample = port_val_optimal_ms /port_val_optimal_ms[0]
    port_val_benchmark_norm_insample = port_val_benchmark_insample / port_val_benchmark_insample[0]
    
    #learner
    learner = sl.StrategyLearner(verbose = False, impact = 0.0, commission=0.0)
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

    plt.plot(port_val_optimal_norm_insample , color='red',label = 'Manual Strategy')
    plt.plot(port_val_benchmark_norm_insample , color='purple',label = 'Benchmark')
    plt.plot(port_val_optimal_norm_lr_insample , color='black',label = 'Strategy Learner')
    plt.grid()
    plt.title('Insample Experiment 1 -' + symbol)
    plt.xlabel('Period')
    plt.ylabel('Normalized Returns')
    plt.xticks(fontsize = 8)
    plt.yticks(fontsize = 8)
    plt.legend(loc = "lower left")
    plt.savefig('./images/'+'Insample Experiment 1'+'.png')
    plt.cla()


    
    #OUTSAMPLE
    ######### Manual Strategy
    df_trades_outsample_ms = ms.testPolicy(symbol= symbol, sd=dt.datetime(2010,1,1), ed=dt.datetime(2011,12,31), sv = 1000000)
    
    df_trades_outsample_ms['Symbol'] = symbol
    for i in df_trades_outsample_ms.index:
        if df_trades_outsample_ms.loc[i,'Shares'] < 0:
            df_trades_outsample_ms.loc[i,'Order'] = 'SELL'
            df_trades_outsample_ms.loc[i,'Shares'] = abs(df_trades_outsample_ms.loc[i,'Shares'])

        elif df_trades_outsample_ms.loc[i,'Shares'] > 0:
            df_trades_outsample_ms.loc[i,'Order'] = 'BUY'
            df_trades_outsample_ms.loc[i,'Shares'] = abs(df_trades_outsample_ms.loc[i,'Shares'])
        
        else:
            df_trades_outsample_ms.loc[i,'Order'] = 0 

    
    port_val_optimal_ms = marketsim.compute_portvals(df_trades_outsample_ms,start_val=100000,commission=9.95,impact=0.005)

    benchmark = {
        'Symbol':[symbol,symbol],
        'Order':['BUY','SELL'],
        'Shares':[1000, 1000]        
    }
    #port_val_optimal
    df_benchmark_outsample = pd.DataFrame(benchmark, index = [dt.datetime(2010, 1, 4),dt.datetime(2011, 12, 30)])
    port_val_benchmark_outsample  = marketsim.compute_portvals(df_benchmark_outsample , start_val=100000, commission=9.95, impact=0.005)
    port_val_optimal_norm_outsample  = port_val_optimal_ms /port_val_optimal_ms[0]
    port_val_benchmark_norm_outsample  = port_val_benchmark_outsample  / port_val_benchmark_outsample [0]

    #learner
    df_trades_outsample_learner = learner.testPolicy(symbol = symbol, sd=dt.datetime(2010,1,1), ed=dt.datetime(2011,12,31), sv = 100000) # testing phase  	   		  		 			  		 			     			  	 
    #print(df_trades_outsample_learner)
    
    df_trades_outsample_learner['Symbol'] = symbol
    for i in df_trades_outsample_learner.index:
        if df_trades_outsample_learner.loc[i,'Shares'] < 0:
            df_trades_outsample_learner.loc[i,'Order'] = 'SELL'
            df_trades_outsample_learner.loc[i,'Shares'] = abs(df_trades_outsample_learner.loc[i,'Shares'])

        elif df_trades_outsample_learner.loc[i,'Shares'] > 0:
            df_trades_outsample_learner.loc[i,'Order'] = 'BUY'
            df_trades_outsample_learner.loc[i,'Shares'] = abs(df_trades_outsample_learner.loc[i,'Shares'])
        
        else:
            df_trades_outsample_learner.loc[i,'Order'] = 0
    
    
    
    
    port_val_optimal_lr = marketsim.compute_portvals(df_trades_outsample_learner,start_val=100000,commission=9.95,impact=0.005)
    port_val_optimal_norm_lr_outsample = port_val_optimal_lr /port_val_optimal_lr[0]


    plt.plot(port_val_optimal_norm_outsample , color='red',label = 'Manual Strategy')
    plt.plot(port_val_benchmark_norm_outsample , color='purple',label = 'Benchmark')
    plt.plot(port_val_optimal_norm_lr_outsample , color='black',label = 'Strategy Learner')
    plt.grid()
    plt.title('Outsample Experiment 1 -' + symbol)
    plt.xlabel('Period')
    plt.ylabel('Normalized Returns')
    plt.xticks(fontsize = 8)
    plt.yticks(fontsize = 8)
    plt.legend(loc = "lower left")
    plt.savefig('./images/'+'Outsample Experiment 1'+'.png')
    plt.cla()


if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    print("One does not simply think up a strategy")
    	  	   		  		 			  		 			     			  	 
