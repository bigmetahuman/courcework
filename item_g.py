from libraries import *
df = pd.read_csv("data_cleaned.csv")
# Числовые признаки
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
# Гистограммы распределений
for column in numeric_columns:

    plt.figure(figsize=(8, 5))

    sns.histplot(df[column], bins=30, kde=True)

    plt.title(f'Распределение признака: {column}')

    plt.xlabel(column)

    plt.ylabel("Количество объектов")

    plt.grid(True)

    plt.show()


# Boxplot (выбросы)
for column in numeric_columns:

    plt.figure(figsize=(8, 4))

    sns.boxplot(x=df[column])

    plt.title(f'Boxplot признака: {column}')

    plt.show()