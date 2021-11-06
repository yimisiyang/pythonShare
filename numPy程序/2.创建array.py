import numpy as np


if __name__ == '__main__':
    a = np.array([1, 2, 3], dtype=np.int32)
    print(a.dtype)
    # 2维矩阵
    b = np.array([[1, 2, 3],  [4, 5, 6]], dtype=np.int32)
    print(b)
    # 生成2行3列全为0的矩阵
    zero = np.zeros((2, 3))
    print(zero)
    # 生成3行4列全为1的矩阵
    one = np.ones((3, 4))
    print(one)
    # 生成3行2列全都接近于0（不等于0）的矩阵
    empty = np.empty((3, 2))
    print(empty)
    # 0-9 一维数组
    c = np.arange(10)
    print(c)
    # 4-11 一维数组
    d = np.arange(4, 12)
    print(d)
    # 1-19 步长为3 一维数组
    g = np.arange(1, 20, 3)
    print(g)
    # 重新定义矩阵的形状
    h = np.arange(8).reshape(4, 2)
    print(h)






