import sys
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1/(1+np.exp(-z));

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

#print X
#print y

plt.title("Logistical regression")
for i in range(len(y)):
    if y[i] == 0: plt.plot(X[i,1], X[i,2], 'bo')
    if y[i] == 1: plt.plot(X[i,1], X[i,2], 'rx')
#plt.show()
