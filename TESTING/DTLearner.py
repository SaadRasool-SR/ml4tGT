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
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
class DTLearner(object):  		  	   		  		 			  		 			     			  	 
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


    def get_corellation(self, data_x,data_y):
        corr = np.abs(np.corrcoef(data_x, data_y,rowvar = False)[-1,:-1])
        feature = np.argmax(corr)
        if self.verbose == True:
            print('----------------------')
            print(corr)
            print(feature)
            print('----------------------')
        return feature

    def build_tree(self,data_x, data_y):
        self.leaf_factor = -2

        # base cases
        if data_x.shape[0] == 1:
            return np.array([self.leaf_factor, data_y[0], np.nan, np.nan])


        if data_x.shape[0] <= self.leaf_size:
            self.leaf_value = np.mean(data_x)
            return np.array([self.leaf_factor,np.mean(data_y), np.nan, np.nan])
            

        if np.all(data_y == data_y[0]):
            return np.array([self.leaf_factor, np.mean(data_y[0]), np.nan, np.nan])


        else:
            split_feature = self.get_corellation(data_x,data_y)
            split_val = np.median(data_x[:,split_feature], axis = 0)

            
            if split_val == np.max(data_x[:,split_feature]):
                return np.array([self.leaf_factor, np.mean(data_y), np.nan, np.nan])


            left_tree_x = data_x[data_x[:,split_feature] <= split_val]
            left_tree_y = data_y[data_x[:,split_feature] <= split_val]
            right_tree_x = data_x[data_x[:,split_feature] > split_val]
            right_tree_y = data_y[data_x[:,split_feature] > split_val]

           
            left_tree = self.build_tree(left_tree_x,left_tree_y)
            right_tree = self.build_tree(right_tree_x, right_tree_y)
            right_tree_num = np.atleast_2d(left_tree).T.shape[1]
            root = np.array([split_feature, split_val,1,right_tree_num + 1])
            return np.vstack([root, left_tree, right_tree])

        
  		  	   		  		 			  		 			     			  	 
    def add_evidence(self, data_x, data_y):  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        Add training data to learner  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
        :param data_x: A set of feature values used to train the learner  		  	   		  		 			  		 			     			  	 
        :type data_x: numpy.ndarray  		  	   		  		 			  		 			     			  	 
        :param data_y: The value we are attempting to predict given the X data  		  	   		  		 			  		 			     			  	 
        :type data_y: numpy.ndarray	  	   		  		 			  		 			     			  	 
        """
        # nodes, factors, splitval, left, right

        if self.verbose == True:
            print(data_x)
            print(data_y)

        self.decision_tree = self.build_tree(data_x,data_y)

        #print(self.decision_tree)

	  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    def query(self, test_array):  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        Estimate a set of test points given the model we built.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
        :param points: A numpy array with each row corresponding to a specific query.  		  	   		  		 			  		 			     			  	 
        :type points: numpy.ndarray  		  	   		  		 			  		 			     			  	 
        :return: The predicted result of the input data according to the trained model  		  	   		  		 			  		 			     			  	 
        :rtype: numpy.ndarray  		  	   		  		 			  		 			     			  	 
        """

        ypred_array = np.array([])
        for Xtest in test_array:
            if np.atleast_2d(test_array).T.shape[1] == 1:
                Xtest = test_array

            counter = 0
            row = 0

            found = False
            while not found:
                factor = self.decision_tree[int(row)][0]
                if factor == self.leaf_factor:
                    ypred = self.decision_tree[int(row)][1]
                    ypred_array = np.append(ypred_array,[ypred])
                    found = True
                    break
                split_val = self.decision_tree[int(row)][1]
                val_comp = Xtest[int(factor)] 
                new_row_left = int(self.decision_tree[int(row)][2]) # 1
                new_row_right = int(self.decision_tree[int(row)][3]) # 6
                if val_comp <= split_val:
                    row += new_row_left

                else:
                    row += new_row_right
        return ypred_array	  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    print("the secret clue is 'zzyzx'")  		  	   		  		 			  		 			     			  	 
