import sys
import numpy as np
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

#print "X="
#print X
#print "y="
#print y