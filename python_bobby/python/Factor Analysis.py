import pandas as pd
from sklearn.preprocessing import StandardScaler
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity, calculate_kmo

# Data
data = {
    'rat_2023': [4.2, 9.5, 22.9, 7, 2, 5.6, 8.5, 22.2, 30, 27.7, 30.2, 24.7],
    'rat_2022': [4.6, 13, 24.1, 9.8, 1.9, 4.6, 9.3, 26.6, 23.8, 22, 21.4, 30.4],
    'org_waste': [0.1, 0.9, 1.8, 0.1, 0, 0.4, 0.3, 3.5, 1, 0.2, 0.6, 0.8],
    'delta': [4316, 3940, 12639, 7474, 6259, 8515, 16247, 11841, 12473, 16820, 3748, 27358],
    'sigma': [14.8, 14.8, 35.9, 18.4, 19.7, 16.6, 33.6, 34.8, 22.1, 42.84, 14.9, 69.1],
    'pop': [78390, 92445, 163141, 131151, 63600, 155614, 231983, 222129, 110458, 130440, 125771, 180206],
    'waste': [692.5, 776.7, 1448.5, 1080.3, 560.5, 1155.5, 1985.4, 1855.7, 1026.6, 1199.45, 1254.9, 1703.6]
}

df = pd.DataFrame(data)

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Step 2: Check Bartlett's Test and KMO
bartlett_test, p_value = calculate_bartlett_sphericity(scaled_data)
kmo_all, kmo_model = calculate_kmo(scaled_data)

print("Bartlett's Test:", bartlett_test, "P-value:", p_value)
print("KMO Score:", kmo_model)

# Proceed if KMO is acceptable (usually > 0.6)
if kmo_model > 0.6:
    # Step 5: Perform Factor Analysis
    fa = FactorAnalyzer(n_factors=3, rotation='varimax')
    fa.fit(scaled_data)

    # Step 6: Get factor loadings
    loadings = pd.DataFrame(fa.loadings_, index=df.columns)
    print("Factor Loadings:\n", loadings)
else:
    print("Data may not be suitable for factor analysis due to low KMO score.")
