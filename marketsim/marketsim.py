""""""  		  	   		  		 			  		 			     			  	 
"""MC2-P1: Market simulator.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
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
#import os  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
import numpy as np
import math 		  	   		  		 			  		 			     			  	   	   		  		 			  		 			     			  	 
import pandas as pd
pd.options.display.max_columns = None
pd.options.display.max_rows = None  	   		  		 			  		 			     			  	 
from util import get_data, plot_data



def get_cr(port_value_sum):
    cr =  (port_value_sum[-1]/port_value_sum[0]) - 1
    return cr

def get_dr(port_value_sum):
    dr = (port_value_sum/port_value_sum.shift(1)) - 1
    dr = dr[1:]
    return dr

def get_adr(dr):
    adr = dr.mean()
    return adr

def get_sddr(dr):
    sddr = dr.std()
    return sddr

def get_sr(adr,sddr,k):
    sr = math.sqrt(k) * (adr/sddr)
    return sr



def author():  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    :return: The GT username of the student  		  	   		  		 			  		 			     			  	 
    :rtype: str  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    return "srasool7"
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
def compute_portvals(  		  	   		  		 			  		 			     			  	 
    orders_file="./orders/orders.csv",  		  	   		  		 			  		 			     			  	 
    start_val=1000000,  		  	   		  		 			  		 			     			  	 
    commission=9.95,  		  	   		  		 			  		 			     			  	 
    impact=0.005,  		  	   		  		 			  		 			     			  	 
):  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    Computes the portfolio values.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    :param orders_file: Path of the order file or the file object  		  	   		  		 			  		 			     			  	 
    :type orders_file: str or file object  		  	   		  		 			  		 			     			  	 
    :param start_val: The starting value of the portfolio  		  	   		  		 			  		 			     			  	 
    :type start_val: int  		  	   		  		 			  		 			     			  	 
    :param commission: The fixed amount in dollars charged for each transaction (both entry and exit)  		  	   		  		 			  		 			     			  	 
    :type commission: float  		  	   		  		 			  		 			     			  	 
    :param impact: The amount the price moves against the trader compared to the historical data at each transaction  		  	   		  		 			  		 			     			  	 
    :type impact: float  		  	   		  		 			  		 			     			  	 
    :return: the result (portvals) as a single-column dataframe, containing the value of the portfolio for each trading day in the first column from start_date to end_date, inclusive.  		  	   		  		 			  		 			     			  	 
    :rtype: pandas.DataFrame  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    # this is the function the autograder will call to test your code  		  	   		  		 			  		 			     			  	 
    # NOTE: orders_file may be a string, or it may be a file object. Your  		  	   		  		 			  		 			     			  	 
    # code should work correctly with either input  		  	   		  		 			  		 			     			  	 
    # TODO: Your code here		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    # In the template, instead of computing the value of the portfolio, we just  		  	   		  		 			  		 			     			  	 
    # read in the value of IBM over 6 months  		  	   		  		 			  		 			     			  	 
    # start_date = dt.datetime(2008, 1, 1)  		  	   		  		 			  		 			     			  	 
    # end_date = dt.datetime(2008, 6, 1)  		  	   		  		 			  		 			     			  	 
    # portvals = get_data(["IBM"], pd.date_range(start_date, end_date))  		  	   		  		 			  		 			     			  	 
    # portvals = portvals[["IBM"]]  # remove SPY  		  	   		  		 			  		 			     			  	 
    # rv = pd.DataFrame(index=portvals.index, data=portvals.values)  		  	   		  		 			  		 			     			  	 	  	   		  		 			  		 			     			  	 
    #return rv  		  	   		  		 			  		 			     			  	 
    #return portvals
    
    orders_df = pd.read_csv(orders_file, index_col='Date', parse_dates=True, na_values=['nan'])
    orders_df.sort_index(inplace=True)
    orders_df = orders_df.dropna()
    start_date = orders_df.index[0]
    end_date = orders_df.index[-1]
    list_of_stock = orders_df['Symbol'].unique()

    dates = pd.date_range(dt.datetime.strftime(start_date, '%Y-%m-%d'), dt.datetime.strftime(end_date, '%Y-%m-%d'))
    stock_data = get_data(list_of_stock, dates)

    list_of_cols = np.append(list_of_stock,'Cash')
    trades = pd.DataFrame(columns=list_of_cols, index=stock_data.index)
    #holdings = pd.DataFrame(columns=list_of_cols, index=orders_df.index.unique())
    holdings = pd.DataFrame(columns=list_of_cols, index=stock_data.index)

    trades = trades.fillna(0)
    for row in range(orders_df.shape[0]): 
        timestamp = orders_df.index[row]
        symbol = orders_df['Symbol'][row]
        order =  orders_df['Order'][row]
        shares =  orders_df['Shares'][row]
        current_cash = trades.loc[timestamp,'Cash']
        current_share = trades.loc[timestamp,symbol] 
        stock_price = stock_data.loc[timestamp,symbol]

        if str(current_cash) == str(np.nan):
            current_cash = 0

        if str(current_share) == str(np.nan):
            current_share = 0

        if order == 'BUY':
            trades.loc[timestamp,symbol] = shares + current_share
            cash_cal = stock_price*(1 + impact) * -shares  # Transaction costs , market imapct
            cash_cal -= commission # Transaction costs , commissions

        else:
            trades.loc[timestamp,symbol] = -shares + current_share
            cash_cal = stock_price*(1 - impact) * shares  # Transaction costs , market imapct
            cash_cal -= commission # Transaction costs , commissions

        
        trades.loc[timestamp,'Cash'] = cash_cal + current_cash

    for stock in list_of_stock:

        shares = 0
        for row in range(trades.shape[0]):
            shares += trades.loc[trades.index[row],stock]
            holdings.loc[holdings.index[row],stock] = shares

    cash_total = start_val
    for row in range(holdings.shape[0]):
        cash_total += trades.loc[trades.index[row],'Cash']
        holdings.loc[holdings.index[row],'Cash'] = cash_total


    # values:

    values = holdings.copy()
    values['Total_Value'] = np.nan

    for stock in list_of_stock:
        for row in range(values.shape[0]):
            stock_price = stock_data.loc[values.index[row],stock]
            shares = values.loc[values.index[row],stock]
            stock_value = stock_price * shares
            values.loc[values.index[row],stock] = stock_value

    values['Total_Value'] = values.sum(axis = 1)

    df = values['Total_Value']

    return df

    print('worked')
	  	   		  		 			  		 			     			  	 
def test_code():  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    Helper function to test code  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    # this is a helper function you can use to test your code  		  	   		  		 			  		 			     			  	 
    # note that during autograding his function will not be called.  		  	   		  		 			  		 			     			  	 
    # Define input parameters  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    of = "./orders/orders-01.csv"
    #of = "./orders/additional_orders/orders-01.csv" 

    files_names = os.listdir('./New Folder/')
    path = './New Folder/' 	  	   		  		 			  		 			     			  	 
    sv = 1000000
    #of = "./orders/additional_orders/orders-01.csv" 
    portvals = compute_portvals(orders_file=of, start_val=sv)

    #print(author())  		  	   		  		 			  		 			     			  	 

    # for file in files_names:
    #     fullpath = path + file     	   		  		 			  		 			     			  	 
    #     # Process orders  		  	   		  		 			  		 			     			  	 
    #     portvals = compute_portvals(orders_file=fullpath, start_val=sv)

    #     if isinstance(portvals, pd.DataFrame):  		  	   		  		 			  		 			     			  	 
    #         portvals = portvals[portvals.columns[0]]  # just get the first column  		  	   		  		 			  		 			     			  	 
    #     else:  		  	   		  		 			  		 			     			  	 
    #         "warning, code did not return a DataFrame"
    #     print('----------------')
    #     print(f"filename:{file}, final_portval:{portvals}")		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    # print('done')


    dr = get_dr(portvals)
    adr = get_adr(dr)
    cr = get_cr(portvals)
    sddr = get_sddr(dr)
    sr = get_sr(adr,sddr,252)

    print(dr)
    print(adr)
    print(cr)
    print(sddr)
    print(sr)
    # average daily return 

    # sharpe Ratio


    # Get portfolio stats  		  	   		  		 			  		 			     			  	 
    # Here we just fake the data. you should use your code from previous assignments.  		  	   		  		 			  		 			     			  	 
    # start_date = dt.datetime(2008, 1, 1)  		  	   		  		 			  		 			     			  	 
    # end_date = dt.datetime(2008, 6, 1)  		  	   		  		 			  		 			     			  	 
    # cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = [  		  	   		  		 			  		 			     			  	 
    #     0.2,  		  	   		  		 			  		 			     			  	 
    #     0.01,  		  	   		  		 			  		 			     			  	 
    #     0.02,  		  	   		  		 			  		 			     			  	 
    #     1.5,  		  	   		  		 			  		 			     			  	 
    # ]  		  	   		  		 			  		 			     			  	 
    # cum_ret_SPY, avg_daily_ret_SPY, std_daily_ret_SPY, sharpe_ratio_SPY = [  		  	   		  		 			  		 			     			  	 
    #     0.2,  		  	   		  		 			  		 			     			  	 
    #     0.01,  		  	   		  		 			  		 			     			  	 
    #     0.02,  		  	   		  		 			  		 			     			  	 
    #     1.5,  		  	   		  		 			  		 			     			  	 
    # ]  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    # # Compare portfolio against $SPX  		  	   		  		 			  		 			     			  	 
    # print(f"Date Range: {start_date} to {end_date}")  		  	   		  		 			  		 			     			  	 
    # print()  		  	   		  		 			  		 			     			  	 
    # print(f"Sharpe Ratio of Fund: {sharpe_ratio}")  		  	   		  		 			  		 			     			  	 
    # print(f"Sharpe Ratio of SPY : {sharpe_ratio_SPY}")  		  	   		  		 			  		 			     			  	 
    # print()  		  	   		  		 			  		 			     			  	 
    # print(f"Cumulative Return of Fund: {cum_ret}")  		  	   		  		 			  		 			     			  	 
    # print(f"Cumulative Return of SPY : {cum_ret_SPY}")  		  	   		  		 			  		 			     			  	 
    # print()  		  	   		  		 			  		 			     			  	 
    # print(f"Standard Deviation of Fund: {std_daily_ret}")  		  	   		  		 			  		 			     			  	 
    # print(f"Standard Deviation of SPY : {std_daily_ret_SPY}")  		  	   		  		 			  		 			     			  	 
    # print()  		  	   		  		 			  		 			     			  	 
    # print(f"Average Daily Return of Fund: {avg_daily_ret}")  		  	   		  		 			  		 			     			  	 
    # print(f"Average Daily Return of SPY : {avg_daily_ret_SPY}")  		  	   		  		 			  		 			     			  	 
    # print()  		  	   		  		 			  		 			     			  	 
    # print(f"Final Portfolio Value: {portvals[-1]}")  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    test_code()  		  	   		  		 			  		 			     			  	 
