import pandas as pd
import numpy as np

# Create dataframe

expansions_df = pd.DataFrame()

columns = ['Trivial', 'Very Easy', 'Easy', 'Doable', 'Oh Boy']

expansions_df['Test Case'] = columns
expansions_df['Number of Expansions (A* Misplaced Tile)'] = [0, 1, 2, 4, 5000]

print(expansions_df)