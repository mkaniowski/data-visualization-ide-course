import pandas as pd


# TODO load data into pandas dataframe
def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)


# TODO print the head of the dataframe
def df_head(df: pd.DataFrame) -> pd.DataFrame:
    return df.head()


# TODO print describe of the dataframe
def df_describe(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe()


# TODO print the info of the dataframe
def df_info(df: pd.DataFrame) -> None:
    return df.info()


# TODO check if columns: 'name', 'platform', 'genre' contains any missing values
def check_missing_values(df: pd.DataFrame):
    print(df[['name', 'platform', 'genre']].isnull().sum())


# TODO select only the rows where 'platform' is 'PS4', 'XOne', 'PC' and 'WiiU'
def select_platforms(df: pd.DataFrame):
    return df[df['platform'].isin(['PS4', 'XOne', 'PC', 'WiiU'])]


def main():
    file_path = '../../data/dataset.csv'
    df = load_data(file_path)
    df_head(df)
    df_describe(df)
    df_info(df)
    check_missing_values(df)
    select_platforms(df)

if __name__ == "__main__":
    main()