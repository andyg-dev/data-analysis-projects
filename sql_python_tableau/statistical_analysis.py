import pandas as pd
from scipy.stats import chi2_contingency
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load data
cancel_df = pd.read_csv('cancellations_by_operator.csv')
cluster_df = pd.read_csv('customer_behavior.csv')

### --- Chi-Square Test ---
contingency = pd.crosstab(cancel_df['operator'], cancel_df['status'])
chi2, p, dof, expected = chi2_contingency(contingency)

print("Chi-square:", chi2)
print("p-value:", p)
print("Conclusion:", "Significant difference in cancellation rates." if p < 0.05 else "No significant difference.")

### --- K-Means Clustering ---
features = cluster_df[['num_bookings', 'total_spent', 'avg_distance']].fillna(0)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=3, random_state=42)
cluster_df['segment'] = kmeans.fit_predict(scaled_features)

# Save for Tableau
cluster_df.to_csv('customer_segments.csv', index=False)

# Optional: Visualize
plt.scatter(cluster_df['total_spent'], cluster_df['avg_distance'], c=cluster_df['segment'], cmap='viridis')
plt.xlabel('Total Spent')
plt.ylabel('Average Distance')
plt.title('Customer Segments')
plt.show()
