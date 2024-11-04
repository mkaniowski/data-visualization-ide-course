# Task 1: Loading Data and Getting Basic Information from DataFrame

### Introduction

In this task, you will learn how to load data from a CSV file into a Pandas DataFrame and extract basic information from
it. This is a fundamental step in data analysis and manipulation using Python.

### What is a DataFrame?

A DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes
(rows and columns). It is similar to a table in a database or an Excel spreadsheet. DataFrames are a core component of
the Pandas library and are widely used for data manipulation and analysis.
If you want to get more information about DataFrame you can
visit [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)

### Loading CSV Data Using Pandas

To load data from a CSV file into a DataFrame, you can use the `pd.read_csv()` function provided by the Pandas library.
This function reads a CSV file and converts it into a DataFrame.

If you get exception `FileNotFoundError`, you should check the path to the file and confirm that there is actually a
file
in data folder. If there is no file you can download it from
this [link](https://drive.google.com/drive/folders/18r0XtRXZe_ljb6NfgjUdgnuuINc42SFw). Place the file in data directory
inside this project.

### Getting Basic Information from DataFrame

Once the data is loaded into a DataFrame, you can use several methods to get basic information about the data.
Understanding your data is crucial as it helps you identify any necessary preprocessing steps, detect anomalies, and
decide on the appropriate analysis techniques.

1. **head():** The `head()` method returns the first few rows of the DataFrame. By default, it returns the first 5 rows,
   but you can specify the number of rows to return.
2. **describe():** The `describe()` method generates descriptive statistics of the DataFrame, such as count, mean,
   standard deviation, min, and max values for numerical columns.
3. **info():** The `info()` method provides a concise summary of the DataFrame, including the number of non-null
   entries, data types of columns, and memory usage.

### Selecting specific columns

In this lesson, we are going to limit the number of platforms to 4 (PC, PS4, XOne, WiiU). To achieve this, we will use
the method `df.isin()`. This method takes as argument a list of values and returns a boolean mask that can be used to
filter the DataFrame.

Example:

```python
df[df['col_to_filter'].isin(['val1', 'val2', 'val3', 'val4'])]
```

### Expected Output

`load_data()` function should **return** a DataFrame containing the data loaded from the CSV file.

`df_head()` function should **return** the first 5 rows of the DataFrame.

`df_describe()` function should **return** the descriptive statistics of the DataFrame.

`df_info()` function should **return** the concise summary of the DataFrame.

`select_platforms()` function should **return** a DataFrame containing the data for the selected platforms (PC, PS4,
XOne, WiiU).