
from scipy import stats
# ── scipy.stats метод 1: pearsonr — корреляция Пирсона с p-value ──────────────
print("\nКорреляция Пирсона с p-value (scipy.stats.pearsonr):\n")
num_cols = [c for c in df.select_dtypes(include='number').columns if c != 'Price']
for col in num_cols:
    valid = df[['Price', col]].dropna()
    r, p = stats.pearsonr(valid['Price'], valid[col])
    print(f"  {col}: r = {r:.4f},  p-value = {p:.4f}")

# ── scipy.stats метод 2: spearmanr — корреляция Спирмена ─────────────────────
print("\nКорреляция Спирмена (scipy.stats.spearmanr):\n")
for col in num_cols:
    valid = df[['Price', col]].dropna()
    rho, p = stats.spearmanr(valid['Price'], valid[col])
    print(f"  {col}: rho = {rho:.4f},  p-value = {p:.4f}")
