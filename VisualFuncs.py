import matplotlib.pyplot as plt
import numpy as np
from os import system
from sklearn import tree
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

"""
def VDR(cols, X, y, clf):
    x_min, x_max = X[:, cols[0]].min() - 1, X[:, cols[0]].max() + 1
    y_min, y_max = X[:, cols[1]].min() - 1, X[:, cols[1]].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max,0.01))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    fig_ = plt.figure()
    axis_ = fig_.add_subplot(111)
    axis_.scatter(X[:, cols[0]], X[:, cols[1]], c=y, s=20, edgecolor='k')
    axis_.contourf(xx, yy, Z, alpha=0.4)
    plt.legend(loc = 'lower right')
    plt.show()
"""

def Visual_Dec_Tree(X, trees):
    dotfile = open("dtree2.dot", 'w')
    tree.export_graphviz(trees, out_file = dotfile)
    dotfile.close()
    system('$ dot -Tpng dtree2.dot -o tree.png')

def ThreeD_VDR(cols, X, target, clf, Variable1 = 'Variable 1', Variable2 = 'Variable 2'):
    x_min, x_max = X[:, cols[0]].min() - 1, X[:, cols[0]].max() + 1
    y_min, y_max = X[:, cols[1]].min() - 1, X[:, cols[1]].max() + 1
    
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    
    onlyX = pd.DataFrame({Variable1: xx.ravel(), Variable2 : yy.ravel()})
    
    predicted = clf.predict(onlyX)
    
    fig = plt.figure( figsize = (6,6))
    ax = fig.add_subplot(111, projection = '3d')
    ax.scatter(X[:,cols[0]], X[:,cols[1]], target, c = 'blue', marker = 'o', alpha = 0.4)
    ax.plot_surface(xx, yy, predicted.reshape(xx.shape))
    plt.xlabel(Variable1)
    plt.ylabel(Variable2)
    plt.show()
    
    
def Visual_Logistic( X, y, clf):
    """
    2D Visualization function for logistic regression. Must input a DataFrame and a fitted classifier. Will ouput the decision boundary.
    """
    if type(X)=='pd.core.frame.DataFrame':
        X = X.values
    if type(y)=='pd.core.frame.DataFrame':
        y = y.values 
            
    x_min, x_max = X.iloc[:, 0].min() - 1, X.iloc[:, 0].max() + 1
    y_min, y_max = X.iloc[:, 1].min() - 1, X.iloc[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
    grid = np.c_[xx.ravel(), yy.ravel()]
    probs = clf.predict_proba(grid)[:,1].reshape(xx.shape)
    f, ax = plt.subplots(figsize=(8, 6))
    contour = ax.contourf(xx, yy, probs, 25, cmap="RdBu",
                      vmin=0, vmax=1)
    ax_c = f.colorbar(contour)
    ax_c.set_label("$P(y = 1)$")
    ax_c.set_ticks([0, .25, .5, .75, 1])

    ax.scatter(X.iloc[:,0], X.iloc[:, 1], c=y, s=50,
           cmap="RdBu", vmin=-.2, vmax=1.2,
           edgecolor="white", linewidth=1)
    plt.title('Decision Boundary')
    ax.set(xlabel= X.columns[0], ylabel=X.columns[1])
    
    
    
    
    
    
    
    
    
    

def VDR(X, y, classifier, test_idx=None, resolution=0.02):
   # setup marker generator and color map
   markers = ('s', 'x', 'o', '^', 'v')
   colors = ('purple', 'grey', 'lightgreen', 'blue', 'cyan')
   cmap = ListedColormap(colors[:len(np.unique(y))])

   # plot the decision surface
   x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
   x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
   xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
   np.arange(x2_min, x2_max, resolution))
   Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
   Z = Z.reshape(xx1.shape)
   plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
   plt.xlim(xx1.min(), xx1.max())
   plt.ylim(xx2.min(), xx2.max())

   # plot all samples
   X_test, y_test = X[test_idx, :], y[test_idx]
   for idx, cl in enumerate(np.unique(y)):
      plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
               alpha=0.8, c=cmap(idx),
               marker=markers[idx], label=cl)
   # highlight test samples
   if test_idx:
      X_test, y_test = X[test_idx, :], y[test_idx]
      plt.scatter(X_test[:, 0], X_test[:, 1], c='',
               alpha=1.0, linewidth=1, marker='o',
               s=55, label='test set')
   plt.legend(loc = 'upper left')
