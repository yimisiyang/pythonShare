import numpy as np


if __name__ == '__main__':

    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    print("==================垂直合并===================")
    arr3 = np.vstack((arr1, arr2))
    print(arr3)
    print("==================arr3 的形状===================")
    print(arr3.shape)
    print("==================水平合并===================")
    arr4 = np.hstack((arr1, arr2))
    print(arr4)
    print("==================arr4 的形状===================")
    print(arr4.shape)






