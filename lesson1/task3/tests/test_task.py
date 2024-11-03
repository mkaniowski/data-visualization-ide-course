import unittest

import pandas as pd
import matplotlib.pyplot as plt

from lesson1.task3.task import get_platform_genre_counts, plot_games_per_genre_grouped_by_platform


class TestCase(unittest.TestCase):
    def test_platform_genre_counts_correct_values(self):
        df = pd.read_csv('../../data/dataset.csv')
        df = df[df['platform'].isin(['PS4', 'XOne', 'PC', 'WiiU'])]
        result = get_platform_genre_counts(df)
        expected = df.groupby(['platform', 'genre']).size().reset_index(name='count')

        pd.testing.assert_frame_equal(result, expected)

    def test_check_columns(self):
        df = pd.read_csv('../../data/dataset.csv')
        df = df[df['platform'].isin(['PS4', 'XOne', 'PC', 'WiiU'])]
        result = get_platform_genre_counts(df)
        self.assertListEqual(list(result.columns), ['platform', 'genre', 'count'])

    def test_plot_games_per_genre_grouped_by_platform_correct_values(self):
        df = pd.read_csv('../../data/dataset.csv')
        df = df[df['platform'].isin(['PS4', 'XOne', 'PC', 'WiiU'])]
        platform_genre_counts = get_platform_genre_counts(df)

        plot_games_per_genre_grouped_by_platform(platform_genre_counts)

        ax = plt.gca()

        bars = ax.patches
        for bar, (_, row) in zip(bars, platform_genre_counts.iterrows()):
            expected_count = row['count']
            actual_count = bar.get_height()
            self.assertEqual(actual_count, expected_count)

        plt.close()
