import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # 从-1到1生成100个点
    x = np.linspace(-1, 1, 100)
    y = 2*x + 1
    plt.plot(x, y)
    plt.show()



