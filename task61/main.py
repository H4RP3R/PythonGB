# Задача №61 Определить какое максимальное и минимальное значение median_house_value
# Показать максимальное median_house_value, где median_income = 3.1250
# Узнать какая максимальная population в зоне минимального значения median_house_value


import pandas as pd


df = pd.read_csv(
    'https://gist.githubusercontent.com/H4RP3R/215e47955e2155d71bddfb7caa04691a/raw/d23fb92edc15d03e7107bf702611286b048d3be0/california_housing_test.csv'
)

print(df.median_house_value.min(), df.median_house_value.max())
print(df[df['median_income'] == 3.1250]['median_house_value'].max())
print(df[df['median_house_value'] == df['median_house_value'].min()]['population'].max())
