from sklearn import datasets
import numpy as np

iris= datasets.load_iris()
x= iris.data[:,[2,3]]
y= iris.target

# print(f'class label:', np.unique(y))

# now we will split our data
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test= train_test_split(x,y,
                                                   test_size=0.3,
                                                    random_state=1,
                                                    stratify=y)

# # print(y_train.shape, y_train[:5])
# print(f'label count in y: ', np.bincount(y))
# print(f'label count in y_train:', np.bincount(y_train))
# print(f'label count in y_test:', np.bincount(y_test))

" now let's transform our data "
from sklearn.preprocessing import StandardScaler
sc= StandardScaler()

sc.fit(x_train)
x_train_std= sc.transform(x_train)
x_test_std= sc.transform(x_test)

" now fit our data to model "
from sklearn.linear_model import Perceptron
ppn= Perceptron(eta0= 0.1, random_state=1)
ppn.fit(x_train_std,y_train)

y_pred= ppn.predict(x_test_std)
print(f"misclassified example: %d" % (y_test != y_pred).sum())

# for accuracy
from sklearn.metrics import accuracy_score
print(f"Accuracy: %.3f" % accuracy_score(y_test, y_pred))