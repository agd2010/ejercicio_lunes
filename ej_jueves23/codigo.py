import numpy as np

arr1 = np.random.randint(1,101, size = (1,6))
arr2 = np.random.randint(1,111, size = (1,6))

arr3 = arr1 + arr2

# print(arr1)
# print(arr2)
# print(arr3)
# print(arr2 > arr1)

#arr1_rs = arr1.reshape(2,3)
#arr2_rs = arr2.reshape(2,3)
#print(arr1_rs)
#print(arr2_rs)

#print(arr1_rs + arr2_rs)

# [[[ 1 2 3] [ 4 5 6]]
#
#[[ 7 8 9] [10 11 12]]]

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9],[10, 11, 12]]])

prueba = arr3[0,0]

print(f"{arr3[0,0,0]} {arr3[0,0,1]} {arr3[0,0,2]}")
print(f"{arr3[0,1,0]} {arr3[0,1,1]} {arr3[0,1,2]}")

