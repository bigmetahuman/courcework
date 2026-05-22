from libraries import *


# Загрузка очищенных данных


df = pd.read_csv("data_cleaned.csv")


# Корреляция числовых признаков


correlation = df.corr(numeric_only=True)


# Корреляция с ценой


price_correlation = correlation['Price'].sort_values(ascending=False)

print("Корреляция признаков с ценой:\n")

print(price_correlation)


# Топ 3 признака


top_features = price_correlation[1:4]

print("\nТри признака с наибольшим влиянием:\n")

print(top_features)


# Тепловая карта корреляции


plt.figure(figsize=(10, 8))

sns.heatmap(correlation, annot=True, cmap='coolwarm')

plt.title("Матрица корреляции")

plt.show()