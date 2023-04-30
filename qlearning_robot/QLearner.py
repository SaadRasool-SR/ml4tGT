""""""  		  	   		  		 			  		 			     			  	 
"""  		  	   		  		 			  		 			     			  	 
Template for implementing QLearner  (c) 2015 Tucker Balch  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
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
  		  	   		  		 			  		 			     			  	 
import random as rand  		  	   		  		 			  		 			     			  	 	  	   		  		 			  		 			     			  	 
import numpy as np  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
class QLearner(object):  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    This is a Q learner object.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    :param num_states: The number of states to consider.  		  	   		  		 			  		 			     			  	 
    :type num_states: int  		  	   		  		 			  		 			     			  	 
    :param num_actions: The number of actions available..  		  	   		  		 			  		 			     			  	 
    :type num_actions: int  		  	   		  		 			  		 			     			  	 
    :param alpha: The learning rate used in the update rule. Should range between 0.0 and 1.0 with 0.2 as a typical value.  		  	   		  		 			  		 			     			  	 
    :type alpha: float  		  	   		  		 			  		 			     			  	 
    :param gamma: The discount rate used in the update rule. Should range between 0.0 and 1.0 with 0.9 as a typical value.  		  	   		  		 			  		 			     			  	 
    :type gamma: float  		  	   		  		 			  		 			     			  	 
    :param rar: Random action rate: the probability of selecting a random action at each step. Should range between 0.0 (no random actions) to 1.0 (always random action) with 0.5 as a typical value.  		  	   		  		 			  		 			     			  	 
    :type rar: float  		  	   		  		 			  		 			     			  	 
    :param radr: Random action decay rate, after each update, rar = rar * radr. Ranges between 0.0 (immediate decay to 0) and 1.0 (no decay). Typically 0.99.  		  	   		  		 			  		 			     			  	 
    :type radr: float  		  	   		  		 			  		 			     			  	 
    :param dyna: The number of dyna updates for each regular update. When Dyna is used, 200 is a typical value.  		  	   		  		 			  		 			     			  	 
    :type dyna: int  		  	   		  		 			  		 			     			  	 
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		  		 			  		 			     			  	 
    :type verbose: bool  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    def __init__(	  	   		  		 			  		 			     			  	 
        self,  		  	   		  		 			  		 			     			  	 
        num_states=100,   		  	   		  		 			  		 			     			  	 
        num_actions=4,  		  	   		  		 			  		 			     			  	 
        alpha=0.2,  # learning rate		  	   		  		 			  		 			     			  	 
        gamma=0.9, # discount rate 		  	   		  		 			  		 			     			  	 
        rar=0.5,  # random step should decay over time 		  	   		  		 			  		 			     			  	 
        radr=0.99, # action decay rate, once a policy is developed robot should never take a random step  		  	   		  		 			  		 			     			  	 
        dyna=0,  		  	   		  		 			  		 			     			  	 
        verbose=False, 	  	   		  		 			  		 			     			  	 
    ):  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        Constructor method  		  	   		  		 			  		 			     			  	 
        """
        self.num_states = num_states
        self.num_actions = num_actions
        self.alpha = alpha	  	   		  		 			  		 			     			  	 
        self.verbose = verbose
        self.gamma = gamma
        self.rar = rar  		  	   		  		 			  		 			     			  	 
        self.radr = radr
        self.dyna = dyna  		  	   		  		 			  		 			     			  	 
        self.s = 0  		  	   		  		 			  		 			     			  	 
        self.a = 0
        self.q_table = np.zeros((num_states, num_actions))
        self.T = np.full((self.num_states, self.num_actions, self.num_states), 0.00001) # transition matrix
        self.R = np.zeros((num_states, num_actions)) # reward matrix  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    def querysetstate(self, s):  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        Update the state without updating the Q-table  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
        :param s: The new state  		  	   		  		 			  		 			     			  	 
        :type s: int  		  	   		  		 			  		 			     			  	 
        :return: The selected action  		  	   		  		 			  		 			     			  	 
        :rtype: int  		  	   		  		 			  		 			     			  	 
        """
        # remeber the first day  		  	   		  		 			  		 			     			  	 
        action = rand.randint(0, self.num_actions - 1)
        self.s = s # keeing track of the state
        if rand.uniform(0,1) <= self.rar: # rar is randon action 
            action = rand.randint(0, self.num_actions - 1)
        self.a = action # keeping track of action

        #action = rand.randint(0, self.num_actions - 1)  		  	   		  		 			  		 			     			  	 
        if self.verbose:  		  	   		  		 			  		 			     			  	 
            print(f"s = {s}, a = {action}")  		  	   		  		 			  		 			     			  	 

        return action

    def robot_action(self, s_prime):
        
        # exploration
        if rand.uniform(0,1) <= self.rar: # rar is randon action 
            action = rand.randint(0, self.num_actions - 1)
        else:
            action = np.argmax(self.q_table[s_prime, :]) # gets maxs action for the state
        
        return action
    
    def t_c_update(self, s_prime):
        self.T[self.s, self.a, s_prime] += 1


    def r_update(self, r):
        self.R[self.s,self.a] = (1 - self.alpha) * self.R[self.s, self.a] + (self.alpha * r)
    
    def update_q_table(self, s_prime, r, action):
        # s_prime =  new state
        # action = new action 
        # self.s = old state
        # self.a = ald action

        old_value = self.q_table[self.s, self.a]
        new_best_estimate = self.alpha * (r + self.gamma *self.q_table[s_prime,np.argmax(self.q_table[s_prime, :])])
        self.q_table[self.s,self.a] = (1 - self.alpha) * old_value + new_best_estimate

        if self.verbose:
            print(f"old_value is {old_value}")
            print(f"new_best estimate is {new_best_estimate}")
            print(f"q_table is {self.q_table}")


    def dyna_q_algorithm(self):
        prob = self.T / np.sum(self.T , axis = 0) # gets the prob

        for i in range(self.dyna):
            state = rand.randint(0,self.num_states - 1)
            action = rand.randint(0, self.num_actions - 1)
            state_prime = np.argmax(prob[state,action, :])
            reward = self.R[state,action]
            self.s = state
            self.a = action
            self.update_q_table(state_prime, reward, action)


  		  	   		  		 			  		 			     			  	 
    def query(self, s_prime, r):  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        Update the Q table and return an action  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
        :param s_prime: The new state  		  	   		  		 			  		 			     			  	 
        :type s_prime: int  		  	   		  		 			  		 			     			  	 
        :param r: The immediate reward  		  	   		  		 			  		 			     			  	 
        :type r: float  		  	   		  		 			  		 			     			  	 
        :return: The selected action  		  	   		  		 			  		 			     			  	 
        :rtype: int  		  	   		  		 			  		 			     			  	 
        """
        # update the q_table  the equtation
        # remember previous s and a 
        # decide if you should take a rondom action rar
        # update rar 
        # action should i take = q table row s prime new state and look at each action and choose the highest value argmax  		  	   		  		 			  		 			     			  	 
        # call random number  0 - 1 and if less than rar should take the random action 
    

        action  = self.robot_action(s_prime)
        
        self.update_q_table(s_prime, r, action)
        if self.dyna != 0:
            self.t_c_update(s_prime)
            self.r_update(r)
            self.dyna_q_algorithm()

        self.rar = self.rar * self.radr # decaying randomness
        self.s = s_prime
        self.a = action
        if self.verbose:
            print(f"q_table is {self.q_table}")    		  	   		  		 			  		 			     			  	 
            print(f"s = {s_prime}, a = {action}, r={r}")  	

        return self.a  	# action to take


    def author(self): 
        return 'srasool7'	  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    print("Remember Q from Star Trek? Well, this isn't him")  		  	   		  		 			  		 			     			  	 
