import numpy as np

a=np.array([-0.000357, -0.00025996])
b=np.array([1,2,3,4,5])

print(b.transpose())
print(a*b.reshape(5,1))