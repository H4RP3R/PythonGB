# Задача №57. Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data
# Посмотреть сколько в нем строк и столбцов
# Определить какой тип данных имеют столбцы


import pandas as pd


df = pd.read_csv(
    'https://gist.githubusercontent.com/H4RP3R/215e47955e2155d71bddfb7caa04691a/raw/d23fb92edc15d03e7107bf702611286b048d3be0/california_housing_test.csv'
    )

print('rows: {}, columns {}'.format(*df.shape))
print(df.dtypes)
