# Fake Accounts Detection

This project aims to detect fake accounts on social media platforms using clustering algorithms such as K-Means and DBSCAN. The project involves data preprocessing, clustering, and identifying outliers.

## Project Structure

fake_accounts/ ├── Data/ │ ├── instagram_data.csv │ └── ... ├── preprocess.ipynb ├── get_data.py ├── requirements.txt ├── .gitignore └── README.md

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/fake_accounts.git
    cd fake_accounts
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Data Preprocessing

The [preprocess.ipynb](http://_vscodecontentref_/3) notebook contains the data preprocessing steps, including loading the data, cleaning, and applying clustering algorithms.

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

## Example Code

### Data Preprocessing and Clustering

```python
import pandas as pd
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("Data/instagram_data.csv")

# Data cleaning and preprocessing steps...

# Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Calculate Silhouette Score for K-Means
silhouette_avg_kmeans = silhouette_score(X_scaled, df['cluster'])
print(f'Silhouette Score for K-Means: {silhouette_avg_kmeans}')

# Apply DBSCAN
dbscan = DBSCAN(eps=1.5, min_samples=5)
df['cluster'] = dbscan.fit_predict(X_scaled)

# Calculate Silhouette Score for DBSCAN
filtered_df = df[df['cluster'] != -1]
filtered_X_scaled = X_scaled[filtered_df.index]
silhouette_avg_dbscan = silhouette_score(filtered_X_scaled, filtered_df['cluster'])
print(f'Silhouette Score for DBSCAN: {silhouette_avg_dbscan}')

# Plotting results...