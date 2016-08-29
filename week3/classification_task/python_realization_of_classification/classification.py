import sys
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1/(1+np.exp(-z));
def cost_function(theta, X, y):
    m = len(y)
    J = (-y.T*np.log(sigmoid(X*theta))-(1-y).T*np.log(1-sigmoid(X*theta)))/m
    grad = (X.T*(sigmoid(X*theta)-y))/m
    return (J, grad)

if len(sys.argv) == 1:
    print "You have to pass filename as argument"
    exit() 
(scriptname, filename) = sys.argv

data = [];
file = open(filename, 'r')
for line in file:
    row = [float(num) for num in line.split(',')]
    row.insert(0, 1.0)
    data.append(row)
data = np.array(data)

X = np.array([sample[:-1] for sample in data])
y = np.array([sample[-1] for sample in data])
m = len(y)

plt.title("Logistical regression")
for i in range(len(y)):
    if y[i] == 0: plt.plot(X[i,1], X[i,2], 'bo')
    if y[i] == 1: plt.plot(X[i,1], X[i,2], 'rx')
#plt.show()

X = np.matrix(X)
y = np.matrix(y).T
theta = np.zeros((X.shape[1], 1)) 
cost = 0
#print X
#print y
#print cost_function(theta, X, y)