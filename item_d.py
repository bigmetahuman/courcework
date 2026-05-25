from libraries import *

df = pd.read_csv("data_dirty.csv")

print("Количество пропусков по столбцам:\n")
print(df.isnull().sum())

wrong_area = df[df['Area'] < 0]

print("\nНекорректные значения площади:")
print(wrong_area)

wrong_price = df[df['Price'] == "error"]

print("\nНекорректные значения цены:")
print(wrong_price)

print("\nТипы данных:\n")
print(df.dtypes)