import unittest

import matplotlib.pyplot as plt
import pandas as pd

from lesson1.task2.task import get_genre_counts, plot_games_per_genre


class TestCase(unittest.TestCase):
    def test_genre_counts_correct_values(self):
        df = pd.read_csv('../../data/dataset.csv')
        df = df[df['platform'].isin(['PS4', 'XOne', 'PC', 'WiiU'])]
        result = get_genre_counts(df)
        platform_counts = df['genre'].value_counts().reset_index()
        platform_counts.columns = ['genre', 'count']

        for genre in platform_counts['genre']:
            expected_count = platform_counts[platform_counts['genre'] == genre]['count'].values[0]
            actual_count = result[result['genre'] == genre]['count'].values[0]
            self.assertEqual(actual_count, expected_count)

    def test_check_columns(self):
        df = pd.read_csv('../../data/dataset.csv')
        df = df[df['platform'].isin(['PS4', 'XOne', 'PC', 'WiiU'])]
        result = get_genre_counts(df)
        self.assertListEqual(list(result.columns), ['genre', 'count'])

    def test_plot_games_per_genre_correct_values(self):
        df = pd.read_csv('../../data/dataset.csv')
        df = df[df['platform'].isin(['PS4', 'XOne', 'PC', 'WiiU'])]
        genre_counts = get_genre_counts(df)

        plot_games_per_genre(genre_counts)

        ax = plt.gca()

        bars = ax.patches
        for bar, genre in zip(bars, genre_counts['genre']):
            expected_count = genre_counts[genre_counts['genre'] == genre]['count'].values[0]
            actual_count = bar.get_height()
            self.assertEqual(actual_count, expected_count)

        plt.close()
