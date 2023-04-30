""""""  		  	   		  		 			  		 			     			  	 
"""  		  	   		  		 			  		 			     			  	 
A simple wrapper for linear regression.  (c) 2015 Tucker Balch  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
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
  		  	   		  		 			  		 			     			  	 
import numpy as np  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
class BagLearner(object):  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    This is a Linear Regression Learner. It is implemented correctly.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		  		 			  		 			     			  	 
        If verbose = False your code should not generate ANY output. When we test your code, verbose will be False.  		  	   		  		 			  		 			     			  	 
    :type verbose: bool  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    def __init__(self,learner, kwargs, bags, boost, verbose=False):  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        Constructor method  		  	   		  		 			  		 			     			  	 
        """
        self.learner_method = learner
        self.kwargs = kwargs
        self.bags = bags
        self.boost = boost
        self.verbose = verbose		  	   		  		 			  		 			     			  	 
  					  		 			     			  	 
    def author(self):  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        :return: The GT username of the student  		  	   		  		 			  		 			     			  	 
        :rtype: str  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        return "srasool7"  # replace tb34 with your Georgia Tech username  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    def add_evidence(self, data_x, data_y):  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        Add training data to learner  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
        :param data_x: A set of feature values used to train the learner  		  	   		  		 			  		 			     			  	 
        :type data_x: numpy.ndarray  		  	   		  		 			  		 			     			  	 
        :param data_y: The value we are attempting to predict given the X data  		  	   		  		 			  		 			     			  	 
        :type data_y: numpy.ndarray  		  	   		  		 			  		 			     			  	 
        """
        
        self.learner_models = [] 
        ful_df = np.concatenate((data_x,np.atleast_2d(data_y).T), axis=1)
        for  bag in range(self.bags):
            self.learner = self.learner_method(**self.kwargs)
            ful_df_bag = ful_df[np.random.randint(ful_df.shape[0], size=ful_df.shape[0]),:]
            data_x = ful_df_bag[:,:-1]
            data_y = ful_df_bag[:,-1]
            self.learner.add_evidence(data_x,data_y)
            self.learner_models.append(self.learner)  

        		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    def query(self, points):  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        Estimate a set of test points given the model we built.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
        :param points: A numpy array with each row corresponding to a specific query.  		  	   		  		 			  		 			     			  	 
        :type points: numpy.ndarray  		  	   		  		 			  		 			     			  	 
        :return: The predicted result of the input data according to the trained model  		  	   		  		 			  		 			     			  	 
        :rtype: numpy.ndarray  		  	   		  		 			  		 			     			  	 
        """
        #self.ypred_list = []
        ypred_tota = 0
        for lnr in self.learner_models:
            #yprd = self.learner.query(points)
            ypred_tota += lnr.query(points) 
            #self.ypred_list.append(yprd)
        #ypred_avg
        #for arr in self.ypred_list:
        #    arr += arr
        #ypred_avg = arr/len(self.ypred_list)
        return ypred_tota/len(self.learner_models) 	  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    print("the secret clue is 'zzyzx'")  		  	   		  		 			  		 			     			  	 
