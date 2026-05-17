import pandas as pd
# Импорт данных из CSV файла
df = pd.read_csv("data_dirty.csv")

# Вывод первых 5 строк таблицы
print(df.head())