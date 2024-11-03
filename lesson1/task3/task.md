# Analyzing and Visualizing the Number of Games per Genre Grouped by Platform

### Introduction

In this task, you will learn how to analyze the number of games per genre grouped by platform and visualize the results
using various plotting methods. This will help you understand the distribution of game genres across different
platforms.

### Getting Platform and Genre Counts

To get the number of games per genre grouped by platform, you can use the `groupby()`, `size()` and `reset_index()`.

- `groupby()` - This method groups the DataFrame using the specified column(s).
- `size()` - This method returns the number of elements in each group.
- `reset_index()` - This method resets the index of the resulting DataFrame.

Example:

```python
platform_genre_counts = df.groupby(['col1', 'col2']).size().reset_index(name='count')
```

### Plotting the Data

To complete this task you can use previously used function uin task 2 with some modifications.

Change parameters of `sns.barplot()` function to:

- x - platform
- y - count
- hue - genre

### Expected Output

`get_platform_genre_counts()` - A function that **returns** a DataFrame containing the number of games per genre grouped
by platform.

`plot_games_per_genre_grouped_by_platform()` - A function that **plots** the number of games per genre grouped by
platform using a bar plot.