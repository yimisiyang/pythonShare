
'''
异或
0^0 = 0
0^1 = 1
1^0 = 1
1^1 = 0
'''

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 输入数据
    X = np.array([[1, 0, 0],
                  [1, 0, 1],
                  [1, 1, 0],
                  [1, 1, 1]])
    # 标签
    Y = np.array([[0],
                  [1],
                  [1],
                  [0]])

    # 权值初始化，3行1列，取值范围-1到1
    W = (np.random.random([3,1])-0.5)*2

    print(W)
    # 学习率设置
    lr = 0.11
    # 计算迭代次数
    n = 0
    # 神经网络输出
    O = 0

    def update():
        global X,Y,W,lr
        O = np.dot(X,W) # shape:(3,1)
        W_C = lr*(X.T.dot(Y-O))/int(X.shape[0])
        W = W + W_C

    for _ in range(50):
        # 更新权值
        update()
    # 正样本
    x1 = [0,1]
    y1 = [1,0]
    # 负样本
    x2 = [0,1]
    y2 = [0,1]

    # 计算分界线的斜率以及截距
    k = -W[1]/W[2]
    d = -W[0]/W[2]
    print('k=', k)
    print('d=', d)

    xdata = (-2, 3)

    plt.figure()
    plt.plot(xdata, xdata*k+d, 'r')
    plt.scatter(x1, y1, c='b')
    plt.scatter(x2, y2, c='y')
    plt.show()