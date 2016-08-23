import sys
import numpy as np
import numpy.linalg 
import matplotlib.pyplot as plt

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
theta = np.dot(np.dot(numpy.linalg.pinv(np.dot(np.transpose(X), X)), np.transpose(X)), y)

print "Design matrix X:"
print X
print "Vector y:"
print y
print "Theta vector evaluated via normal equation:"
print theta
