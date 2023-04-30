""""""  		  	   		  		 			  		 			     			  	 
"""Assess a betting strategy.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
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
  		  	   		  		 			  		 			     			  	 
import numpy as np
import sys  		  	   		  		 			  		 			     			  	 
np.set_printoptions(threshold=sys.maxsize)
import matplotlib.pyplot as plt  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
def author():  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    :return: The GT username of the student  		  	   		  		 			  		 			     			  	 
    :rtype: str  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    return "srasool7"  # replace tb34 with your Georgia Tech username.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
def gtid():  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    :return: The GT ID of the student  		  	   		  		 			  		 			     			  	 
    :rtype: int  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    return 903857343  # replace with your GT ID number  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
def get_spin_result(win_prob):  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    :param win_prob: The probability of winning  		  	   		  		 			  		 			     			  	 
    :type win_prob: float  		  	   		  		 			  		 			     			  	 
    :return: The result of the spin.  		  	   		  		 			  		 			     			  	 
    :rtype: bool  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    result = False  		  	   		  		 			  		 			     			  	 
    if np.random.random() <= win_prob:  		  	   		  		 			  		 			     			  	 
        result = True  		  	   		  		 			  		 			     			  	 
    return result  

def experiment_1(max_spins, max_episodes, win_prob,exp_array,bankroll, bankroll_limit):
    for epi in range(max_episodes):
        winnings_list = []
        stop_bet_spin =[]
        episode_winnings = 0
        num_spin = 0
        max_num_spin_reached = False
        while num_spin < max_spins:
            while episode_winnings < 80 and not max_num_spin_reached:
                if bankroll == True:
                    if bankroll_limit >= episode_winnings:
                        break
                won = False
                bet_amount = 1
                while not won:
                    #wager bet_amount on black
                    won = get_spin_result(win_prob)
                    if won == True:
                        episode_winnings = episode_winnings + bet_amount
                    else:
                        episode_winnings = episode_winnings - bet_amount
                        bet_amount = bet_amount * 2
                    if bankroll == True:
                        if bet_amount > episode_winnings + abs(bankroll_limit):
                            bet_amount = episode_winnings + abs(bankroll_limit)
                    winnings_list.append(episode_winnings)
                    #if episode_winnings >= 80 or num_spin >= max_spins:
                    #    won = True
                    #    max_num_spin_reached = True
                    stop_bet_spin.append(num_spin)
                    num_spin += 1
            num_spin += 1
        #print(winnings_list)
        exp_array[epi,1:stop_bet_spin[-1]+2] = winnings_list
        exp_array[epi,stop_bet_spin[-1]+2:] = winnings_list[-1]
    return exp_array
            
def plot_array(df_array,plot_title, x_ax_label, y_ax_label, x_range_min, x_range_max, y_range_min, y_range_max):
    x_values = list(range(0,df_array.shape[1]))
    for row in range(len(df_array)):
        plt.plot(x_values,df_array[row],label = 'episode: '+str(row+1))
    plt.xlim(x_range_min,x_range_max)
    plt.ylim(y_range_min,y_range_max)
    plt.title(plot_title)
    plt.xlabel(x_ax_label)
    plt.ylabel(y_ax_label)
    plt.legend()
    plt.savefig('./images/'+plot_title+'.png')

def mean_std_median_calc(exp_data_array):
    
    exp_data_array[-3,:] = np.mean(exp_data_array,axis=0)
    exp_data_array[-2,:] = np.std(exp_data_array,axis=0)
    exp_data_array[-1,:] = np.median(exp_data_array,axis=0)

    #exp_data_array[1000,:] = np.mean(exp_data_array,axis=0)
    #exp_data_array[1001,:] = np.std(exp_data_array,axis=0)
    #exp_data_array[1002,:] = np.median(exp_data_array,axis=0)

    return exp_data_array

def plot_array_2(df_array,plot_title, x_ax_label, y_ax_label, x_range_min, x_range_max, y_range_min, y_range_max):
    plt.cla()
    x_values = list(range(0,df_array.shape[1]))
    plt.plot(x_values,df_array[1000],label = 'Winning mean')
    plt.plot(x_values,df_array[1001],label = 'Winning std')
    plt.plot(x_values,df_array[1000] + df_array[1001],label = 'Winning mean + Winning std')
    plt.plot(x_values,df_array[1000] - df_array[1001],label = 'Winning mean - Winning std')

    plt.xlim(x_range_min,x_range_max)
    plt.ylim(y_range_min,y_range_max)
    plt.title(plot_title)
    plt.xlabel(x_ax_label)
    plt.ylabel(y_ax_label)
    plt.legend()
    plt.savefig('./images/'+plot_title+'.png')

def plot_array_3(df_array,plot_title, x_ax_label, y_ax_label, x_range_min, x_range_max, y_range_min, y_range_max):
    plt.cla()
    x_values = list(range(0,df_array.shape[1]))
    plt.plot(x_values,df_array[1002],label = 'Winning median')
    plt.plot(x_values,df_array[1002] + df_array[1001],label = 'Winning median + Winning std')
    plt.plot(x_values,df_array[1002] - df_array[1001],label = 'Winning median - Winning std')

    plt.xlim(x_range_min,x_range_max)
    plt.ylim(y_range_min,y_range_max)
    plt.title(plot_title)
    plt.xlabel(x_ax_label)
    plt.ylabel(y_ax_label)
    plt.legend()
    plt.savefig('./images/'+plot_title+'.png')

# def experiment(max_spins, max_episodes, win_prob,exp_array, bankroll, bankroll_limit):
#     for epi in range(1):
#         winnings_list = []
#         stop_bet_spin =[]
#         episode_winnings = 0
#         num_spin = 0
#         max_num_spin_reached = False
#         while num_spin < max_spins:
#             while episode_winnings < 80 and not max_num_spin_reached:
#                 if bankroll == True:
#                     if bankroll_limit >= episode_winnings:
#                         break
#                 won = False
#                 bet_amount = 1
#                 while not won:
#                     #wager bet_amount on black
#                     won = get_spin_result(win_prob)
#                     if won == True:
#                         episode_winnings = episode_winnings + bet_amount
#                     else:
#                         episode_winnings = episode_winnings - bet_amount
#                         bet_amount = bet_amount * 2

#                     if bankroll == True:
#                         if bet_amount > episode_winnings + abs(bankroll_limit):
#                             bet_amount = episode_winnings + abs(bankroll_limit)

#                     winnings_list.append(episode_winnings)
#                     if episode_winnings >= 80 or num_spin >= max_spins:
#                         won = True
#                         max_num_spin_reached = True
#                         stop_bet_spin.append(num_spin)
#                     num_spin += 1
#             num_spin += 1
#         print(winnings_list)
#         print(stop_bet_spin)
#         #exp_array[epi,1:stop_bet_spin[0]+2] = winnings_list
#         #exp_array[epi,stop_bet_spin[0]+2:] = winnings_list[-1]
#    return exp_array

def test_code():  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    Method to test your code  		  	   		  		 			  		 			     			  	 
    """

    # American Roulette has 38 numbers in total, 2 green (0 and double 00)
    # red = 18
    # black = 18
    # win prob = 18/38 		  	   		  		 			  		 			     			  	 	  	   		  		 			  		 			     			  	 
    # add your code here to implement the experiments
    
    # constant variables 
    win_prob = 18/38  # set appropriately to the probability of a win  	 	  	   		  		 			  		 			     			  	 		  	   		  		 			  		 			     			  	 
    np.random.seed(gtid())  # do this only once  		  	   		  		 			  		 			     			  	 		  	   		  		 			  		 			     			  	 
    # add your code here to implement the experiments

    # experiment 1_part 1
    number_of_spins = 1001
    number_of_episodes = 10
    exp_array = np.empty(shape=[number_of_episodes,number_of_spins])
    exp_array[:,0] = 0
    experiment_1_array = experiment_1(number_of_spins,number_of_episodes,win_prob,exp_array,bankroll=False,bankroll_limit=0)
    plot_array(experiment_1_array,plot_title='Figure:1', x_ax_label='Number of spins', y_ax_label='Winnings($)',x_range_min=0,x_range_max=300,y_range_min=-256, y_range_max=100)
    
    # experiment 1 part 2
    number_of_spins = 1001
    number_of_episodes = 1003
    exp_array = np.empty(shape=[number_of_episodes,number_of_spins])
    exp_array[:,0] = 0
    experiment_1_2_array = experiment_1(number_of_spins,number_of_episodes,win_prob,exp_array,bankroll=False,bankroll_limit=0)
    experiment_1_2_array = mean_std_median_calc(experiment_1_2_array)
    plot_array_2(experiment_1_2_array,plot_title='Figure:2', x_ax_label='Number of spins', y_ax_label='Mean each Spin Winnings for all episodes',x_range_min=0,x_range_max=300,y_range_min=-256, y_range_max=100)
  		  	   		  		 			  		 			     			  	 
    # experiment 1 part 3
    plot_array_3(experiment_1_2_array,plot_title='Figure:3', x_ax_label='Number of spins', y_ax_label='Median each Spin Winnings for all episodes',x_range_min=0,x_range_max=300,y_range_min=-256, y_range_max=100)

    # experiment 2 part 1
    bankroll = True
    bankroll_limit = -256
    number_of_spins = 1001
    number_of_episodes = 1003
    exp_array = np.empty(shape=[number_of_episodes,number_of_spins])
    exp_array[:,0] = 0


    experiment_2_1_array= experiment_1(number_of_spins, number_of_episodes, win_prob, exp_array, bankroll, bankroll_limit)
    print(experiment_2_1_array.max(axis = 1))
    print(experiment_2_1_array.min(axis = 1))
    print(experiment_2_1_array)
    print(np.count_nonzero(experiment_2_1_array.max(axis = 1) == 80))
    print(np.count_nonzero(experiment_2_1_array.min(axis = 1) == -256))
    
    experiment_2_1_array = mean_std_median_calc(experiment_2_1_array)
    plot_array_2(experiment_2_1_array,plot_title='Figure:4', x_ax_label='Number of spins', y_ax_label='Mean each Spin Winnings for all episodes',x_range_min=0,x_range_max=300,y_range_min=-256, y_range_max=100)

    
    # experiment 2 part 2
    plot_array_3(experiment_2_1_array,plot_title='Figure:5', x_ax_label='Number of spins', y_ax_label='Median each Spin Winnings for all episodes',x_range_min=0,x_range_max=300,y_range_min=-256, y_range_max=100)

if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    test_code()  		  	   		  		 			  		 			     			  	 
