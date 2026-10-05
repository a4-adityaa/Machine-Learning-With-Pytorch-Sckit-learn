import numpy as np

class perceptron:
    ''' Perceptron classifier

    Parameters
    ----------
    eta : float
    ~ learning rate (between 0.0-1.0)
    
    n_iter: int
    ~ Passes over the training datasets

    random_state: int
    ~ Random number generator seed for random weight initialization

    Attribute
    ----------

    w_: 1d-array
    ~ Weights after fitting

    b_: scalar
    ~ Bias unit after fitting

    errors_: list
    ~ Number of misclassifications (updates) in each epoch

    '''
    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, x,y):
        ''' Fit training data

        Parameters
        ----------
        x: {array-like}, shape = [n_samples, n_features]
        ~ Training vectors, where n_samples is the number of samples and
          n_features is the number of features.

        y: array-like, shape = [n_samples]
        ~ Target values.

        Returns
        -------
        self: object

        '''
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=x.shape[1]) # dataset me total features
        self.b_ = np.float64(0.) # self.b_ = bias and self.w_ = weight
        self.errors_ = []  # har epochs me kitne misclassification hue unka record

        for _ in range(self.n_iter): # har epoch ke liye training repeat krta hai
            errors = 0 # accumulates errors
            for xi, target in zip(x,y): # har input sample ko uske actual label ke sath pair karta hai
                update = self.eta * (target - self.predict(xi)) # current weights se prediction krta hai
                self.w_ += update * xi
                self.b_ += update
                errors += int(update != 0.0)
            self.errors_.append(errors) # har epochs ke error store karta hai
        return self

    def net_input(self, x):
        ''' Calculate net input '''
        return np.dot(x, self.w_) + self.b_

    def predict(self, x):
        ''' Return class label after unit step '''
        return np.where(self.net_input(x) >= 0.0, 1, -1)

if __name__ == "__main__":

    x= np.array([[2,3],[3,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,9]])
    y= np.array([0,0,0,0,1,1,1,1])

    ppn= perceptron(eta=0.1,
                    n_iter=10,
                    random_state=1)

    ppn.fit(x,y)

    " now let's check result "

    print("Weight: ", ppn.w_)
    print("Bias: ", ppn.b_)
    print("Errors: ", ppn.errors_)

    y_pred= ppn.predict(x)
    print("Prediction: ", y_pred)
    print("Actual: ", y)