import numpy as np
from sklearn.tree import DecisionTreeRegressor

class SDTLearner(object):  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    This is a Linear Regression Learner. It is implemented correctly.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		  		 			  		 			     			  	 
        If verbose = False your code should not generate ANY output. When we test your code, verbose will be False.  		  	   		  		 			  		 			     			  	 
    :type verbose: bool  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    def __init__(self, leaf_size, verbose=False):

        self.leaf_size = leaf_size
        self.verbose = verbose

        """  		  	   		  		 			  		 			     			  	 
        Constructor method  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        #pass  # move along, these aren't the drones you're looking for  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
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
        self.Regressor = DecisionTreeRegressor(criterion='squared_error',splitter='best',min_samples_leaf=self.leaf_size)
        self.Regressor.fit(data_x,data_y)
        

	  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    def query(self, test_array):  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        Estimate a set of test points given the model we built.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
        :param points: A numpy array with each row corresponding to a specific query.  		  	   		  		 			  		 			     			  	 
        :type points: numpy.ndarray  		  	   		  		 			  		 			     			  	 
        :return: The predicted result of the input data according to the trained model  		  	   		  		 			  		 			     			  	 
        :rtype: numpy.ndarray  		  	   		  		 			  		 			     			  	 
        """
        return self.Regressor.predict(test_array)
 	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    print("the secret clue is 'zzyzx'")  		  	   		  		 			  		 			     			  	 
