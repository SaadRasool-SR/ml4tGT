""""""  		  	   		  		 			  		 			     			  	 
"""  		  	   		  		 			  		 			     			  	 
Test a learner.  (c) 2015 Tucker Balch  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
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
"""  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
import math  		  	   		  		 			  		 			     			  	 
import sys  		  	   		  		 			  		 			     			  	 	  	   		  		 			  		 			     			  	 
import numpy as np  		  	   		  		 			  		 			     			  	 	  	   		  		 			  		 			     			  	 
#import LinRegLearner as lrl
import random as  rand
import DTLearner as dt
import RTLearner as rt
import BagLearner as bl
import InsaneLearner as it
import matplotlib.pyplot as plt
#import time
#tart_time = time.time()

  		  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    if len(sys.argv) != 2:  		  	   		  		 			  		 			     			  	 
        print("Usage: python testlearner.py <filename>")  		  	   		  		 			  		 			     			  	 
        sys.exit(1)  		  	   		  		 			  		 			     			  	 
    inf = open(sys.argv[1])
    if inf.name.rsplit('/',-1)[-1] == 'Istanbul.csv':  	   		  		 			  		 			     			  	 
        data = np.array(  		  	   		  		 			  		 			     			  	 
            [list(map(float, s.strip().split(",")[1:])) for s in inf.readlines()[1:]]  		  	   		  		 			  		 			     			  	 
        )
    else:
        data = np.array(  		  	   		  		 			  		 			     			  	 
            [list(map(float, s.strip().split(","))) for s in inf.readlines()]  		  	   		  		 			  		 			     			  	 
        )

    np.random.seed(1234567)

    #remove NA's
    data = data[~np.isnan(data).any(axis=1)]

    # data shuffle
    np.random.shuffle(data)

	  	   		  		 			  		 			     			  	 
    # compute how much of the data is training and testing  		  	   		  		 			  		 			     			  	 
    train_rows = int(0.6* data.shape[0])  		#### change it from 0.6  	   		  		 			  		 			     			  	 
    test_rows = data.shape[0] - train_rows  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    # separate out training and testing data  		  	   		  		 			  		 			     			  	 
    Xtrain = data[:train_rows, 0:-1]  		  	   		  		 			  		 			     			  	 
    Ytrain = data[:train_rows, -1]  		  	   		  		 			  		 			     			  	 
    Xtest = data[train_rows:, 0:-1]  		  	   		  		 			  		 			     			  	 
    Ytest = data[train_rows:, -1]  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    
    leaf_size = 100
    increments = 2
    leaf_array = np.arange(0,leaf_size,increments)

    def plot_array(x, y, plot_title, x_ax_label, y_ax_label, y2=None):

        plt.plot(x, y, label = 'In_Sample')
        plt.plot(x, y2, label = 'Out_Sample')
        plt.title(plot_title)
        plt.xlabel(x_ax_label)
        plt.ylabel(y_ax_label)
        plt.legend()
        plt.savefig('./images/'+plot_title+'.png')

        
        #plt.show()

    
    def Experiment(learner_type, Xtrain, Ytrain, leaf_size, increments, performance_metric):
        metric_in_sample = []
        metric_out_sample = []
        for leaf in range(0,leaf_size,increments):
            if learner_type == 'DTLearner':
                learner = dt.DTLearner(leaf_size = leaf, verbose = False) # constructor

            if learner_type == 'RTLearner':
                learner = rt.RTLearner(leaf_size = leaf, verbose = False) # constructor

            learner.add_evidence(Xtrain, Ytrain) # training step

            pred_y_train = learner.query(Xtrain)  # get the predictions
            pred_y_test = learner.query(Xtest)  # get the predictions

            if performance_metric == 'rmse': 		  	   		  		 			  		 			     			  	 
                metric_train = math.sqrt(((Ytrain - pred_y_train) ** 2).sum() / Ytrain.shape[0])	   		  		 			  		 			     			  	 
                metric_test = math.sqrt(((Ytest - pred_y_test) ** 2).sum() / Ytest.shape[0])

            if performance_metric == 'r2':
                ytrain_mean = Ytrain.mean()
                ytest_mean =  Ytest.mean()	
                rss_train = ((Ytrain - pred_y_train) ** 2).sum()
                rss_test = ((Ytest - pred_y_test) ** 2).sum()
                rss_tot_train = ((Ytrain - ytrain_mean) ** 2).sum()
                rss_tot_test = ((Ytest - ytest_mean) ** 2).sum()
                metric_train = 1 - (rss_train/rss_tot_train)
                metric_test = 1 - (rss_test/rss_tot_test)

            if performance_metric == 'mae':
                abs_err_train = abs(pred_y_train - Ytrain).sum()
                abs_err_test = abs(pred_y_test - Ytest).sum()
                metric_train = abs_err_train / Ytrain.shape[0]
                metric_test = abs_err_test / Ytest.shape[0]


            metric_in_sample.append(metric_train)
            metric_out_sample.append(metric_test)
        
        return metric_in_sample,metric_out_sample

    def experiment_bag(learner_type, number_exp, bag_size, Xtrain, Ytrain, leaf_size, increments, performance_metric):

        array_element = int(leaf_size/increments)

        metric_in_sample_total = np.zeros([array_element])
        metric_out_sample_total = np.zeros([array_element])

        for exp in range(number_exp):
            metric_in_sample = np.array([])
            metric_out_sample = np.array([])
        

            for leaf in range(0,leaf_size,increments):
                if learner_type == 'DTLearner':
                    learner = bl.BagLearner(learner = dt.DTLearner, kwargs = {"leaf_size":leaf}, bags = bag_size, boost = False, verbose = False)
                
                if learner_type == 'RTLearner':
                    learner = bl.BagLearner(learner = rt.RTLearner, kwargs = {"leaf_size":leaf}, bags = bag_size, boost = False, verbose = False)

                learner.add_evidence(Xtrain, Ytrain) # training step
        
                pred_y_train = learner.query(Xtrain)  # get the predictions
                pred_y_test = learner.query(Xtest)  # get the predictions 

                if performance_metric == 'rmse':	  	   		  		 			  		 			     			  	 
                    train_metric = math.sqrt(((Ytrain - pred_y_train) ** 2).sum() / Ytrain.shape[0])
                    test_metric = math.sqrt(((Ytest - pred_y_test) ** 2).sum() / Ytest.shape[0])


                if performance_metric == 'r2':
                    ytrain_mean = Ytrain.mean()
                    ytest_mean =  Ytest.mean()	
                    rss_train = ((Ytrain - pred_y_train) ** 2).sum()
                    rss_test = ((Ytest - pred_y_test) ** 2).sum()
                    rss_tot_train = ((Ytrain - ytrain_mean) ** 2).sum()
                    rss_tot_test = ((Ytest - ytest_mean) ** 2).sum()
                    train_metric = 1 - (rss_train/rss_tot_train)
                    test_metric = 1 - (rss_test/rss_tot_test)

                if performance_metric == 'mae':
                    abs_err_train = abs(pred_y_train - Ytrain).sum()
                    abs_err_test = abs(pred_y_test - Ytest).sum()
                    train_metric = abs_err_train / Ytrain.shape[0]
                    test_metric = abs_err_test / Ytest.shape[0]
                    

                metric_in_sample = np.append(metric_in_sample,[train_metric])
                metric_out_sample = np.append(metric_out_sample,[test_metric])

            metric_in_sample_total += metric_in_sample
            metric_out_sample_total += metric_out_sample

        metric_in_sample_avg = metric_in_sample_total / number_exp
        metric_out_sample_avg = metric_out_sample_total / number_exp

        return metric_in_sample_avg, metric_out_sample_avg


