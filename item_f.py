from libraries import *

df = pd.read_csv("data_cleaned.csv")
# Числовые признаки
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns

print("Описательные статистики:\n")
for column in numeric_columns:

    print(f"\n===== {column} =====")

    print("Среднее значение:", df[column].mean())

    print("Медиана:", df[column].median())

    print("Минимальное значение:", df[column].min())

    print("Максимальное значение:", df[column].max())

    print("Дисперсия:", df[column].var())

    print("Стандартное отклонение:", df[column].std())

print("\nОбщая статистика:\n")
print(df[numeric_columns].describe())