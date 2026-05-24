from libraries import *


df = pd.read_csv("data.csv")


print("Количество квартир:", len(df))


# 1% пропусков в Area
area_missing = np.random.choice(df.index, size=int(len(df) * 0.01), replace=False)
df.loc[area_missing, 'Area'] = np.nan

# 1% пропусков в Kitchen area
kitchen_missing = np.random.choice(df.index, size=int(len(df) * 0.01), replace=False)
df.loc[kitchen_missing, 'Kitchen area'] = np.nan



# Некорректные значения цены
price_error = np.random.choice(df.index, size=int(len(df) * 0.01), replace=False)
df.loc[price_error, 'Price'] = random.randint(-1,-100)

# Отрицательная площадь
area_error = np.random.choice(df.index, size=int(len(df) * 0.005), replace=False)
df.loc[area_error, 'Area'] = random.randint(-1,-100)



print("\nКоличество пропусков:")
print(df.isnull().sum())

df.to_csv("data_dirty.csv", index=False)

print("\nФайл data_dirty.csv успешно создан")