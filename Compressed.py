# compressed file
import numpy as np

array_2 = np.array([10, 20, 30, 40, 50])
array_3 = np.array([[1, 2, 3], [4, 5, 6]])

np.savez_compressed('arrays_compressed.npz', array_2=array_2, array_3=array_3)

# Load
import numpy as np

data = np.load('arrays_compressed.npz')

loaded_array_2 = data['array_2']
loaded_array_3 = data['array_3']
print(loaded_array_2)
print(loaded_array_3)
