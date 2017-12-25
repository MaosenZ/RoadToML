'''
Use matplotlib to display the dataset
'''

import kNN
from numpy import array
import matplotlib
import matplotlib.pyplot as plt

#read data
datingDataMat,datingLabels = kNN.file2matrix('datingTestSet.txt')
#draw
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
ax.axis([-2,25,-0.2,2.0])
plt.xlabel('Percentage of Time Spent Playing Video Games')
plt.ylabel('Liters of Ice Cream Consumed Per Week')
plt.show()
