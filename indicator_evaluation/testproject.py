import TheoreticallyOptimalStrategy as tos
import datetime as dt
import marketsimcode as marketsim
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from util import get_data, plot_data  	
import datetime as dt
import indicators


def author():  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    :return: The GT username of the student  		  	   		  		 			  		 			     			  	 
    :rtype: str  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    return "srasool7"

def testproject():
    # TheoreticallyOptimalStrategy
    df_trades = tos.testPolicy(symbol = "JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000)  
    port_val_optimal = marketsim.compute_portvals(df_trades,start_val=100000,commission=0.00,impact=0.00)
    benchmark = {
        'Symbol':['JPM','JPM'],
        'Order':['BUY','SELL'],
        'Shares':[1000, 1000]        
    }
    df_benchmark = pd.DataFrame(benchmark, index = [dt.datetime(2008, 1, 2),dt.datetime(2009, 12, 31)])
    port_val_benchmark = marketsim.compute_portvals(df_benchmark, start_val=100000, commission=0.00, impact=0.00)
    port_val_optimal_norm = port_val_optimal /port_val_optimal[0]
    port_val_benchmark_norm = port_val_benchmark / port_val_benchmark[0]

    port_val_optimal_dr = marketsim.get_dr(port_val_optimal)
    port_val_benchmark_dr = marketsim.get_dr(port_val_benchmark)
    port_val_optimal_adr = marketsim.get_adr(port_val_optimal_dr)
    port_val_benchmark_adr = marketsim.get_adr(port_val_benchmark_dr)
    port_val_optimal_sddr = marketsim.get_sddr(port_val_optimal_dr)
    port_val_benchmark_ssdr = marketsim.get_sddr(port_val_benchmark_dr)




    def plot_data(data1, data2, title, xtitle, ytitle):
        plt.plot(data1, color='red',label = 'Optimal')
        plt.plot(data2 ,color='purple',label = 'Benchmark')
        plt.grid()
        plt.title(title)
        plt.xlabel(xtitle)
        plt.ylabel(ytitle)
        plt.xticks(fontsize = 8)
        plt.yticks(fontsize = 8)
        plt.legend()
        plt.savefig('./images/'+title+'.png')
        plt.cla()

    plot_data(port_val_optimal_norm,port_val_benchmark_norm, 'Benchmark vs Optimal Trading Strategy','Date', 'Normalized Cumulative Performance')
    
    start_date = dt.datetime(2007, 1, 1)
    end_date = dt.datetime(2009,12,31)
    symbol = ["JPM"]
    dates = pd.date_range(dt.datetime.strftime(start_date, '%Y-%m-%d'), dt.datetime.strftime(end_date, '%Y-%m-%d'))
    stock_data = get_data(symbol, dates)

    golden_cross = indicators.golden_death_cross(stock_data,symbol)
    golden_cross = golden_cross[golden_cross.index >= dt.datetime(2008, 1, 1)]

    golden_cross_norm = golden_cross.iloc[:,:-1]/golden_cross.iloc[0,:-1]

    buy_golden_cross = golden_cross[golden_cross['golden_death_cross'] == 'BUY']
    buy_golden_cross_norm = buy_golden_cross.iloc[:,:-1]/buy_golden_cross.iloc[0,:-1]

    sell_death_cross = golden_cross[golden_cross['golden_death_cross'] == 'SELL']
    sell_death_cross_norm = sell_death_cross.iloc[:,:-1]/sell_death_cross.iloc[0,:-1]

    def plot_data(data1, data2, data3, data4, data5 ,title, xtitle, ytitle):
        plt.plot(data1, color='red',label = 'price')
        plt.plot(data2 ,color='green',label = 'Golden_cross', marker='X', linestyle='None', markersize = 10.0)
        plt.plot(data3 ,color='black',label = 'Death_cross',marker='o', linestyle='None', markersize = 10.0)
        plt.plot(data4 ,color='blue',label = 'sma_50')
        plt.plot(data5 ,color='pink',label = 'sma_200')
        plt.grid()
        plt.title(title)
        plt.xlabel(xtitle)
        plt.ylabel(ytitle)
        plt.xticks(fontsize = 8)
        plt.yticks(fontsize = 8)
        plt.legend()
        plt.savefig('./images/'+title+'.png')
        plt.cla()

    plot_data(golden_cross[symbol],
              buy_golden_cross['50_sma'],
              sell_death_cross['200_sma'],
              golden_cross['50_sma'],
              golden_cross['200_sma'],
              'Golden and Death Cross Indicator',
              'Date',
              'Price($)')

    stock_data = get_data(symbol, dates)
    rsi_df = indicators.rsi(stock_data, symbol, period = 14)
    rsi_df = rsi_df[rsi_df.index >= dt.datetime(2008, 1, 1)]
    buy_rsi = rsi_df[rsi_df['rsi_signal'] == 'BUY']
    sell_rsi = rsi_df[rsi_df['rsi_signal'] == 'SELL']

    def plot_data_rsi(data2, data3, data4 ,title, xtitle, ytitle):
        #plt.plot(data1, color='red',label = 'price')
        plt.plot(data2, color='blue',label = 'rsi_value')
        plt.plot(data3 ,color='green',label = 'rsi_buy', marker='X', linestyle='None', markersize = 7.0)
        plt.plot(data4 ,color='black',label = 'rsi_sell',marker='o', linestyle='None', markersize = 7.0)
        plt.axhline(y = 30, color = 'r', linestyle = '--')
        plt.axhline(y = 70, color = 'r', linestyle = '--')
        plt.grid()
        plt.title(title)
        plt.xlabel(xtitle)
        plt.ylabel(ytitle)
        plt.xticks(fontsize = 8)
        plt.yticks(fontsize = 8)
        plt.legend()
        plt.savefig('./images/'+title+'.png')
        plt.cla()

    plot_data_rsi(rsi_df['rsi'],
                buy_rsi['rsi'],
                sell_rsi['rsi'],
                'Rsi 14 days Indicator',
                'Date',
                'Rsi')
    
    stock_data = get_data(symbol, dates)
    ema_df = indicators.ema_crossover(stock_data, symbol)
    ema_df = ema_df[ema_df.index >= dt.datetime(2008, 1, 1)]
    ema_df_norm = ema_df.iloc[:,:-1]/ema_df.iloc[0,:-1]
    buy_ema = ema_df[ema_df['ema_crossover_signal'] == 'BUY']
    ema_df_norm_buy = buy_ema.iloc[:,:-1]/buy_ema.iloc[0,:-1]
    sell_ema = ema_df[ema_df['ema_crossover_signal'] == 'SELL']
    ema_df_norm_sell = sell_ema.iloc[:,:-1]/sell_ema.iloc[0,:-1]

    

    def plot_data_ema(data1, data2, data3, data4, data5, data6,title, xtitle, ytitle):
        plt.plot(data1, color='red',label = 'price')
        plt.plot(data2, color='blue',label = 'ema_12')
        plt.plot(data3, color='black',label = 'ema_26')
        plt.plot(data4, color='orange',label = 'ema_ratio')
        plt.plot(data5 ,color='green',label = 'buy', marker='X', linestyle='None', markersize = 8.0)
        plt.plot(data6 ,color='black',label = 'sell',marker='o', linestyle='None', markersize = 8.0)
        plt.grid()
        plt.title(title)
        plt.xlabel(xtitle)
        plt.ylabel(ytitle)
        plt.xticks(fontsize = 8)
        plt.yticks(fontsize = 8)
        plt.legend()
        plt.savefig('./images/'+title+'.png')
        plt.cla()

    plot_data_ema(ema_df_norm['JPM'],
            ema_df_norm['ema_12'],
            ema_df_norm['ema_26'],
            ema_df_norm['ema_ratio'],
            ema_df_norm_buy['ema_12'],
            ema_df_norm_sell['ema_12'],
            'Ema 12 and 26 Crossover Indicator',
            'Date',
            'Normailized Value')
    
    stock_data = get_data(symbol, dates)
    momentum_df = indicators.momentum(stock_data,symbol,days = 5)
    momentum_df = momentum_df[momentum_df.index >= dt.datetime(2008, 1, 1)]
    buy_momentum = momentum_df[momentum_df['momentum_signal'] == 'BUY']
    sell_momentum = momentum_df[momentum_df['momentum_signal'] == 'SELL']

    def plot_data_ema(data1, data2, data3, title, xtitle, ytitle):
        plt.plot(data1, color='red',label = 'momentum')
        plt.plot(data2 ,color='green',label = 'buy', marker='X', linestyle='None', markersize = 8.0)
        plt.plot(data3 ,color='black',label = 'sell',marker='o', linestyle='None', markersize = 8.0)
        plt.grid()
        plt.title(title)
        plt.xlabel(xtitle)
        plt.ylabel(ytitle)
        plt.xticks(fontsize = 8)
        plt.yticks(fontsize = 8)
        plt.legend()
        plt.savefig('./images/'+title+'.png')
        plt.cla()

    plot_data_ema(momentum_df['momentum'],
            buy_momentum['momentum'],
            sell_momentum['momentum'],
            'Momentum Indicator',
            'Date',
            'Momentum %')
    

    stock_data = get_data(symbol, dates)

    bollinger_band_pct = indicators.bb_pct(stock_data,symbol,days = 20)
    bollinger_band_pct = bollinger_band_pct[bollinger_band_pct.index >= dt.datetime(2008, 1, 1)]
    bollinger_band_pct_norm = (bollinger_band_pct.iloc[:,:-1] - bollinger_band_pct.iloc[0,:-1].mean())/bollinger_band_pct.iloc[0,:-1].std()


    #buy_bollinger_band = bollinger_band_pct[bollinger_band_pct['BB_%_signal'] == 'BUY']
    #buy_bollinger_band_norm = (buy_bollinger_band.iloc[:,:-1] - buy_bollinger_band.iloc[:,:-1].mean())/buy_bollinger_band.iloc[0,:-1].std()

    #sell_bollinger_band = bollinger_band_pct[bollinger_band_pct['BB_%_signal'] == 'SELL']
    #sell_bollinger_band_norm = (sell_bollinger_band.iloc[:,:-1] - sell_bollinger_band.iloc[:,:-1].mean())  /sell_bollinger_band.iloc[0,:-1].std()

    def plot_data_bb(symbol, data1, data2, data3, data4,title, xtitle, ytitle):
        plt.plot(data1, color='red',label = symbol[0])
        plt.plot(data2, color='Blue',label = 'lower_bound')
        plt.plot(data3, color='Blue',label = 'upper_bound')
        plt.plot(data4, color='black',label = 'rolling_mean')
        plt.grid()
        plt.title(title)
        plt.xlabel(xtitle)
        plt.ylabel(ytitle)
        plt.xticks(fontsize = 8)
        plt.yticks(fontsize = 8)
        plt.legend()
        plt.savefig('./images/'+title+'.png')
        plt.cla()

    plot_data_bb(symbol,
                bollinger_band_pct[symbol],
                bollinger_band_pct['lower_bound'],
                bollinger_band_pct['upper_bound'],
                bollinger_band_pct['rolling_mean'],
                'Bollinger_Band_Indicator',
                'Date',
                'Price_Value')
    
    def plot_data_bb(data1, title, xtitle, ytitle):
        plt.plot(data1, color='black',label = 'Bollinger_bands_%')
        plt.axhline(y = 0, color = 'r', linestyle = '--')
        plt.axhline(y = 1, color = 'r', linestyle = '--')
        plt.grid()
        plt.title(title)
        plt.xlabel(xtitle)
        plt.ylabel(ytitle)
        plt.xticks(fontsize = 8)
        plt.yticks(fontsize = 8)
        plt.legend()
        plt.savefig('./images/'+title+'.png')
        plt.cla()

    plot_data_bb(
                bollinger_band_pct['Bollinger_bands_%'],
                'Bollinger_Band_Indicator_%',
                'Date',
                'Bollinger_Band_Indicator_%')


    #print(port_val_optimal)
    
if __name__ == "__main__":
    testproject() 