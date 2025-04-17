import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create user-item rating matrix
data = {
    'Item1': [4, 3, 5, np.nan, 4],
    'Item2': [3, np.nan, 4, 5, 3],
    'Item3': [2, 1, 3, 2, np.nan],
    'Item4': [4, 5, np.nan, 4, 5],
    'TargetItem': [2, 3, 2, 3, 3]
}

ratings_df = pd.DataFrame(data, index=['User1', 'User2', 'User3', 'User4', 'User5'])

# Compute original average rating of the target item
original_avg = ratings_df['TargetItem'].mean()
print(f"Target Item Average Rating Before Attack: {original_avg:.2f}")

# Add 5 fake users with high ratings for the target item
for i in range(5):
    ratings_df.loc[f'FakeUser_{i+1}'] = [3, 3, 3, 3, 5]

# Compute new average rating after attack
after_attack_avg = ratings_df['TargetItem'].mean()
print(f"Target Item Average Rating After Attack: {after_attack_avg:.2f}")

# Simple Heatmap
sns.heatmap(ratings_df.fillna(0), cmap="gray", cbar=False)
plt.show()
