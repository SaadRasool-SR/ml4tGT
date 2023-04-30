from util import get_data, plot_data
import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = None
pd.options.display.max_rows = None

def author():  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    :return: The GT username of the student  		  	   		  		 			  		 			     			  	 
    :rtype: str  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    return "srasool7"

def get_stock_data(symbol,sd,ed):
    dates = pd.date_range(sd,ed)
    stock_data = get_data(symbol, dates)
    return  stock_data


def testPolicy(symbol, sd, ed, sv):
    stock_data = get_stock_data([symbol],sd,ed)
    adj_close = stock_data[symbol]
    today_stock_price = adj_close.loc[adj_close.index[0]]
    money = sv
    orders_df = pd.DataFrame(columns=['Symbol','Order','Shares'])
    dates_buy = []
    dates_sell = []
    trading = True

    x = 0
   #for x in range(stock_data.shape[0]):
    while trading:
        buy = False
        sell = False
        #Hold = False
        short = False
        action = []

        while not buy:
            if x == adj_close.shape[0] - 1:
                trading = False
                break
            next_day_price = adj_close.loc[adj_close.index[x + 1]]
            # buying 
            if next_day_price > today_stock_price:
                buy = True
                action.append(adj_close.index[x])
                action.append(symbol)
                action.append('BUY')
                action.append(1000)
                #orders_df.loc[len(orders_df)] = action
                orders_df.loc[adj_close.index[x],'Order'] = 'BUY'
                if str(orders_df.loc[adj_close.index[x],'Shares']) == 'nan':
                    orders_df.loc[adj_close.index[x],'Shares'] = 1000
                else:
                    orders_df.loc[adj_close.index[x],'Shares'] = 1000 + orders_df.loc[adj_close.index[x],'Shares']
            
            # # shorting     
            elif next_day_price < today_stock_price:
                buy = True
                short = True
                action.append(adj_close.index[x])
                action.append(symbol)
                action.append('SELL')
                action.append(1000)
                #orders_df.loc[len(orders_df)] = action
                orders_df.loc[adj_close.index[x],'Order'] = 'SELL'
                if str(orders_df.loc[adj_close.index[x],'Shares']) == 'nan':
                    orders_df.loc[adj_close.index[x],'Shares'] = 1000
                else:    
                    orders_df.loc[adj_close.index[x],'Shares'] = 1000 + orders_df.loc[adj_close.index[x],'Shares']

            else:
                today_stock_price = next_day_price
                x += 1

        while buy and not sell:
            action = []

            if x == adj_close.shape[0] - 1:
                if orders_df.iloc[-1]['Order'] == 'BUY':
                    sell = True
                    orders_df.loc[adj_close.index[x],'Order'] = 'SELL'
                    orders_df.loc[adj_close.index[x],'Shares'] = 1000
                    action.append(adj_close.index[x])
                    action.append(symbol)
                    action.append('SELL')
                    action.append(1000)
                    #orders_df.loc[len(orders_df)] = action
                trading = False
                break

            next_day_price = adj_close.loc[adj_close.index[x + 1]]

            if next_day_price > today_stock_price and not short:
                today_stock_price = next_day_price
                x+=1
            
            elif next_day_price < today_stock_price and short:
                today_stock_price = next_day_price
                x+=1

            elif short and next_day_price > today_stock_price:
                sell = True
                action.append(adj_close.index[x])
                action.append(symbol)
                action.append('BUY')
                action.append(1000)
                #orders_df.loc[len(orders_df)] = action
                orders_df.loc[adj_close.index[x],'Order'] = 'BUY'
                orders_df.loc[adj_close.index[x],'Shares'] = 1000

            else:
                sell = True
                action.append(adj_close.index[x])
                action.append(symbol)
                action.append('SELL')
                action.append(1000)
                #orders_df.loc[len(orders_df)] = action
                orders_df.loc[adj_close.index[x],'Order'] = 'SELL'
                orders_df.loc[adj_close.index[x],'Shares'] = 1000
                #x-=1

        

    #orders_df = orders_df.set_index('Date')
    orders_df['Symbol'] = 'JPM'

    return orders_df

