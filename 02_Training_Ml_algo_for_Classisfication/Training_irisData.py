" Here we will train our iris data with perceptron "

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Perceptron import perceptron

# s= 'https://archive.ics.uci.edu/ml/machine-learning-datsets/iris/iris.data'

df= pd.read_csv(r"D:\Machine Learning With Pytorch & Sckit~learn\iris.data",
                header=None, encoding='utf+8')

# print(df.tail())
" now plot graphs to visulize "

# select setosa and versicolor
y= df.iloc[0:100,4].values  # selects data [0:100] and 4 says 4th column
y= np.where(y=='Iris-setosa',-1,1) # used for classification i.e if 0 then setosa elseif 1 then versicolor

# extract sepal and petal length
x= df.iloc[0:100, [0,2]].values 

# now plot data
plt.scatter(x[:50,0], x[:50,1],
            color='red', marker='o',label='Setosa')

plt.scatter(x[50:100, 0], x[50:100, 1],
            color='blue', marker='s', label='Versicolor')

plt.xlabel('Sepal lenghth [cm]')
plt.ylabel('Petal length [cm]')

plt.legend(loc='upper left')

# Now we will train our iris data  using perceptron
ppn = perceptron(eta=0.1, n_iter=10)
ppn.fit(x,y)

plt.figure()
plt.plot(range(1, len(ppn.errors_)+1),
         ppn.errors_, marker='o')

plt.xlabel('Epochs')
plt.ylabel('Number of updates')
plt.show()