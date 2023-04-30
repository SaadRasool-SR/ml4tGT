"""Analyze a portfolio.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
Copyright 2017, Georgia Tech Research Corporation  		  	   		  		 			  		 			     			  	 
Atlanta, Georgia 30332-0415  		  	   		  		 			  		 			     			  	 
All Rights Reserved  		  	   		  		 			  		 			     			  	 
"""  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
import datetime as dt  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
import numpy as np  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
import pandas as pd  		  	   		  		 			  		 			     			  	 
from util import get_data, plot_data
import math  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
def data_cleaning(df):
    df.fillna(method= "ffill", inplace = True)
    df.fillna(method= "bfill", inplace = True)
    return df

def normalized(df):
    df = df/df.ix[0,:]
    return df

def allocations(df, allocs):
    df = df * allocs
    return df

def port_val(df,start_val):
    df = df * start_val
    return df

def portfolio_value(df):
    df = df.sum(axis = 1)
    return df

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


# This is the function that will be tested by the autograder  		  	   		  		 			  		 			     			  	 
# The student must update this code to properly implement the functionality  		  	   		  		 			  		 			     			  	 
def assess_portfolio(  		  	   		  		 			  		 			     			  	 
    sd=dt.datetime(2008, 1, 1),  		  	   		  		 			  		 			     			  	 
    ed=dt.datetime(2009, 1, 1),  		  	   		  		 			  		 			     			  	 
    syms=["GOOG", "AAPL", "GLD", "XOM"],  		  	   		  		 			  		 			     			  	 
    allocs=[0.1, 0.2, 0.3, 0.4],  		  	   		  		 			  		 			     			  	 
    sv=1000000,  		  	   		  		 			  		 			     			  	 
    rfr=0.0,  		  	   		  		 			  		 			     			  	 
    sf=252.0,  		  	   		  		 			  		 			     			  	 
    gen_plot=False,  		  	   		  		 			  		 			     			  	 
):  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    Estimate a set of test points given the model we built.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		  		 			  		 			     			  	 
    :type sd: datetime  		  	   		  		 			  		 			     			  	 
    :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		  		 			  		 			     			  	 
    :type ed: datetime  		  	   		  		 			  		 			     			  	 
    :param syms: A list of 2 or more symbols that make up the portfolio (note that your code should support any symbol in the data directory)  		  	   		  		 			  		 			     			  	 
    :type syms: list  		  	   		  		 			  		 			     			  	 
    :param allocs:  A list of 2 or more allocations to the stocks, must sum to 1.0  		  	   		  		 			  		 			     			  	 
    :type allocs: list  		  	   		  		 			  		 			     			  	 
    :param sv: The starting value of the portfolio  		  	   		  		 			  		 			     			  	 
    :type sv: int  		  	   		  		 			  		 			     			  	 
    :param rfr: The risk free return per sample period that does not change for the entire date range (a single number, not an array)  		  	   		  		 			  		 			     			  	 
    :type rfr: float  		  	   		  		 			  		 			     			  	 
    :param sf: Sampling frequency per year  		  	   		  		 			  		 			     			  	 
    :type sf: float  		  	   		  		 			  		 			     			  	 
    :param gen_plot: If True, optionally create a plot named plot.png. The autograder will always call your  		  	   		  		 			  		 			     			  	 
        code with gen_plot = False.  		  	   		  		 			  		 			     			  	 
    :type gen_plot: bool  		  	   		  		 			  		 			     			  	 
    :return: A tuple containing the cumulative return, average daily returns,  		  	   		  		 			  		 			     			  	 
        standard deviation of daily returns, Sharpe ratio and end value  		  	   		  		 			  		 			     			  	 
    :rtype: tuple  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    # Read in adjusted closing prices for given symbols, date range  		  	   		  		 			  		 			     			  	 
    dates = pd.date_range(sd, ed)  		  	   		  		 			  		 			     			  	 
    prices_all = get_data(syms, dates)  # automatically adds SPY  		  	   		  		 			  		 			     			  	 
    prices = prices_all[syms]  # only portfolio symbols  		  	   		  		 			  		 			     			  	 
    prices_SPY = prices_all["SPY"]  # only SPY, for comparison later  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    # Get daily portfolio value  		  	   		  		 			  		 			     			  	 
    #port_val = prices_SPY  # add code here to compute daily portfolio values 

    # Data cleaning / forward and backfill data
    portfolio = data_cleaning(prices)

    #normalized
    portfolio_norm = normalized(portfolio)


    #allocation  
    alloced = allocations(portfolio_norm, allocs)

    #port_val
    pos_val = port_val(alloced,sv)

    port_value_sum = portfolio_value(pos_val)

    dr = get_dr(port_value_sum)
    adr = get_adr(dr)
    cr = get_cr(port_value_sum)
    sddr = get_sddr(dr)
    sr = get_sr(adr,sddr,252)

	   		  		 			  		 			     			  	 
    # Get portfolio statistics (note: std_daily_ret = volatility)  		  	   		  		 			  		 			     			  	 
    #cr, adr, sddr, sr = [  		  	   		  		 			  		 			     			  	 
    #    0.25,  		  	   		  		 			  		 			     			  	 
    #    0.001,  		  	   		  		 			  		 			     			  	 
    #    0.0005,  		  	   		  		 			  		 			     			  	 
    #    2.1,  		  	   		  		 			  		 			     			  	 
    #]  # add code here to compute stats  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    # Compare daily portfolio value with SPY using a normalized plot  		  	   		  		 			  		 			     			  	 
    if gen_plot:  		  	   		  		 			  		 			     			  	 
        # add code to plot here  		  	   		  		 			  		 			     			  	 
        df_temp = pd.concat(  		  	   		  		 			  		 			     			  	 
            [port_value_sum, prices_SPY], keys=["Portfolio", "SPY"], axis=1  		  	   		  		 			  		 			     			  	 
        )  		  	   		  		 			  		 			     			  	 
        pass  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    # Add code here to properly compute end value  		  	   		  		 			  		 			     			  	 
    ev = (np.array(allocs) * sv * cr).sum() + sv 	   		  		 			  		 			     			  	 
  		  	   		  		 				     			  	 
    return cr, adr, sddr, sr, ev  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
