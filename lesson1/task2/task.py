import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# TODO return a dataframe with the number of games per genre
def get_genre_counts(df: pd.DataFrame) -> pd.DataFrame:
    platform_counts = df['genre'].value_counts().reset_index()
    platform_counts.columns = ['genre', 'count']
    return platform_counts


# TODO create bar plot of number of games per genre
def plot_games_per_genre(df: pd.DataFrame):
    plt.figure(figsize=(12, 6))
    sns.barplot(x='genre', y='count', data=df)
    plt.title('Number of Games per Platform')
    plt.xlabel('Platform')
    plt.ylabel('Number of Games')
    plt.xticks(rotation=45)
    plt.show()