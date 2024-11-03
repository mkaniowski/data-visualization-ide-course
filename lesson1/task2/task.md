# Task 2: Analyzing and Visualizing the Number of Games per Genre

### Introduction

In this task, you will learn how to analyze the number of games per genre and visualize the results using various
plotting methods. This is an essential step in understanding the distribution of game genres in your dataset.

### Getting Genre Counts

To get the number of games per genre, you can use the `value_counts()` method on the 'genre' column of your DataFrame.
This method returns a Series containing counts of unique values.

```python
platform_counts = df['some_colum'].value_counts().reset_index()
```

`reset_index()` - This method resets the index of the Series to convert it into a DataFrame.

After resetting the index, you need to rename the columns to 'genre' and 'count' for clarity. You can do this by
acessing the 'columns' attribute of the DataFrame and assigning list of strings that are column names.

```python
platform_counts.columns = ['new_col_name1', 'new_col_name1']
```

### Plotting the Data

Once you have the genre counts, you can visualize the data using bar plot.

First, you need to create a figure and axis object using the `plt.subplots()` method. This method returns a tuple
containing the figure and axis objects.

```python
plt.figure(figsize=(12, 6))
```

```python
sns.barplot(x='col_name1', y='col_name2', data=some_df)
```

To show the plot, you can use the `plt.show()` method.

```python
plt.show()
```

Before using `plt.show()`, you can also set the title and labels for the plot using the `plt.title()`, `plt.xlabel()`,
and `plt.ylabel()` methods.

```python
plt.title('Title of the Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
```

Example:

```python
plt.figure(figsize=(12, 6))
sns.barplot(x='col_name1', y='col_name2', data=some_df)
plt.title('Title of the Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()
```

You can modify the plot even further. To get more methods check
the [seaborn documentaton](https://seaborn.pydata.org/generated/seaborn.barplot.html)
and [matplotlib documentation](https://matplotlib.org/stable/index.html).

### Expected Output

`get_genre_counts()` - A function that **returns** a DataFrame containing the counts of games per genre.

`plot_genre_counts()` - A function that **plots** the genre counts using a bar plot.