def test_code():  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    Performs a test of your code and prints the results  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    # This code WILL NOT be tested by the auto grader  		  	   		  		 			  		 			     			  	 
    # It is only here to help you set up and test your code  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    # Define input parameters  		  	   		  		 			  		 			     			  	 
    # Note that ALL of these values will be set to different values by  		  	   		  		 			  		 			     			  	 
    # the autograder!  		  	   		  		 			  		 			     			  	 
    start_date = dt.datetime(2010,1,1)  		  	   		  		 			  		 			     			  	 
    end_date = dt.datetime(2010, 12, 31)  		  	   		  		 			  		 			     			  	 
    symbols = ["GOOG", "AAPL", "GLD", "XOM"]  		  	   		  		 			  		 			     			  	 
    allocations = [0.2, 0.3, 0.4, 0.1]  		  	   		  		 			  		 			     			  	 
    start_val = 1000000  		  	   		  		 			  		 			     			  	 
    risk_free_rate = 0.0  		  	   		  		 			  		 			     			  	 
    sample_freq = 252  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    # Assess the portfolio  		  	   		  		 			  		 			     			  	 
    cr, adr, sddr, sr, ev = assess_portfolio(  		  	   		  		 			  		 			     			  	 
        sd=start_date,  		  	   		  		 			  		 			     			  	 
        ed=end_date,  		  	   		  		 			  		 			     			  	 
        syms=symbols,  		  	   		  		 			  		 			     			  	 
        allocs=allocations,  		  	   		  		 			  		 			     			  	 
        sv=start_val,  		  	   		  		 			  		 			     			  	 
        gen_plot=False,  		  	   		  		 			  		 			     			  	 
    )  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    #Print statistics  		  	   		  		 			  		 			     			  	 
    # print(f"Start Date: {start_date}")  		  	   		  		 			  		 			     			  	 
    # print(f"End Date: {end_date}")  		  	   		  		 			  		 			     			  	 
    # print(f"Symbols: {symbols}")  		  	   		  		 			  		 			     			  	 
    # print(f"Allocations: {allocations}")  		  	   		  		 			  		 			     			  	 
    print(f"Sharpe Ratio: {sr}")  		  	   		  		 			  		 			     			  	 
    #print(f"Volatility (stdev of daily returns): {sddr}")  		  	   		  		 			  		 			     			  	 
    print(f"Average Daily Return: {adr}")  		  	   		  		 			  		 			     			  	 
    print(f"Cumulative Return: {cr}")
    #print(f"ev Return: {ev}")   		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    test_code()  		  	   		  		 			  		 			     			  	 
