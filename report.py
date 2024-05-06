import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

# n_vals = ["3", "4", "5", "6"]
n_vals = ["3"]

for i in range(len(n_vals)):
    # Create dataframe
    expansions_df = pd.DataFrame()

    columns = ['Trivial', 'Very Easy', 'Easy', 'Doable', 'Oh Boy']

    expansions_df['Test Case'] = columns

    numExpansions = list(map(int, input().split()))

    expansions_df['Depth Size(A* Misplaced Tile)'] = numExpansions

    # expansions_df['Max Queue Size(A* Misplaced Tile)'] = numExpansions

    # expansions_df['Number of Expansions (A* Misplaced Tile)'] = numExpansions
    # 14600 expansions for oh boy
    # 9347 queue size
    # 22 depth

    # expansions= 1 2 3 4 14600
    # queue size = 0 3 4 7 9347
    # depth = 0 1 2 4 22

    fig = sns.lineplot(expansions_df, x='Test Case', y='Depth Size(A* Misplaced Tile)')
    plt.title(f"Depth Size vs. Test Cases (N = {n_vals[i]})")

    # fig = sns.lineplot(expansions_df, x='Test Case', y='Number of Expansions (A* Misplaced Tile)')
    # plt.title(f"Number of Expansions vs. Test Cases (N = {n_vals[i]})")

    plt.show()