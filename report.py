import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

n_vals = ["3", "4", "5", "6"]

for i in range(len(n_vals)):
    # Create dataframe
    expansions_df = pd.DataFrame()

    columns = ['Trivial', 'Very Easy', 'Easy', 'Doable', 'Oh Boy']

    expansions_df['Test Case'] = columns

    numExpansions = list(map(int, input().split()))

    expansions_df['Number of Expansions (A* Misplaced Tile)'] = numExpansions
    #8508 expansions for oh boy

    fig = sns.lineplot(expansions_df, x='Test Case', y='Number of Expansions (A* Misplaced Tile)')
    plt.title(f"Number of Expansions vs. Test Cases (N = {n_vals[i]})")

    plt.show()