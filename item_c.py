from libraries import *
df = pd.read_csv("data_dirty.csv")

print("Количество объектов:", len(df))

numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
categorical_columns = df.select_dtypes(include=['object']).columns

print("\nЧисловые параметры:")
print(list(numeric_columns))

print("\nКатегориальные параметры:")
print(list(categorical_columns))