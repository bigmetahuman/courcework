from libraries import *
#errors
#some categories dont have errors because of another item

df = pd.read_csv("data_dirty.csv")

print("Количество пропусков по столбцам:\n")
print(df.isnull().sum())

# Отрицательная площадь
wrong_area = df[df['Area'] < 0]

print("\nНекорректные значения площади:")
print(wrong_area)

# Некорректные значения цены
wrong_price = df[df['Price'] == "error"]

print("\nНекорректные значения цены:")
print(wrong_price)

# Общая информация

print("\nТипы данных:\n")
print(df.dtypes)