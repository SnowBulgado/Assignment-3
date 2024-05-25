# text file
import numpy as np

array_4 = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])

np.savetxt('array_4.txt', array_4)

# Load
import numpy as np

loaded_array_4 = np.loadtxt('array_4.txt')
print(loaded_array_4)

