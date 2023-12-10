# Задача №61 Определить какое максимальное и минимальное значение median_house_value
# Показать максимальное median_house_value, где median_income = 3.1250
# Узнать какая максимальная population в зоне минимального значения median_house_value


import pandas as pd


df = pd.read_csv(
    'https://gist.githubusercontent.com/H4RP3R/3ca02fb7457052842710b4a3d4ccd51f/raw/f2378e242967fb6ee4745731a34a478ac0d6c13f/gistfile1.txt')

print(df.median_house_value.min(), df.median_house_value.max())
print(df[df['median_income'] == 3.1250]['median_house_value'].max())
print(df[df['median_house_value'] == df['median_house_value'].min()]['population'].max())
