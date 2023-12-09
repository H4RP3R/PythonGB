# Задача №57. Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data
# Посмотреть сколько в нем строк и столбцов
# Определить какой тип данных имеют столбцы


import pandas as pd


df = pd.read_csv(
    'https://gist.githubusercontent.com/H4RP3R/3ca02fb7457052842710b4a3d4ccd51f/raw/f2378e242967fb6ee4745731a34a478ac0d6c13f/gistfile1.txt')

print('rows: {}, columns {}'.format(*df.shape))
print(df.dtypes)
