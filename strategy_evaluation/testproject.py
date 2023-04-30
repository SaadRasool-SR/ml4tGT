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
import experiment1 as exp1
import numpy as np
import experiment2 as exp2


def test_project():

    ######### Manual Strategy
    np.random.seed(1234567)
    random.seed(1234567)

    symbol = 'JPM'
    df_trades_insample = ms.testPolicy(symbol= symbol, sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,12,31), sv = 1000000)
    
    df_trades_insample['Symbol'] = symbol
    for i in df_trades_insample.index:
        if df_trades_insample.loc[i,'Shares'] < 0:
            df_trades_insample.loc[i,'Order'] = 'SELL'
            df_trades_insample.loc[i,'Shares'] = abs(df_trades_insample.loc[i,'Shares'])

        elif df_trades_insample.loc[i,'Shares'] > 0:
            df_trades_insample.loc[i,'Order'] = 'BUY'
            df_trades_insample.loc[i,'Shares'] = abs(df_trades_insample.loc[i,'Shares'])
        
        else:
            df_trades_insample.loc[i,'Order'] = 0 

          


    port_val_optimal = marketsim.compute_portvals(df_trades_insample,start_val=100000,commission=9.95,impact=0.005)

    benchmark = {
        'Symbol':[symbol,symbol],
        'Order':['BUY','SELL'],
        'Shares':[1000, 1000]        
    }
    #port_val_optimal
    df_benchmark_insample = pd.DataFrame(benchmark, index = [dt.datetime(2008, 1, 2),dt.datetime(2009, 12, 31)])
    port_val_benchmark_insample = marketsim.compute_portvals(df_benchmark_insample, start_val=100000, commission=9.95, impact=0.005)
    port_val_optimal_norm_insample = port_val_optimal /port_val_optimal[0]
    port_val_benchmark_norm_insample = port_val_benchmark_insample / port_val_benchmark_insample[0]

    port_val_optimal_dr_insample = marketsim.get_dr(port_val_optimal)
    port_val_optimal_cr_insample = marketsim.get_cr (port_val_optimal)
    port_val_benchmark_dr_insample = marketsim.get_dr(port_val_benchmark_insample)
    port_val_optimal_adr_insample = marketsim.get_adr(port_val_optimal_dr_insample)
    port_val_benchmark_adr_insample = marketsim.get_adr(port_val_benchmark_dr_insample)
    port_val_optimal_sddr_insample = marketsim.get_sddr(port_val_optimal_dr_insample)
    port_val_benchmark_ssdr_insample = marketsim.get_sddr(port_val_benchmark_dr_insample)

    print(port_val_optimal_sddr_insample)
    print(port_val_optimal_adr_insample)
    print(port_val_optimal_cr_insample)


    plt.plot(port_val_optimal_norm_insample, color='red',label = 'Manual Strategy')
    plt.plot(port_val_benchmark_norm_insample, color='purple',label = 'Benchmark')
    plt.vlines(df_trades_insample[df_trades_insample['Order']=='BUY'].index,ymin = min(min(port_val_optimal_norm_insample),min(port_val_benchmark_norm_insample)),  ymax = max(max(port_val_optimal_norm_insample),max(port_val_benchmark_norm_insample)), color='blue',label = 'LONG', linestyle='solid')
    plt.vlines(df_trades_insample[df_trades_insample['Order']=='SELL'].index,ymin = min(min(port_val_optimal_norm_insample),min(port_val_benchmark_norm_insample)),  ymax = max(max(port_val_optimal_norm_insample),max(port_val_benchmark_norm_insample)), color='black',label = 'SHORT', linestyle='solid')
    plt.grid()
    plt.title('Insample - ' + symbol)
    plt.xlabel('Period')
    plt.ylabel('Normalized Returns')
    plt.xticks(fontsize = 8)
    plt.yticks(fontsize = 8)
    plt.legend(loc = "lower left")
    #plt.savefig('./images/'+'Insample '+ symbol+'.png')
    plt.cla()
    



    df_trades_outsample = ms.testPolicy(symbol= symbol, sd=dt.datetime(2010,1,1), ed=dt.datetime(2011,12,31), sv = 1000000)
    df_trades_outsample['Symbol'] = symbol
    for i in df_trades_outsample.index:
        if df_trades_outsample.loc[i,'Shares'] < 0:
            df_trades_outsample.loc[i,'Order'] = 'SELL'
            df_trades_outsample.loc[i,'Shares'] = abs(df_trades_outsample.loc[i,'Shares'])

        elif df_trades_outsample.loc[i,'Shares'] > 0:
            df_trades_outsample.loc[i,'Order'] = 'BUY'
            df_trades_outsample.loc[i,'Shares'] = abs(df_trades_outsample.loc[i,'Shares'])
        
        else:
            df_trades_outsample.loc[i,'Order'] = 0 

    
    
    
    port_val_optimal = marketsim.compute_portvals(df_trades_outsample,start_val=100000,commission=9.95,impact=0.005)

    benchmark = {
        'Symbol':[symbol,symbol],
        'Order':['BUY','SELL'],
        'Shares':[1000, 1000]        
    }
    #port_val_optimal
    df_benchmark_outsample = pd.DataFrame(benchmark, index = [dt.datetime(2010, 1, 4),dt.datetime(2011, 12, 30)])
    port_val_benchmark_outsample  = marketsim.compute_portvals(df_benchmark_outsample , start_val=100000, commission=9.95, impact=0.005)
    port_val_optimal_norm_outsample  = port_val_optimal /port_val_optimal[0]
    port_val_benchmark_norm_outsample  = port_val_benchmark_outsample  / port_val_benchmark_outsample [0]

    port_val_optimal_dr_outsample  = marketsim.get_dr(port_val_optimal)
    port_val_benchmark_dr_outsample  = marketsim.get_dr(port_val_benchmark_outsample)
    port_val_optimal_adr_outsample  = marketsim.get_adr(port_val_optimal_dr_outsample )
    port_val_benchmark_adr_outsample  = marketsim.get_adr(port_val_benchmark_dr_outsample )
    port_val_optimal_sddr_outsample  = marketsim.get_sddr(port_val_optimal_dr_outsample)
    port_val_benchmark_ssdr_outsample  = marketsim.get_sddr(port_val_benchmark_dr_outsample )
    port_val_optimal_cr_outsample = marketsim.get_cr (port_val_optimal)

    print(port_val_optimal_sddr_outsample)
    print(port_val_optimal_adr_outsample)
    print(port_val_optimal_cr_outsample)


    plt.plot(port_val_optimal_norm_outsample , color='red',label = 'Manual Strategy')
    plt.plot(port_val_benchmark_norm_outsample , color='purple',label = 'Benchmark')
    plt.vlines(df_trades_outsample[df_trades_outsample['Order']=='BUY'].index, ymin = min(min(port_val_optimal_norm_outsample),min(port_val_benchmark_norm_outsample)),  ymax = max(max(port_val_optimal_norm_outsample),max(port_val_benchmark_norm_outsample)), color='blue',label = 'LONG', linestyle='solid')
    plt.vlines(df_trades_outsample[df_trades_outsample['Order']=='SELL'].index,ymin = min(min(port_val_optimal_norm_outsample),min(port_val_benchmark_norm_outsample)),  ymax = max(max(port_val_optimal_norm_outsample),max(port_val_benchmark_norm_outsample)), color='black',label = 'SHORT', linestyle='solid')
    plt.grid()
    plt.title('OutSample - ' + symbol)
    plt.xlabel('Period')
    plt.ylabel('Normalized Returns')
    plt.xticks(fontsize = 8)
    plt.yticks(fontsize = 8)
    plt.legend(loc = "lower left")
    #plt.savefig('./images/'+'Outsample '+symbol +'.png')
    plt.cla()

    ######### Learner Strategy

    #learner = sl.StrategyLearner(verbose = False, impact = 0.0, commission=0.0)
    #learner.add_evidence(symbol = "JPM", sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,12,31), sv = 100000) # training phase 
    #df_trades = learner.testPolicy(symbol = "JPM", sd=dt.datetime(2010,1,1), ed=dt.datetime(2011,12,31), sv = 100000) # testing phase 
    
    exp1.experiment_1(symbol = symbol)

    exp2.experiment2(symbol = symbol)


    

def author(): 
  return 'srasool7' # replace tb34 with your Georgia Tech username.
  		  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    test_project()  		  	   		  		 			  		 			     			  	 
