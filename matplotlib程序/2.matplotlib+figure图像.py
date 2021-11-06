import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    # [-1,1] 之间100个数，间隔相同
    x = np.linspace(-1, 1, 100)
    y1 = 2*x + 1
    y2 = x**2
    plt.figure()
    plt.plot(x, y1)
    # 指定图的大小
    plt.figure(figsize=(8, 5))
    plt.plot(x, y2)
    plt.show()

    # 虚线
    plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
    # 实线
    plt.plot(x, y2, color='blue', linewidth=5.0, linestyle='-')
    plt.show()




