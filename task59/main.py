# Задача №59. Проверить есть ли в файле пустые значения
# Показать median_house_value где median_income < 2
# Показать данные в первых 2 столбцах
# Выбрать данные где housing_median_age < 20 и median_house_value > 70000


import pandas as pd


df = pd.read_csv(
    'https://gist.githubusercontent.com/H4RP3R/3ca02fb7457052842710b4a3d4ccd51f/raw/f2378e242967fb6ee4745731a34a478ac0d6c13f/gistfile1.txt')

print(df.isna().sum(), end='\n\n')
print(df[df['median_income'] < 2]['median_house_value'],  end='\n\n')
print(df[df.columns[:2]],  end='\n\n')
print(df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)], end='\n\n')
