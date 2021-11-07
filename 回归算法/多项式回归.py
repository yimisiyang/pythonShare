import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


if __name__ == '__main__':
    # 载入数据
    data = np.genfromtxt("job.csv", delimiter=",")
    x_data = data[1:, 1]
    y_data = data[1:, 2]
    plt.scatter(x_data, y_data)
    plt.show()

    x_data = x_data[:, np.newaxis]
    y_data = y_data[:, np.newaxis]

    # 创建并拟合模型,定义一个线性回归对象，线性回归
    model = LinearRegression()
    model.fit(x_data, y_data)

    # 画图（2）
    plt.plot(x_data, y_data, 'b.')
    plt.plot(x_data, model.predict(x_data), 'r')
    plt.show()

    # 定义多项式回归,degree的值可以调节多项式的特征
    poly_reg = PolynomialFeatures(degree=5)
    # 特征处理
    x_poly = poly_reg.fit_transform(x_data)
    # 定义回归模型
    lin_reg = LinearRegression()
    # 训练模型
    lin_reg.fit(x_poly, y_data)

    # 画图（3）
    plt.plot(x_data, y_data, 'b.')
    plt.plot(x_data, lin_reg.predict(poly_reg.fit_transform(x_data)), c='r')
    plt.title('Truth or Bluff (Polynomial Regression)')
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()

    # 画图(4)
    plt.plot(x_data, y_data, 'b.')
    x_test = np.linspace(1, 10, 100)
    x_test = x_test[:, np.newaxis]
    plt.plot(x_test, lin_reg.predict(poly_reg.fit_transform(x_test)), c='r')
    plt.title('Truth or Bluff (Polynomial Regression)')
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()


