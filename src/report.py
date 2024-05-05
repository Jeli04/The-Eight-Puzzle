import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Create dataframe

expansions_df = pd.DataFrame()

columns = ['Trivial', 'Very Easy', 'Easy', 'Doable', 'Oh Boy']

expansions_df['Test Case'] = columns
expansions_df['Number of Expansions (A* Misplaced Tile)'] = [0, 1, 2, 4, 100]

sns.lineplot(data=expansions_df,x='Test Case', y='Number of Expansions (A* Misplaced Tile)')
plt.show()