###### Experiment Calls


#import InsaneLearner as it  
    learner = it.InsaneLearner(verbose = False) # constructor  
    learner.add_evidence(Xtrain, Ytrain) # training step  
    Y = learner.query(Xtest) # query

# # Experiment 1:

    # learner_type = 'DTLearner'
    # performance_metric = 'rmse'
    # metric_in_sample,metric_out_sample = Experiment(learner_type, Xtrain, Ytrain, leaf_size, increments, performance_metric)    
    # plot_array(leaf_array, metric_in_sample, plot_title = 'Rmse vs Leaf_Size (Overfitting Analysis)', x_ax_label = 'leaf size', y_ax_label = 'Rmse', y2=metric_out_sample)



# # Experiment 2:

    # learner_type = 'DTLearner'  
    # number_exp = 2
    # bag_size = 20
    # performance_metric = 'rmse'
    # metric_in_sample_avg, metric_out_sample_avg = experiment_bag(learner_type,number_exp, bag_size, Xtrain, Ytrain, leaf_size, increments,performance_metric)
    # plt.clf()
    # plot_array(leaf_array, metric_in_sample_avg, plot_title = 'Rmse vs Leaf_Size (Overfitting Analysis with Bagging (size = 20))', x_ax_label = 'leaf size', y_ax_label = 'Rmse', y2=metric_out_sample_avg)



