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

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
def plot_decision_regions(X, y, classifier, test_idx=None,
                          resolution=0.02):
    # setup marker generator and color map
    markers = ('o', 's', '^', 'v', '<')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

# plot the decision surface

    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    lab = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    lab = lab.reshape(xx1.shape)
    plt.contourf(xx1, xx2, lab, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
# plot class examples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=x[y == cl, 0],
                    y=x[y == cl, 1],
                    alpha=0.8,
                    c=colors[idx],
                    marker=markers[idx],
                    label=f'Class {cl}',
                    edgecolor='black')
    # highlight test examples
    if test_idx:
    # plot all examples
            X_test, y_test = X[test_idx, :], y[test_idx]
            plt.scatter(X_test[:, 0], X_test[:, 1],
                        c='none', edgecolor='black', alpha=1.0,
                        linewidth=1, marker='o',
                        s=100, label='Test set')

# now plot 
x_combined_std= np.vstack((x_train_std, x_test_std))
y_combined= np.hstack((y_train, y_test))

plot_decision_regions(X= x_combined_std,
                      y=y_combined,
                      classifier=ppn,
                      test_idx= range(105,150))

plt.xlabel('Petal length [standarized]')
plt.ylabel('Petal Width [standarized]')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()