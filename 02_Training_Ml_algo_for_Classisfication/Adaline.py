" let's implement an Adaline and fit our iris data "

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

    def activation(self, x):
        ''' Compute linear activation '''
        return x

    def predict(self, x):
        ''' Return class label after unit step '''
        return np.where(self.activation(self.net_input(x)) >= 0.0, 1, -1)

        # for w_j in range(self.w_.shape[0]):
        #     self.w[w_j] += self.eta*(2.0 *(x[:,w_j]*errors)).mean()
        
        self.w_ += self.eta * 2.0 * x.T.dot(errors) / x.shape[0]


df= pd.read_csv(r"D:\Machine Learning With Pytorch & Sckit~learn\iris.data",
                header=None, encoding='utf+8')

# print(df.tail())
" now plot graphs to visulize "

# select setosa and versicolor
y= df.iloc[0:100,4].values  # selects data [0:100] and 4 says 4th column
y= np.where(y=='Iris-setosa',-1,1) # used for classification i.e if 0 then setosa elseif 1 then versicolor

# extract sepal and petal length
x= df.iloc[0:100, [0,2]].values 

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
ada1 = AdalineGD(n_iter=15, eta=0.1).fit(x, y)
ax[0].plot(range(1, len(ada1.loss_) + 1),
           np.log10(ada1.loss_), marker='o')
ax[0].set_xlabel('Epochs')
ax[0].set_ylabel('log(Mean squared error)')
ax[0].set_title('Adaline - Learning rate 0.1')
ada2 = AdalineGD(n_iter=15, eta=0.0001).fit(x, y)
ax[1].plot(range(1, len(ada2.loss_) + 1),
           ada2.loss_, marker='o')
ax[1].set_xlabel('Epochs')
ax[1].set_ylabel('Mean squared error')
ax[1].set_title('Adaline - Learning rate 0.0001')
plt.tight_layout()
plt.show()

" now let's standarlize our data "

x_std= np.copy(x)
x_std[:,0] = (x[:,0] - x[:,0].mean()) / x[:,0].std()
x_std[:,1] = (x[:,1] - x[:,1].mean()) / x[:,1].std()

" now we will create new instance and pass our standarlized data "
ada_gd = AdalineGD(n_iter=20, eta=0.01)
ada_gd.fit(x_std,y)

" now visulize "
from Training_irisData import plot_decision_regions

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))   

plt.sca(ax[0])                                               

plot_decision_regions(x_std, y, classifier=ada_gd)

ax[0].set_title('Adaline - Gradient descent')             
ax[0].set_xlabel('Sepal length [standardized]')             
ax[0].set_ylabel('Petal length [standardized]')             
ax[0].legend(loc='upper left')                             


ax[1].plot(
    range(1, len(ada_gd.loss_) + 1),
    ada_gd.loss_,
    marker='o'
)                                                          

ax[1].set_xlabel('Epochs')                                   
ax[1].set_ylabel('Mean squared error')                       
ax[1].set_title('Adaline - Gradient descent')                

plt.tight_layout()
plt.show()                                                    