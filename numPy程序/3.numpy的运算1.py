import numpy as np


if __name__ == '__main__':
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr2 = np.array([[1, 1, 2], [2, 3, 3]])
    print(arr1)
    print(arr2)
    # 对应元素相加
    print(arr1 + arr2)
    # 对应元素相减
    print(arr1 - arr2)
    # 减
    print(arr1 * arr2)
    # 幂运算
    print(arr1 ** arr2)
    # 除法
    print(arr1 / arr2)
    # 取余
    print(arr1 % arr2)
    # 取整
    print(arr1 // arr2)
    # 所有的元素加2
    print(arr1+2)
    # 所有的元素乘以10
    print(arr1*10)
    # 判断哪些元素大于3
    arr3 = arr1 > 3
    print(arr3)
    # 3*5 单位阵
    arr4 = np.ones((3, 5))
    print(arr4)

    print(arr1)
    # 矩阵乘法   2*3  3*5
    np.dot(arr1, arr4)
    # 矩阵乘法
    arr1.dot(arr4)
    print(arr1)
    # 矩阵转置
    print(arr1.T)
    # 矩阵转置
    print(np.transpose(arr1))





