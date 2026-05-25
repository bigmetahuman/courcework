from libraries import *

df = pd.read_csv("data_cleaned.csv")

correlation = df.corr(numeric_only=True)

price_correlation = correlation['Price'].sort_values(ascending=False)
print("Корреляция признаков с ценой:\n")
print(price_correlation)

top_features = price_correlation[1:4]
print("\nТри признака с наибольшим влиянием:\n")
print(top_features)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Матрица корреляции")
plt.show()