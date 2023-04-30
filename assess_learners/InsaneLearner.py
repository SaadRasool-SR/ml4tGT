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
import LinRegLearner as lrl
import BagLearner as bl 		  	   		  		 			  		 			     			  	   	   		  		 			  		 			     			  	  		  	   		  		 			  		 			     			  	 
class InsaneLearner(object):  		  	   		  		 			  		 			     			  	   	   		  		 			  		 			     			  	 
    def __init__(self, verbose=False):
        self.learner_ls = []
    def author(self):  		  	   		  		 			  		 			     			  	    		  		 			  		 			     			  	 
        return "srasool7"  # replace tb34 with your Georgia Tech username 
    def add_evidence(self, data_x, data_y):
        for bag in range(20):
            self.learner = bl.BagLearner(learner = lrl.LinRegLearner, kwargs = {}, bags = 20, boost = False, verbose = False)
            self.learner.add_evidence(data_x,data_y)
            self.learner_ls.append(self.learner)
    def query(self, test_array):
        ypred = 0
        for ln in self.learner_ls:
            ypred = ypred + ln.query(test_array)
        return ypred/len(self.learner_ls)		  		 			  		 			     			  	  		  	   		  		 			  		 			     			  	 	  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    print("the secret clue is 'zzyzx'")  		  	   		  		 			  		 			     			  	 
