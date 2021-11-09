
import pandas as pd
if __name__ == '__main__':
    file = pd.read_csv('people2.csv', encoding='utf8')
    print(file)

    file.to_csv('people2.csv')

