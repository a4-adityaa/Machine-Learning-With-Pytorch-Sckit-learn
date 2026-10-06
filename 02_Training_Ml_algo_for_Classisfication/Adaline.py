" let's implement an Adaline and fit our iris data "

import numpy as np
import pandas as pd

class AdalineGD:
    ''' ADAdaptive LInear neuraon classifier.
    
    parameters
    ----------
    
    eta: float
    ~ Learning rate (between 0.0-1.0)

    n_iter: int
    ~ Passes over the training dataset

    random_state: int
    ~ Random number generator seed for random weight initialization
    
    Attributes
    ----------
    
    w_: 1d-array
    ~ Weights after fitting
    
    b_: scalar
    ~ Bias unit after fitting
    
    loss_ : list 
    ~ Mean squared error loss function value in each epoch

    '''
    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, x, y):
        ''' Fit training data
        
        parameters
        ----------
        x: {array-like}, shape = [n_samples, n_features]
        ~ Training vectors, where n_samples is the number of samples and
          n_features is the number of features.
          
        y: array- like, shape = [n_exaples]
        target values
        
        Returns
        -------
        self: object
        
        '''
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=x.shape[1]) # dataset me total features
        self.b_ = np.float64(0.) # self.b_ = bias and self.w_ = weight
        self.loss_ = [] # har epochs me kitne misclassification hue unka record

        for i in range(self.n_iter):
            net_input = self.net_input(x)
            output = self.activation(net_input)
            errors = (y - output) # difference between actual and predicted
            self.w_ += self.eta * x.T.dot(errors) # update weights
            self.b_ += self.eta * errors.sum() # update bias
            loss = (errors**2).mean() # mean squared error
            self.loss_.append(loss) # append loss to list
        return self

    def net_input(self, x):
        ''' Calculate net input '''
        return np.dot(x, self.w_) + self.b_

    def activations(self, x):
        ''' Compute linear activation '''
        return x

    def predict(self, x):
        ''' Return class label after unit step '''
        return np.where(self.activation(self.net_input(x)) >= 0.0, 1, -1)
        