# binary file
import numpy as np

array_1 = np.array([1, 2, 3, 4, 5])

np.save('array_1.npy', array_1)

# Load
import numpy as np

loaded_array_1 = np.load('array_1.npy')
print(loaded_array_1)


