import pandas as pd
import numpy as np


if __name__ == '__main__':
    dates = np.arange(20170101,20170105)
    df1 = pd.DataFrame(np.arange(12).reshape((4,3)),index=dates,columns=['A','B','C'])
    df1

    df2 = pd.DataFrame(df1,index=dates,columns=['A','B','C','D','E'])
    df2

    s1 = pd.Series([3,4,6],index=dates[:3])
    s2 = pd.Series([32,5,2],index=dates[1:])
    df2['D'] = s1
    df2['E'] = s2
    df2

    df2.dropna(axis=0,how='any') #axis=[0,1] 0代表行，1代表列。how=['any','all'] any任意一个或多个 all全部

    df2.dropna(axis=1,how='any') #axis=[0,1] 0代表行，1代表列。how=['any','all'] any任意一个或多个 all全部

    df2.fillna(value=0)#把空值赋值为0

    df2.isnull()#查看空值

    np.any(df2.isnull())#只要有一个或多个空值就会返回true

    np.all(df2.isnull())#所有为空值才返回true

