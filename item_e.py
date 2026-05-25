from libraries import *

df = pd.read_csv("data_dirty.csv")

df['Price'] = df['Price'].replace("error", np.nan)
df['Price'] = pd.to_numeric(df['Price'])
df.loc[df['Area'] < 0, 'Area'] = np.nan

numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
categorical_columns = df.select_dtypes(include=['object']).columns

# Заполнение числовых
for column in numeric_columns:
    df[column] = df[column].fillna(df[column].mean())

# Заполнение категориальных
for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])

# Проверка после очистки
print("Количество пропусков после очистки:\n")
print(df.isnull().sum())
# Проверка некорректных данных
print("\nОтрицательные площади:")
print(df[df['Area'] < 0])

print("\nНекорректные цены:")
print(df[df['Price'] == "error"])

df.to_csv("data_cleaned.csv", index=False)
print("\nФайл data_cleaned.csv успешно создан")