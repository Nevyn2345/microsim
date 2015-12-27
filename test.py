import matplotlib.pyplot as plt

import numpy as np

xx = np.array([100])
yy = np.array([100])
means = [xx.mean(), yy.mean()]
stds = [xx.std() / 3, yy.std() / 3]

corr = 0.8 

covs = [[stds[0]**2, stds[0]*stds[1]*corr], [stds[0]*stds[1]*corr, stds[1]**2]]

x = np.random.multivariate_normal(means, covs,1000).T

plt.subplot(111)
plt.scatter(x[0], x[1])
#plt2 = plt.imshow(x)

plt.show()
