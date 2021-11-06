import numpy as np


if __name__ == '__main__':
    # 生成3行2列0到1之间的随机数
    sample1 = np.random.random((3, 2))
    print("=============生成3行2列0到1之间的随机数==============")
    print(sample1)
    # 生成3行2列符合标准正态分布的随机数（0-1分布）
    sample2 = np.random.normal(size=(3, 2))
    print("=============生成3行2列符合标准正态分布的随机数（0-1分布）==============")
    print(sample2)
    # 生成3行2列从0到10的随机整数
    sample3 = np.random.randint(0, 10, size=(3, 2))
    print("=============生成3行2列从0到10的随机整数==============")
    print(sample3)
    print("=============sample1==============")
    print(sample1)
    # 求和
    print("=============求和==============")
    print(np.sum(sample1))
    # 求最小值
    print("=============求最小值==============")
    print(np.min(sample1))
    # 求最大值
    print("=============求最大值==============")
    print(np.max(sample1))
    # 对列求和
    print("=============对列求和==============")
    print(np.sum(sample1, axis=0))
    # 对行求和
    print("=============对行求和==============")
    print(np.sum(sample1, axis=1))
    # 求最小值的索引
    print("=============求最小值的索引==============")
    print(np.argmin(sample1))
    # 求最大值的索引
    print("=============求最大值的索引==============")
    print(np.argmax(sample1))
    # 求平均值
    print("=============求平均值==============")
    print(np.mean(sample1))
    # 求平均值
    print("=============求平均值==============")
    print(sample1.mean())
    # 求中位数
    print("============= sample1 求中位数==============")
    print(np.median(sample1))
    # 开方
    print("============= sample1 开方==============")
    print(np.sqrt(sample1))
    # 一维数组10个数，范围0-9之间
    sample4 = np.random.randint(0, 10, size=(1, 10))
    print("=============sample4==============")
    print(sample4)
    # 排序
    print("=============sample4 排序==============")
    print(np.sort(sample4))



