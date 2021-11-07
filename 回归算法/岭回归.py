
import numpy as np
from numpy import genfromtxt
from sklearn import linear_model
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 读入数据
    data = genfromtxt(r"longley.csv", delimiter=',')
    print(data)

    # 切分数据
    x_data = data[1:, 2:]
    y_data = data[1:, 1]
    print(x_data)
    print(y_data)

    # 创建模型
    # 生成50个值
    alphas_to_test = np.linspace(0.001, 1)
    # 创建模型，保存误差值
    model = linear_model.RidgeCV(alphas=alphas_to_test, store_cv_values=True)
    model.fit(x_data, y_data)

    # 岭系数
    print(model.alpha_)
    # loss值
    print(model.cv_values_.shape)

    # 画图
    # 岭系数跟loss值的关系
    plt.plot(alphas_to_test, model.cv_values_.mean(axis=0))
    # 选取的岭系数值的位置
    plt.plot(model.alpha_, min(model.cv_values_.mean(axis=0)), 'ro')
    plt.show()

    print(model.predict(x_data[2, np.newaxis]))