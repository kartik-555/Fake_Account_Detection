# Fake Accounts Detection

This project aims to detect fake accounts on social media platforms using clustering algorithms such as K-Means and DBSCAN. The project involves data preprocessing, clustering, and identifying outliers.


### Data Preprocessing

The [fake_accounts.ipynb]notebook contains the data preprocessing steps, including loading the data, cleaning, and applying clustering algorithms.

### Clustering and Outlier Detection

1. **K-Means Clustering**:
    - Apply K-Means clustering to the data.
    - Calculate the Silhouette Score to evaluate the clustering quality.
    - Identify outliers based on the distance to the nearest cluster center.

2. **DBSCAN Clustering**:
    - Apply DBSCAN clustering to the data.
    - Identify outliers (DBSCAN labels outliers as -1).

### Combining Outliers

Combine the outliers detected by different clustering algorithms and remove duplicate entries based on `user_id`.

### Plotting

Use `matplotlib` and `seaborn` to visualize the clustering results and outliers.
