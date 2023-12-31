# Дан файл california_housing_train.csv.
# Найти максимальное значение переменной "households" в зоне минимального значения переменной "population" и
# сохраните это значение в переменную max_households_in_min_population. Используйте модуль pandas.


# Введите ваше решение ниже
# Введите ваше решение ниже
import pandas as pd


df = pd.read_csv('california_housing_train.csv')
max_households_in_min_population = df[df['population']==df['population'].min()]['households'].max()