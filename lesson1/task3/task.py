import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# TODO return a dataframe with the number of games per genre grouped by platform
def get_platform_genre_counts(df: pd.DataFrame) -> pd.DataFrame:
    platform_genre_counts = df.groupby(['platform', 'genre']).size().reset_index(name='count')
    return platform_genre_counts


# TODO create bar plot of number of games per genre grouped by platform
def plot_games_per_genre_grouped_by_platform(platform_genre_counts: pd.DataFrame):
    plt.figure(figsize=(12, 6))
    sns.barplot(x='platform', y='count', hue='genre', data=platform_genre_counts)
    plt.title('Number of Games per Genre Grouped by Platform')
    plt.xlabel('Platform')
    plt.ylabel('Number of Games')
    plt.xticks(rotation=45)
    plt.show()