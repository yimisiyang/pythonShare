import numpy as np


if __name__ == '__main__':

    arr1 = np.arange(12).reshape((3, 4))
    print(arr1)
    print("===============横向分割，分成2份===============")
    arr2, arr3 = np.split(arr1, 2, axis=1)
    print(arr2)
    print(arr3)

    print("=============纵向分割，分成3份===============")
    arr4, arr5, arr6 = np.split(arr1, 3, axis=0)
    print(arr4)
    print(arr5)
    print(arr6)

    print("=============横向分割，分成3份，不等分割===============")
    arr7, arr8, arr9 = np.array_split(arr1,3,axis=1)
    print(arr7)
    print(arr8)
    print(arr9)





