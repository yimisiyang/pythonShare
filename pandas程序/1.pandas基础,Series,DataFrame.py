import pandas as pd
import numpy as np


if __name__ == '__main__':
        # 创建一个series，索引为默认值
        s1 = pd.Series([4, 7, -5, 3])
        print("===============打印S1================")
        print(s1)
        # series的值
        print("===============打印S1.value================")
        print(s1.values)
        # series的索引
        print("===============打印S1.index================")
        print(s1.index)
        print("===============指定索引================")
        s2 = pd.Series([4.0, 6.5, -0.5, 4.2], index=['d', 'b', 'a', 'c'])
        print(s2)
        # 根据索引取值
        print("===============打印索引为a的值================")
        print(s2['a'])
        # 根据索引取值
        print("===============打印索引为a、b、c的值================")
        print(s2[['a', 'b', 'c']])
        print("===============判断索引是否在里面================")
        print('b' in s2)
        print('e' in s2)

        # Series可以看成是一个定长的有序字典
        dic1 = {'apple':5, 'pen':3, 'applepen':10}
        s3 = pd.Series(dic1)
        print(s3)

        # DataFrame
        print("================转换成dataframe===================")
        data = {'year':[2014,2015,2016,2017],
                'income':[10000,30000,50000,80000],
                'pay':[5000,20000,30000,30000]
        }
        df1 = pd.DataFrame(data)
        print(df1)
        print("================创建dataframe===================")
        df2 = pd.DataFrame(np.arange(12).reshape((3, 4)))
        print(df2)
        print("================创建dataframe 并指定行列标签===================")
        df3 = pd.DataFrame(np.arange(12).reshape((3, 4)), index=['a', 'c', 'b'], columns=[2, 33, 44, 5])
        print(df3)
        # 列
        print("================打印列标签===================")
        print(df1.columns)
        # 行

        print(df1.index)
        # 值
        print(df1.values)

        print(df1.describe())
        # 转置
        print(df1.T)

        df3.sort_index(axis=1) # 列排序

        df3.sort_index(axis=0) # 行排序

        df3.sort_values(by=44)


