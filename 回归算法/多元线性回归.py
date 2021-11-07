from numpy import genfromtxt
from sklearn import linear_model

if __name__ == '__main__':
    # 读入数据
    data = genfromtxt(r"Delivery.csv", delimiter=',')
    print(data)
    # 切分数据
    x_data = data[:, :-1]
    y_data = data[:, -1]
    print(x_data)
    print(y_data)

    # 创建模型
    model = linear_model.LinearRegression()
    model.fit(x_data, y_data)

    # 系数
    print("coefficients:", model.coef_)
    # 截距
    print("intercept:", model.intercept_)

    # 测试
    x_test = [[102, 4]]
    predict = model.predict(x_test)
    print("predict:", predict)
    print("score", model.score(x_data, y_data))




