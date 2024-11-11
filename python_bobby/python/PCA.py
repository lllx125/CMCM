import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

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

# Exclude target variables (rat_2023 and rat_2022) for PCA
independent_vars = df.drop(columns=['rat_2023', 'rat_2022'])

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(independent_vars)

# Perform PCA
pca = PCA()
pca.fit(scaled_data)

# Explained variance by each component
explained_variance = pca.explained_variance_ratio_

# Plot explained variance to choose the number of components
plt.figure(figsize=(8, 5))
plt.plot(range(1, len(explained_variance) + 1), explained_variance, marker='o')
plt.xlabel('Principal Component')
plt.ylabel('Explained Variance Ratio')
plt.title('Explained Variance by Principal Components')
plt.show()

# Select the number of components based on the elbow method or explained variance
n_components = 2  # Adjust this based on the plot, if necessary

# Apply PCA with the chosen number of components
pca = PCA(n_components=n_components)
principal_components = pca.fit_transform(scaled_data)

# Display principal components and loadings
loadings = pd.DataFrame(pca.components_.T, index=independent_vars.columns, columns=[f'PC{i+1}' for i in range(n_components)])
principal_components_df = pd.DataFrame(principal_components, columns=[f'PC{i+1}' for i in range(n_components)])

print("Explained Variance by Each Component:", explained_variance[:n_components])
print("Principal Components:\n", principal_components_df)
print("Loadings (Contribution of Each Variable to Each Principal Component):\n", loadings)