# # Experiment 3:
    # leaf_size = 100
    # increments = 2 

    # learner_type = 'DTLearner'
    # performance_metric = 'r2'
    # metric_in_sample,metric_out_sample = Experiment(learner_type, Xtrain, Ytrain, leaf_size, increments, performance_metric)    
    # plt.clf()
    # plot_array(leaf_array, metric_in_sample, plot_title = 'R2 vs Leaf_Size - DTLearner', x_ax_label = 'leaf size', y_ax_label = 'R2', y2=metric_out_sample)

    # learner_type = 'RTLearner'
    # performance_metric = 'r2'
    # metric_in_sample,metric_out_sample = Experiment(learner_type, Xtrain, Ytrain, leaf_size, increments, performance_metric)    
    # plt.clf()
    # plot_array(leaf_array, metric_in_sample, plot_title = 'R2 vs Leaf_Size - RTLearner', x_ax_label = 'leaf size', y_ax_label = 'R2', y2=metric_out_sample)

    
    # learner_type = 'DTLearner'
    # performance_metric = 'mae'
    # metric_in_sample, metric_out_sample = Experiment(learner_type, Xtrain, Ytrain, leaf_size, increments, performance_metric)    
    # plt.clf()
    # plot_array(leaf_array, metric_in_sample, plot_title = 'mae vs Leaf_Size - DTLearner', x_ax_label = 'leaf size', y_ax_label = 'Mae', y2=metric_out_sample)

    # learner_type = 'RTLearner'
    # performance_metric = 'mae'
    # metric_in_sample,metric_out_sample = Experiment(learner_type, Xtrain, Ytrain, leaf_size, increments, performance_metric)    
    # plt.clf() 
    # plot_array(leaf_array, metric_in_sample, plot_title = 'mae vs Leaf_Size - RTLearner', x_ax_label = 'leaf size', y_ax_label = 'Mae', y2=metric_out_sample)

    # ### bagging

    # learner_type = 'DTLearner'  
    # number_exp = 2
    # bag_size = 20
    # performance_metric = 'r2'
    # metric_in_sample_avg, metric_out_sample_avg = experiment_bag(learner_type,number_exp, bag_size, Xtrain, Ytrain, leaf_size, increments,performance_metric)
    # plt.clf() 
    # plot_array(leaf_array, metric_in_sample_avg, plot_title = 'R2 vs Leaf_Size - DTLearner with Bagging (size = 20)', x_ax_label = 'leaf size', y_ax_label = 'R2', y2=metric_out_sample_avg)

    # learner_type = 'RTLearner'  
    # number_exp = 2
    # bag_size = 20
    # performance_metric = 'r2'
    # metric_in_sample_avg, metric_out_sample_avg = experiment_bag(learner_type,number_exp, bag_size, Xtrain, Ytrain, leaf_size, increments,performance_metric)
    # plt.clf() 
    # plot_array(leaf_array, metric_in_sample_avg, plot_title = 'R2 vs Leaf_Size - RTLearner with Bagging (size = 20)', x_ax_label = 'leaf size', y_ax_label = 'R2', y2=metric_out_sample_avg)

    
    # learner_type = 'DTLearner'  
    # number_exp = 2
    # bag_size = 20
    # performance_metric = 'mae'
    # metric_in_sample_avg, metric_out_sample_avg = experiment_bag(learner_type,number_exp, bag_size, Xtrain, Ytrain, leaf_size, increments,performance_metric)
    # plt.clf() 
    # plot_array(leaf_array, metric_in_sample_avg, plot_title = 'Mae vs Leaf_Size -DTLearner with Bagging (size = 20)', x_ax_label = 'leaf size', y_ax_label = 'mae', y2=metric_out_sample_avg)

    # learner_type = 'RTLearner'  
    # number_exp = 2
    # bag_size = 20
    # performance_metric = 'mae'
    # metric_in_sample_avg, metric_out_sample_avg = experiment_bag(learner_type,number_exp, bag_size, Xtrain, Ytrain, leaf_size, increments,performance_metric)
    # plt.clf() 
    # plot_array(leaf_array, metric_in_sample_avg, plot_title = 'Mae vs Leaf_Size - RTLearner with Bagging (size = 20)', x_ax_label = 'leaf size', y_ax_label = 'mae', y2=metric_out_sample_avg)

    # #print("--- %s seconds ---" % (time.time() - start_time))


