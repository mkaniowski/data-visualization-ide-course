import unittest
from io import StringIO
from unittest.mock import patch
import pandas as pd
from lesson1.task1.task import load_data, df_head, df_describe, df_info, check_missing_values, select_platforms


class TestCase(unittest.TestCase):
    def test_loads_csv_file_correctly(self):
        file_path = '../../data/dataset.csv'
        df = load_data(file_path)
        self.assertFalse(df.empty)
        self.assertEqual(list(df.columns),
                         ['name', 'platform', 'year_of_release', 'genre', 'publisher', 'na_sales', 'eu_sales',
                          'jp_sales', 'other_sales', 'global_sales', 'critic_score', 'critic_count', 'user_score',
                          'user_count', 'developer', 'rating'])

    def test_df_head_correct_values(self):
        df = pd.read_csv('../../data/dataset.csv')
        expected = df.head()
        result = df_head(df)
        pd.testing.assert_frame_equal(result, expected)

    def test_df_describe_correct_values(self):
        df = pd.read_csv('../../data/dataset.csv')
        expected = df.describe()
        result = df_describe(df)
        pd.testing.assert_frame_equal(result, expected)

    def test_prints_info_of_dataframe(self):
        df = pd.read_csv('../../data/dataset.csv')
        with patch('sys.stdout', new=StringIO()) as fake_out:
            df_info(df)
            self.assertNotEqual(fake_out.getvalue().strip(), "")

    def test_prints_missing_values_of_dataframe(self):
        df = pd.read_csv('../../data/dataset.csv')
        with patch('sys.stdout', new=StringIO()) as fake_out:
            check_missing_values(df)
            self.assertNotEqual(fake_out.getvalue().strip(), "")

    def test_number_of_rows_reduced_after_select_platforms(self):
        df = pd.read_csv('../../data/dataset.csv')
        initial_row_count = len(df)
        result = select_platforms(df)
        final_row_count = len(result)
        row_count_after_filter = len(df[df['platform'].isin(['PS4', 'XOne', 'PC', 'WiiU'])])
        self.assertNotEqual(initial_row_count, final_row_count)
        self.assertLess(final_row_count, initial_row_count)
        self.assertEqual(final_row_count, row_count_after_filter)