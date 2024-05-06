import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def get_nodeexpansion_plot():
    # Create dataframe
    expansions_df = pd.DataFrame()

    columns = ['Trivial', 'Very Easy', 'Easy', 'Doable', 'Oh Boy']

    expansions_df['Test Case'] = columns

    numExpansions = list(map(int, input().split()))

    expansions_df['A* Misplaced Tile'] = numExpansions
    #8508 expansions for oh boy

    numExpansions_1 = list(map(int, input().split()))
    expansions_df['A* Euclidean Distance'] = numExpansions_1

    numExpansions_2 = list(map(int, input().split()))
    expansions_df['Uniform Cost'] = numExpansions_2

    dfm = expansions_df.melt('Test Case', var_name='Search Algorithms', value_name='# of Expanded Nodes')

    sns.catplot(x="Test Case", y="# of Expanded Nodes", hue='Search Algorithms', data=dfm, kind='point')
    plt.show()

    expansions_df.to_csv('src/csvs/expansion_analysis.csv')

def get_nodedepth_plot():
    # Create dataframe
    depth_df = pd.DataFrame()

    columns = ['Trivial', 'Very Easy', 'Easy', 'Doable', 'Oh Boy']

    depth_df['Test Case'] = columns

    numDepth = list(map(int, input().split()))

    depth_df['A* Misplaced Tile'] = numDepth
    #8508 expansions for oh boy

    numDepth_1 = list(map(int, input().split()))
    depth_df['A* Euclidean Distance'] = numDepth_1

    numDepth_2 = list(map(int, input().split()))
    depth_df['Uniform Cost'] = numDepth_2

    dfm = depth_df.melt('Test Case', var_name='Search Algorithms', value_name='Depth of Search')

    sns.catplot(x="Test Case", y="Depth of Search", hue='Search Algorithms', data=dfm, kind='point')
    plt.show()

    depth_df.to_csv('src/csvs/depth_analysis.csv')

def get_nodeequeue_plot():
    # Create dataframe
    queue_df = pd.DataFrame()

    columns = ['Trivial', 'Very Easy', 'Easy', 'Doable', 'Oh Boy']

    queue_df['Test Case'] = columns

    numQueue = list(map(int, input().split()))

    queue_df['A* Misplaced Tile'] =  numQueue
    #8508 expansions for oh boy

    numQueue_1 = list(map(int, input().split()))
    queue_df['A* Euclidean Distance'] = numQueue_1

    numQueue_2 = list(map(int, input().split()))
    queue_df['Uniform Cost'] = numQueue_2

    dfm = queue_df.melt('Test Case', var_name='Search Algorithms', value_name='Maximum Queue Size')

    sns.catplot(x="Test Case", y="Maximum Queue Size", hue='Search Algorithms', data=dfm, kind='point')
    plt.show()

    queue_df.to_csv('src/csvs/queue_size_analysis.csv')

if __name__ == '__main__':
    get_nodeexpansion_plot()
    get_nodedepth_plot()
    get_nodeequeue_plot()
    print("Visuals have been generated....")