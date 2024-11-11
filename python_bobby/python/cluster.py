import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

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

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

inertia = []
for k in range(1, 10):
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

# Plotting the Elbow graph
plt.figure(figsize=(8, 5))
plt.plot(range(1, 10), inertia, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal Clusters')
plt.show()

# Apply K-means clustering with an optimal number of clusters (e.g., 3)
kmeans = KMeans(n_clusters=3, random_state=0)
df['cluster'] = kmeans.fit_predict(scaled_data)

# Display the resulting clusters
print(df[['rat_2023', 'rat_2022', 'org_waste', 'delta', 'sigma', 'pop', 'waste', 'cluster']])
