import pandas as pd
import numpy as np

if __name__ == '__main__':
    df1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns=['a','b','c','d'])
    df2 = pd.DataFrame(np.arange(12,24).reshape((3,4)),columns=['a','b','c','d'])
    df3 = pd.DataFrame(np.arange(24,36).reshape((3,4)),columns=['a','b','c','d'])
    print(df1)
    print(df2)
    print(df3)

    df4 = pd.concat([df1,df2,df3],axis=0)#纵向合并
    print(df4)

    df4 = pd.concat([df1,df2,df3],axis=0,ignore_index=True)#纵向合并，不考虑原来的index
    print(df4)

    df5 = pd.concat([df1,df2,df3],axis=1)#横向合并
    print(df5)

    df1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns=['a','b','c','f'])
    df2 = pd.DataFrame(np.arange(12,24).reshape((3,4)),columns=['a','c','d','e'])
    print(df1)
    print(df2)

    df6 = pd.concat([df1,df2],join='outer',ignore_index=True)#合并两个表，缺少的部分填充NaN
    print(df6)

    df7 = pd.concat([df1,df2],join='inner',ignore_index=True)#合并两个表，缺少的部分去掉
    print(df7)

    df1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns=['a','b','c','f'])
    df2 = pd.DataFrame(np.arange(12,24).reshape((4,3)),columns=['a','c','d'])
    print(df1)
    print(df2)

    df8 = pd.concat([df1,df2],axis=1,join_axes=[df1.index])#横向合并，index使用df1的index
    print(df8)

    df8 = pd.concat([df1,df2],axis=1)#横向合并
    print(df8)

