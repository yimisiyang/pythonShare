import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    x = np.linspace(-3, 3, 100)
    y1 = 2 * x + 1
    y2 = x ** 2
    # xy范围
    plt.xlim((-1, 2))
    # xy描述
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
    plt.plot(x, y2, color='blue', linewidth=5.0, linestyle='-')
    plt.show()

