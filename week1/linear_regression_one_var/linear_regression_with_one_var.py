import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize

def J(thetas):
    sum = 0
    for i in range(m):
        sum += (thetas[0] + thetas[1]*x[i] - y[i])**2
    return (1/float(2*m))*sum

if len(sys.argv) == 1:
    print "You have to pass filename as argument"
    exit() 
(scriptname, filename) = sys.argv

frame = pd.read_csv(filename, header=0, sep=',')
xlabel = frame.columns.values[0]
ylabel = frame.columns.values[1]
x = list(frame[xlabel])
y = list(frame[ylabel])
m = len(x)

(theta0, theta1) = optimize.minimize(J, [0,0]).x
space = np.arange(min(x),max(x),0.1)

plt.plot(x, y, 'bo')
plt.plot(space, [theta0 + theta1*x0 for x0 in space])
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title("Linear regression with one variable")
plt.show()