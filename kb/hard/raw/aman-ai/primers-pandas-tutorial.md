# Primers • Pandas Tutorial

**Source:** https://aman.ai/primers/pandas%20copy/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Overview](#overview)
* [Background](#background)
* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Overview: Pandas data-structures](#overview-pandas-data-structures)
* [pandas is column-major](#pandas-is-column-major)
  + [Converting DataFrame to row-major order](#converting-dataframe-to-row-major-order)
* [`Series` objects](#series-objects)
  + [Creating a `Series`](#creating-a-series)
  + [Similar to a 1D `ndarray`](#similar-to-a-1d-ndarray)
  + [Index labels](#index-labels)
  + [Init from `dict`](#init-from-dict)
  + [Automatic alignment](#automatic-alignment)
    - [Init with a scalar](#init-with-a-scalar)
    - [`Series` name](#series-name)
    - [Plotting a `Series`](#plotting-a-series)
* [Handling time](#handling-time)
  + [Time range](#time-range)
  + [Resampling](#resampling)
  + [Upsampling and interpolation](#upsampling-and-interpolation)
  + [Timezones](#timezones)
  + [Periods](#periods)
* [`DataFrame` objects](#dataframe-objects)
  + [Creating a `DataFrame`](#creating-a-dataframe)
  + [Multi-indexing](#multi-indexing)
  + [Dropping a level](#dropping-a-level)
  + [Transposing](#transposing)
  + [Stacking and unstacking levels](#stacking-and-unstacking-levels)
  + [Most methods return modified copies](#most-methods-return-modified-copies)
  + [Accessing rows](#accessing-rows)
  + [Adding and removing columns](#adding-and-removing-columns)
    - [Assigning new columns](#assigning-new-columns)
    - [Evaluating an expression](#evaluating-an-expression)
    - [Querying a `DataFrame`](#querying-a-dataframe)
    - [Sorting a `DataFrame`](#sorting-a-dataframe)
    - [Plotting a `DataFrame`](#plotting-a-dataframe)
    - [Operations on `DataFrame`s](#operations-on-dataframes)
    - [Automatic alignment](#automatic-alignment-1)
    - [Handling missing data](#handling-missing-data)
    - [Aggregating with `groupby`](#aggregating-with-groupby)
    - [Pivot tables](#pivot-tables)
    - [Overview functions](#overview-functions)
* [Saving & loading](#saving--loading)
  + [Saving](#saving)
  + [Loading](#loading)
* [Combining `DataFrame`s](#combining-dataframes)
  + [SQL-like joins](#sql-like-joins)
  + [Concatenation](#concatenation)
* [Categories](#categories)
* [Practical example using a sample dataset](#practical-example-using-a-sample-dataset)
  + [Dataset at a glance](#dataset-at-a-glance)
  + [Iterating over rows](#iterating-over-rows)
    - [`.apply()`](#apply)
    - [`.iterrows()` and `.itertuples()`](#iterrows-and-itertuples)
    - [Ordering slicing operations](#ordering-slicing-operations)
  + [SettingWithCopyWarning](#settingwithcopywarning)
    - [`View` vs. `Copy`](#view-vs-copy)
    - [Solutions](#solutions)
      * [Combine all chained operations into one single operation](#combine-all-chained-operations-into-one-single-operation)
      * [Raise an error](#raise-an-error)
  + [Indexing and slicing](#indexing-and-slicing)
    - [`.iloc[]`: selecting rows based on integer indices](#iloc-selecting-rows-based-on-integer-indices)
    - [`.loc[]`: selecting rows by labels or boolean masks](#loc-selecting-rows-by-labels-or-boolean-masks)
      * [Selecting rows by boolean masks](#selecting-rows-by-boolean-masks)
      * [Selecting rows by labels](#selecting-rows-by-labels)
        + [Creating labels](#creating-labels)
        + [Selecting rows by labels](#selecting-rows-by-labels-1)
    - [Slicing Series](#slicing-series)
  + [Accessors](#accessors)
    - [string accessor](#string-accessor)
    - [Other accessors](#other-accessors)
  + [Data exploration](#data-exploration)
    - [`.head()`, `.tail()`, `.describe()`, `.info()`](#head-tail-describe-info)
    - [Count unique values](#count-unique-values)
    - [Plotting](#plotting)
  + [Common pitfalls](#common-pitfalls)
    - [NaNs as floats](#nans-as-floats)
    - [Changes aren’t in-place by default](#changes-arent-in-place-by-default)
    - [Reproducibility issues](#reproducibility-issues)
    - [Not GPU compatible](#not-gpu-compatible)
* [What next?](#what-next)
* [References and Credits](#references-and-credits)
* [Citation](#citation)

## Overview

* The pandas library provides high-performance, easy-to-use data structures and data analysis tools. The main data structure is the `DataFrame`, which you can think of as an in-memory 2D table (like a spreadsheet, with column names and row labels).
* Many features available in Excel are available programmatically, such as creating pivot tables, computing columns based on other columns, plotting graphs, etc. You can also group rows by column value, or join tables much like in SQL. Pandas is also great at handling time series data.

## Background

* It’s possible that Python wouldn’t have become [the lingua franca of data science if it wasn’t for pandas](https://stackoverflow.blog/2017/09/14/python-growing-quickly/). The package’s exponential growth on Stack Overflow means two things:

  1. It’s getting increasingly popular.
  2. It can be frustrating to use sometimes (hence the high number of questions).
* This tutorial contains a few peculiar things about pandas that hopefully make your life easier and code faster.

## Prerequisites

* If you are not familiar with NumPy, we recommend that you go through the [NumPy tutorial](../numpy) now.

## Setup

* First, let’s import pandas. People usually import it as `pd`:

  ```
    import pandas as pd
  ```

## Overview: Pandas data-structures

* The pandas library contains these useful data structures:
  + `Series` objects: A `Series` object is 1D array, similar to a column in a spreadsheet (with a column name and row labels).
  + `DataFrame` objects: A `DataFrame` is a concept inspired by R’s Data Frame, which is, in turn, similar to tables in relational databases. This is a 2D table with rows and columns, similar to a spreadsheet (with names for columns and labels for rows).
  + `Panel` objects: You can see a `Panel` as a dictionary of `DataFrame`s. These are less used, so we will not discuss them here.

## pandas is column-major

> An important thing to know about pandas is that it is column-major, which explains many of its quirks.

* Column-major means consecutive elements in a column are stored next to each other in memory. Row-major means the same but for elements in a row. Because modern computers process sequential data more efficiently than non-sequential data, if a table is row-major, accessing its rows will be much faster than accessing its columns.
* In NumPy, major order can be specified. When a `ndarray` is created, it’s row-major by default if you don’t specify the order.
* Like R’s Data Frame, pandas’ `DataFrame` is column-major. People coming to pandas from NumPy tend to treat `DataFrame` the way they would `ndarray`, e.g. trying to access data by rows, and find `DataFrame` slow.
* **Note**: A column in a `DataFrame` is a `Series`. You can think of a `DataFrame` as a bunch of `Series` being stored next to each other in memory.
* **For our dataset, accessing a row takes about 50x longer than accessing a column in our `DataFrame`.**
* Run the following code snippet in a Colab/Jupyter notebook:

  ```
    # Get the column `date`, 1000 loops
    %timeit -n1000 df["Date"]

    # Get the first row, 1000 loops
    %timeit -n1000 df.iloc[0]
  ```

  + which outputs:

  ```
    1.78 µs ± 167 ns per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    145 µs ± 9.41 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
  ```

### Converting DataFrame to row-major order

* If you need to do a lot of row operations, you might want to convert your `DataFrame` to a NumPy’s row-major `ndarray`, then iterating through the rows. Run the following code snippet in a Colab/Jupyter notebook:

  ```
    # Now, iterating through our DataFrame is 100x faster.
    %timeit -n1 df_np = df.to_numpy(); rows = [row for row in df_np]
  ```

  + which outputs:

  ```
    4.55 ms ± 280 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)
  ```
* Accessing a row or a column of our `ndarray` takes nanoseconds instead of microseconds. Run the following code snippet in a Colab/Jupyter notebook:

  ```
    df_np = df.to_numpy()
    %timeit -n1000 df_np[0]
    %timeit -n1000 df_np[:,0]
  ```

  + which outputs:

  ```
    147 ns ± 1.54 ns per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    204 ns ± 0.678 ns per loop (mean ± std. dev. of 7 runs, 1000 loops each)
  ```

## `Series` objects

### Creating a `Series`

* Let’s start by creating our first `Series` object!

  ```
    import pandas as pd

    pd.Series([1, 2, 3])
  ```

  + which outputs:

  ```
    0    1
    1    2
    2    3
    dtype: int64
  ```

### Similar to a 1D `ndarray`

* `Series` objects behave much like one-dimensional NumPy `ndarray`s, and you can often pass them as parameters to NumPy functions:

  ```
    import pandas as pd

    s = pd.Series([1, 2, 3])
    np.exp(s)
  ```

  + which outputs:

  ```
    0     2.718282
    1     7.389056
    2    20.085537
    dtype: float64
  ```
* Arithmetic operations on `Series` are also possible, and they apply **elementwise**, just like for `ndarray`s:

  ```
    s = pd.Series([1, 2, 3])
    np.exp(s)
    s + [1000, 2000, 3000]
  ```

  + which outputs:

  ```
    0    1001
    1    2002
    2    3003
    dtype: int64
  ```
* Similar to NumPy, if you add a single number to a `Series`, that number is added to all items in the `Series`. This is called **broadcasting**:

  ```
    s = pd.Series([1, 2, 3])
    np.exp(s)
    s + 1000
  ```

  + which outputs:

  ```
    0    1001
    1    1002
    2    1003
    dtype: int64
  ```
* The same is true for all binary operations such as `*` or `/`, and even conditional operations:

  ```
    s = pd.Series([1, 2, 3])
    np.exp(s)
    s < 0
  ```

  + which outputs:

  ```
    0    False
    1    False
    2    False
    dtype: bool
  ```

### Index labels

* Each item in a `Series` object has a unique identifier called the **index label**. By default, it is simply the rank of the item in the `Series` (starting at `0`) but you can also set the index labels manually:

  ```
    import pandas as pd

    s = pd.Series([68, 83, 112, 68], index=["alice", "bob", "charles", "darwin"])
    s
  ```

  + which outputs:

  ```
    alice       68
    bob         83
    charles    112
    darwin      68
    dtype: int64
  ```
* You can then use the `Series` just like a `dict`:

  ```
    s["bob"]
  ```

  + which outputs:

  ```
    83
  ```
* You can still access the items by integer location, like in a regular array:

  ```
    s[1]
  ```

  + which outputs:

  ```
    83
  ```
* To make it clear when you are accessing by label, it is recommended to always use the `loc` attribute when accessing by label:

  ```
    s.loc["bob"]
  ```

  + which outputs:

  ```
    83
  ```
* Similarly, to make it clear when you are accessing by integer location, it is recommended to always use the `iloc` attribute when accessing by integer location:

  ```
    s2.iloc[1]
  ```

  + which outputs:

  ```
    83
  ```
* Slicing a `Series` also slices the index labels:

  ```
    s.iloc[1:3]
  ```

  + which outputs:

  ```
    bob         83
    charles    112
    dtype: int64
  ```
* Pitfall: This can lead to unexpected results when using the default numeric labels, so be careful:

  ```
    surprise = pd.Series([1000, 1001, 1002, 1003])
    surprise
  ```

  + which outputs:

  ```
    0    1000
    1    1001
    2    1002
    3    1003
    dtype: int64
  ```

  ```
    surprise_slice = surprise[2:]
    surprise_slice
  ```

  + which outputs:

  ```
    2    1002
    3    1003
    dtype: int64
  ```
* Oh look! The first element has index label `2`. The element with index label `0` is absent from the slice:

  ```
    try:
        surprise_slice[0]
    except KeyError as e:
        print("Key error:", e)
  ```

  + which outputs:

  ```
    Key error: 0
  ```
* But remember that you can access elements by integer location using the `iloc` attribute. This illustrates another reason why it’s always better to use `loc` and `iloc` to access `Series` objects:

  ```
    surprise_slice.iloc[0]
  ```

  + which outputs:

  ```
    1002
  ```

### Init from `dict`

* You can create a `Series` object from a `dict`. The keys will be used as index labels:

  ```
    import pandas as pd

    weights = {"alice": 68, "bob": 83, "colin": 86, "darwin": 68}
    pd.Series(weights)
  ```

  + which outputs:

  ```
    alice     68
    bob       83
    colin     86
    darwin    68
    dtype: int64
  ```
* You can control which elements you want to include in the `Series` and in what order by explicitly specifying the desired `index`:

  ```
    pd.Series(weights, index = ["colin", "alice"])
  ```

  + which outputs:

  ```
    colin    86
    alice    68
    dtype: int64
  ```

### Automatic alignment

* When an operation involves multiple `Series` objects, pandas automatically aligns items by matching index labels.

  ```
    import pandas as pd

    s1 = pd.Series([68, 83, 112, 68], index=["alice", "bob", "charles", "darwin"])

    weights = {"alice": 68, "bob": 83, "colin": 86, "darwin": 68}
    s2 = pd.Series(weights)

    print(s2.keys())
    print(s3.keys())

    s2 + s3
  ```

  + which outputs:

  ```
    alice     136
    bob       166
    colin     172
    darwin    136
    dtype: int64
  ```
* The resulting `Series` contains the union of index labels from `s2` and `s3`. Since `"colin"` is missing from `s2` and `"charles"` is missing from `s3`, these items have a `NaN` result value. (i.e., Not-a-Number means **missing**).
* Automatic alignment is very handy when working with data that may come from various sources with varying structure and missing items. But if you forget to set the right index labels, you can have surprising results:

  ```
    s1 = pd.Series([68, 83, 112, 68], index=["alice", "bob", "charles", "darwin"])
    s2 = pd.Series([1000, 1000, 1000, 1000])

    print("s1 = ", s1.values)
    print("s2 = ", s2.values)

    s1 + s2
  ```

  + which outputs:

  ```
    alice     NaN
    bob       NaN
    charles   NaN
    darwin    NaN
    0         NaN
    1         NaN
    2         NaN
    3         NaN
    dtype: float64
  ```
* Pandas could not align the `Series`, since their labels do not match at all, hence the full `NaN` result.

#### Init with a scalar

* You can also initialize a `Series` object using a scalar and a list of index labels: all items will be set to the scalar.

  ```
    pd.Series(42, ["life", "universe", "everything"])
  ```

  + which outputs:

  ```
    life          42
    universe      42
    everything    42
    dtype: int64
  ```

#### `Series` name

* A `Series` can have a `name`:

  ```
    pd.Series([83, 68], index=["bob", "alice"], name="weights")
  ```

  + which outputs:

  ```
    bob      83
    alice    68
    Name: weights, dtype: int64
  ```

#### Plotting a `Series`

* Pandas makes it easy to plot `Series` data using matplotlib (for more details on matplotlib, check out the [matplotlib tutorial](tools_matplotlib.ipynb)).
* Just import matplotlib and call the `plot()` method:

  ```
    %matplotlib inline
    import matplotlib.pyplot as plt

    temperatures = [4.4, 5.1, 6.1, 6.2, 6.1, 6.1, 5.7, 5.2, 4.7, 4.1, 3.9, 3.5]
    s = pd.Series(temperatures, name="Temperature")
    s.plot()
    plt.show()
  ```

  + which outputs:
* There are **many** options for plotting your data. It is not necessary to list them all here: if you need a particular type of plot (histograms, pie charts, etc.), just look for it in the excellent [visualization](http://pandas.pydata.org/pandas-docs/stable/visualization.html) section of pandas’ documentation, and look at the example code.

## Handling time

* Many datasets have timestamps, and pandas is awesome at manipulating such data:

  + It can represent periods (such as 2016Q3) and frequencies (such as “monthly”),
  + It can convert periods to actual timestamps, and **vice versa**,
  + It can resample data and aggregate values any way you like,
  + It can handle timezones.

#### Time range

* Let’s start by creating a time series using `pd.date_range()`. This returns a `DatetimeIndex` containing one datetime per hour for 12 hours starting on October 29th 2016 at 5:30PM.

  ```
    import pandas as pd

    dates = pd.date_range('2016/10/29 5:30pm', periods=12, freq='H')
    dates
  ```

  + which outputs:

  ```
    DatetimeIndex(['2016-10-29 17:30:00', '2016-10-29 18:30:00',
                   '2016-10-29 19:30:00', '2016-10-29 20:30:00',
                   '2016-10-29 21:30:00', '2016-10-29 22:30:00',
                   '2016-10-29 23:30:00', '2016-10-30 00:30:00',
                   '2016-10-30 01:30:00', '2016-10-30 02:30:00',
                   '2016-10-30 03:30:00', '2016-10-30 04:30:00'],
                   dtype='datetime64[ns]', freq='H')
  ```
* This `DatetimeIndex` may be used as an index in a `Series`:

  ```
    temperatures = [4.4, 5.1, 6.1, 6.2, 6.1, 6.1, 5.7, 5.2, 4.7, 4.1, 3.9, 3.5]
    temp_series = pd.Series(temperatures, dates)
    temp_series
  ```

  + which outputs:

  ```
    2016-10-29 17:30:00    4.4
    2016-10-29 18:30:00    5.1
    2016-10-29 19:30:00    6.1
    2016-10-29 20:30:00    6.2
    2016-10-29 21:30:00    6.1
    2016-10-29 22:30:00    6.1
    2016-10-29 23:30:00    5.7
    2016-10-30 00:30:00    5.2
    2016-10-30 01:30:00    4.7
    2016-10-30 02:30:00    4.1
    2016-10-30 03:30:00    3.9
    2016-10-30 04:30:00    3.5
    Freq: H, dtype: float64
  ```
* Let’s plot this series:

  ```
    import matplotlib.pyplot as plt

    temp_series.plot(kind="bar")

    plt.grid(True)
    plt.show()
  ```

  + which outputs:

### Resampling

* Pandas lets us resample a time series very simply. Just call the `resample()` method and specify a new frequency:

  ```
    import pandas as pd

    temp_series = pd.Series({pd.Timestamp('2016-10-29 17:30:00', freq='H'): 4.4, pd.Timestamp('2016-10-29 18:30:00', freq='H'): 5.1, pd.Timestamp('2016-10-29 19:30:00', freq='H'): 6.1, pd.Timestamp('2016-10-29 20:30:00', freq='H'): 6.2, pd.Timestamp('2016-10-29 21:30:00', freq='H'): 6.1, pd.Timestamp('2016-10-29 22:30:00', freq='H'): 6.1, pd.Timestamp('2016-10-29 23:30:00', freq='H'): 5.7, pd.Timestamp('2016-10-30 00:30:00', freq='H'): 5.2, pd.Timestamp('2016-10-30 01:30:00', freq='H'): 4.7, pd.Timestamp('2016-10-30 02:30:00', freq='H'): 4.1, pd.Timestamp('2016-10-30 03:30:00', freq='H'): 3.9, pd.Timestamp('2016-10-30 04:30:00', freq='H'): 3.5})

    temp_series_freq_2H = temp_series.resample("2H")
    temp_series_freq_2H
  ```

  + which outputs:

  ```
    <pandas.core.resample.DatetimeIndexResampler object at [address]>
  ```
* The resampling operation is actually a deferred operation, which is why we did not get a `Series` object, but a `DatetimeIndexResampler` object instead. To actually perform the resampling operation, we can simply call the `mean()` method: Pandas will compute the mean of every pair of consecutive hours:

  ```
    temp_series_freq_2H = temp_series_freq_2H.mean()
    temp_series_freq_2H
  ```

  + which outputs:

  ```
    2016-10-29 16:00:00    4.40
    2016-10-29 18:00:00    5.60
    2016-10-29 20:00:00    6.15
    2016-10-29 22:00:00    5.90
    2016-10-30 00:00:00    4.95
    2016-10-30 02:00:00    4.00
    2016-10-30 04:00:00    3.50
    Freq: 2H, dtype: float64
  ```
* Let’s plot the result:

  ```
    temp_series_freq_2H.plot(kind="bar")
    plt.show()
  ```

  + which outputs:
* Note how the values have automatically been aggregated into 2-hour periods. If we look at the 6-8PM period, for example, we had a value of `5.1` at 6:30PM, and `6.1` at 7:30PM. After resampling, we just have one value of `5.6`, which is the mean of `5.1` and `6.1`. Rather than computing the mean, we could have used any other aggregation function, for example we can decide to keep the minimum value of each period:

  ```
    temp_series_freq_2H = temp_series.resample("2H").min()
    temp_series_freq_2H
  ```

  + which outputs:

  ```
    2016-10-29 16:00:00    4.4
    2016-10-29 18:00:00    5.1
    2016-10-29 20:00:00    6.1
    2016-10-29 22:00:00    5.7
    2016-10-30 00:00:00    4.7
    2016-10-30 02:00:00    3.9
    2016-10-30 04:00:00    3.5
    Freq: 2H, dtype: float64
  ```
* Or, equivalently, we could use the `apply()` method instead:

  ```
    import numpy as np

    temp_series_freq_2H = temp_series.resample("2H").apply(np.min)
    temp_series_freq_2H
  ```

  + which outputs:

  ```
    2016-10-29 16:00:00    4.4
    2016-10-29 18:00:00    5.1
    2016-10-29 20:00:00    6.1
    2016-10-29 22:00:00    5.7
    2016-10-30 00:00:00    4.7
    2016-10-30 02:00:00    3.9
    2016-10-30 04:00:00    3.5
    Freq: 2H, dtype: float64
  ```

### Upsampling and interpolation

* The [above](#resampling) was an example of downsampling. We can also upsample (i.e., increase the frequency), but this creates holes in our data:

  ```
    import pandas as pd

    temp_series = pd.Series({pd.Timestamp('2016-10-29 17:30:00', freq='H'): 4.4, pd.Timestamp('2016-10-29 18:30:00', freq='H'): 5.1, pd.Timestamp('2016-10-29 19:30:00', freq='H'): 6.1, pd.Timestamp('2016-10-29 20:30:00', freq='H'): 6.2, pd.Timestamp('2016-10-29 21:30:00', freq='H'): 6.1, pd.Timestamp('2016-10-29 22:30:00', freq='H'): 6.1, pd.Timestamp('2016-10-29 23:30:00', freq='H'): 5.7, pd.Timestamp('2016-10-30 00:30:00', freq='H'): 5.2, pd.Timestamp('2016-10-30 01:30:00', freq='H'): 4.7, pd.Timestamp('2016-10-30 02:30:00', freq='H'): 4.1, pd.Timestamp('2016-10-30 03:30:00', freq='H'): 3.9, pd.Timestamp('2016-10-30 04:30:00', freq='H'): 3.5})

    temp_series_freq_15min = temp_series.resample("15Min").mean()
    temp_series_freq_15min.head(n=10) # `head` displays the top n values
  ```

  + which outputs:

  ```
    2016-10-29 17:30:00    4.4
    2016-10-29 17:45:00    NaN
    2016-10-29 18:00:00    NaN
    2016-10-29 18:15:00    NaN
    2016-10-29 18:30:00    5.1
    2016-10-29 18:45:00    NaN
    2016-10-29 19:00:00    NaN
    2016-10-29 19:15:00    NaN
    2016-10-29 19:30:00    6.1
    2016-10-29 19:45:00    NaN
    Freq: 15T, dtype: float64
  ```
* One solution is to fill the gaps by interpolating. We just call the `interpolate()` method. The default is to use linear interpolation, but we can also select another method, such as cubic interpolation:

  ```
    temp_series_freq_15min = temp_series.resample("15Min").interpolate(method="cubic")
    temp_series_freq_15min.head(n=10)
  ```

  + which outputs:

  ```
    2016-10-29 17:30:00    4.400000
    2016-10-29 17:45:00    4.452911
    2016-10-29 18:00:00    4.605113
    2016-10-29 18:15:00    4.829758
    2016-10-29 18:30:00    5.100000
    2016-10-29 18:45:00    5.388992
    2016-10-29 19:00:00    5.669887
    2016-10-29 19:15:00    5.915839
    2016-10-29 19:30:00    6.100000
    2016-10-29 19:45:00    6.203621
    Freq: 15T, dtype: float64
  ```
* Plotting the data:

  ```
    temp_series.plot(label="Period: 1 hour")
    temp_series_freq_15min.plot(label="Period: 15 minutes")
    plt.legend()
    plt.show()
  ```

  + which outputs:

### Timezones

* By default datetimes are **naive**: they are not aware of timezones, so 2016-10-30 02:30 might mean October 30th 2016 at 2:30am in Paris or in New York. We can make datetimes timezone **aware** by calling the `tz_localize()` method:

  ```
    import pandas as pd

    temp_series_ny = pd.Series({pd.Timestamp('2016-10-29 17:30:00', freq='H'): 4.4, pd.Timestamp('2016-10-29 18:30:00', freq='H'): 5.1, pd.Timestamp('2016-10-29 19:30:00', freq='H'): 6.1, pd.Timestamp('2016-10-29 20:30:00', freq='H'): 6.2, pd.Timestamp('2016-10-29 21:30:00', freq='H'): 6.1, pd.Timestamp('2016-10-29 22:30:00', freq='H'): 6.1, pd.Timestamp('2016-10-29 23:30:00', freq='H'): 5.7, pd.Timestamp('2016-10-30 00:30:00', freq='H'): 5.2, pd.Timestamp('2016-10-30 01:30:00', freq='H'): 4.7, pd.Timestamp('2016-10-30 02:30:00', freq='H'): 4.1, pd.Timestamp('2016-10-30 03:30:00', freq='H'): 3.9, pd.Timestamp('2016-10-30 04:30:00', freq='H'): 3.5})

    temp_series_ny = temp_series.tz_localize("America/New_York")
    temp_series_ny
  ```

  + which outputs:

  ```
    2016-10-29 17:30:00-04:00    4.4
    2016-10-29 18:30:00-04:00    5.1
    2016-10-29 19:30:00-04:00    6.1
    2016-10-29 20:30:00-04:00    6.2
    2016-10-29 21:30:00-04:00    6.1
    2016-10-29 22:30:00-04:00    6.1
    2016-10-29 23:30:00-04:00    5.7
    2016-10-30 00:30:00-04:00    5.2
    2016-10-30 01:30:00-04:00    4.7
    2016-10-30 02:30:00-04:00    4.1
    2016-10-30 03:30:00-04:00    3.9
    2016-10-30 04:30:00-04:00    3.5
    Freq: H, dtype: float64
  ```
* Note that `-04:00` is now appended to all the datetimes. This means that these datetimes refer to [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) - 4 hours.
* We can convert these datetimes to Paris time like this:

  ```
    temp_series_paris = temp_series_ny.tz_convert("Europe/Paris")
    temp_series_paris
  ```

  + which outputs:

  ```
    2016-10-29 23:30:00+02:00    4.4
    2016-10-30 00:30:00+02:00    5.1
    2016-10-30 01:30:00+02:00    6.1
    2016-10-30 02:30:00+02:00    6.2
    2016-10-30 02:30:00+01:00    6.1
    2016-10-30 03:30:00+01:00    6.1
    2016-10-30 04:30:00+01:00    5.7
    2016-10-30 05:30:00+01:00    5.2
    2016-10-30 06:30:00+01:00    4.7
    2016-10-30 07:30:00+01:00    4.1
    2016-10-30 08:30:00+01:00    3.9
    2016-10-30 09:30:00+01:00    3.5
    Freq: H, dtype: float64
  ```
* You may have noticed that the UTC offset changes from `+02:00` to `+01:00`: this is because France switches to winter time at 3am that particular night (time goes back to 2am). Notice that 2:30am occurs twice! Let’s go back to a naive representation (if you log some data hourly using local time, without storing the timezone, you might get something like this):

  ```
    temp_series_paris_naive = temp_series_paris.tz_localize(None)
    temp_series_paris_naive
  ```

  + which outputs:

  ```
    2016-10-29 23:30:00    4.4
    2016-10-30 00:30:00    5.1
    2016-10-30 01:30:00    6.1
    2016-10-30 02:30:00    6.2
    2016-10-30 02:30:00    6.1
    2016-10-30 03:30:00    6.1
    2016-10-30 04:30:00    5.7
    2016-10-30 05:30:00    5.2
    2016-10-30 06:30:00    4.7
    2016-10-30 07:30:00    4.1
    2016-10-30 08:30:00    3.9
    2016-10-30 09:30:00    3.5
    Freq: H, dtype: float64
  ```
* Now `02:30` is really ambiguous. If we try to localize these naive datetimes to the Paris timezone, we get an error:

  ```
    try:
        temp_series_paris_naive.tz_localize("Europe/Paris")
    except Exception as e:
        print(type(e))
        print(e)
  ```

  + which outputs:

  ```
    <class 'pytz.exceptions.AmbiguousTimeError'>
    Cannot infer dst time from %r, try using the 'ambiguous' argument
  ```
* Fortunately using the `ambiguous` argument we can tell pandas to infer the right DST (Daylight Saving Time) based on the order of the ambiguous timestamps:

  ```
    temp_series_paris_naive.tz_localize("Europe/Paris", ambiguous="infer")
  ```

  + which outputs:

  ```
    2016-10-29 23:30:00+02:00    4.4
    2016-10-30 00:30:00+02:00    5.1
    2016-10-30 01:30:00+02:00    6.1
    2016-10-30 02:30:00+02:00    6.2
    2016-10-30 02:30:00+01:00    6.1
    2016-10-30 03:30:00+01:00    6.1
    2016-10-30 04:30:00+01:00    5.7
    2016-10-30 05:30:00+01:00    5.2
    2016-10-30 06:30:00+01:00    4.7
    2016-10-30 07:30:00+01:00    4.1
    2016-10-30 08:30:00+01:00    3.9
    2016-10-30 09:30:00+01:00    3.5
    Freq: H, dtype: float64
  ```

### Periods

* The `pd.period_range()` function returns a `PeriodIndex` instead of a `DatetimeIndex`. For example, let’s get all quarters in 2016 and 2017:

  ```
    import pandas as pd

    quarters = pd.period_range('2016Q1', periods=8, freq='Q')
    quarters
  ```

  + which outputs:

  ```
    PeriodIndex(['2016Q1', '2016Q2', '2016Q3', '2016Q4', '2017Q1', '2017Q2',
                 '2017Q3', '2017Q4'],
                 dtype='period[Q-DEC]', freq='Q-DEC')
  ```
* Adding a number `N` to a `PeriodIndex` shifts the periods by `N` times the `PeriodIndex`’s frequency:

  ```
    quarters + 3
  ```

  + which outputs:

  ```
    PeriodIndex(['2016Q4', '2017Q1', '2017Q2', '2017Q3', '2017Q4', '2018Q1',
                 '2018Q2', '2018Q3'],
                 dtype='period[Q-DEC]', freq='Q-DEC')
  ```
* The `asfreq()` method lets us change the frequency of the `PeriodIndex`. All periods are lengthened or shortened accordingly. For example, let’s convert all the quarterly periods to monthly periods (zooming in):

  ```
    quarters.asfreq("M")
  ```

  + which outputs:

  ```
    PeriodIndex(['2016-03', '2016-06', '2016-09', '2016-12', '2017-03', '2017-06',
                 '2017-09', '2017-12'],
                 dtype='period[M]', freq='M')
  ```
* By default, the `asfreq` zooms on the end of each period. We can tell it to zoom on the start of each period instead:

  ```
    quarters.asfreq("M", how="start")
  ```

  + which outputs:

  ```
    PeriodIndex(['2016-01', '2016-04', '2016-07', '2016-10', '2017-01', '2017-04',
                 '2017-07', '2017-10'],
                 dtype='period[M]', freq='M')
  ```
* And we can zoom out:

  ```
    quarters.asfreq("A")
  ```

  + which outputs:

  ```
    PeriodIndex(['2016', '2016', '2016', '2016', '2017', '2017', '2017', '2017'], dtype='period[A-DEC]', freq='A-DEC')
  ```
* We can create a `Series` with a `PeriodIndex`:

  ```
    quarterly_revenue = pd.Series([300, 320, 290, 390, 320, 360, 310, 410], index = quarters)
    quarterly_revenue
  ```

  + which outputs:

  ```
    2016Q1    300
    2016Q2    320
    2016Q3    290
    2016Q4    390
    2017Q1    320
    2017Q2    360
    2017Q3    310
    2017Q4    410
  ```
* Plotting this data:

  ```
    quarterly_revenue.plot(kind="line")
    plt.show()
  ```

  + which outputs:
* We can convert periods to timestamps by calling `to_timestamp`. By default this will give us the first day of each period, but by setting `how` and `freq`, we can get the last hour of each period:

  ```
    last_hours = quarterly_revenue.to_pd.Timestamp(how="end", freq="H")
    last_hours
  ```

  + which outputs:

  ```
    2016-03-31 23:59:59.999999999    300
    2016-06-30 23:59:59.999999999    320
    2016-09-30 23:59:59.999999999    290
    2016-12-31 23:59:59.999999999    390
    2017-03-31 23:59:59.999999999    320
    2017-06-30 23:59:59.999999999    360
    2017-09-30 23:59:59.999999999    310
    2017-12-31 23:59:59.999999999    410
    Freq: Q-DEC, dtype: int64
  ```
* And back to periods by calling `to_period`:

  ```
    last_hours.to_period()
  ```

  + which outputs:

  ```
    2016Q1    300
    2016Q2    320
    2016Q3    290
    2016Q4    390
    2017Q1    320
    2017Q2    360
    2017Q3    310
    2017Q4    410
    Freq: Q-DEC, dtype: int64
  ```
* Pandas also provides many other time-related functions that we recommend you check out in the [documentation](http://pandas.pydata.org/pandas-docs/stable/timeseries.html). To whet your appetite, here is one way to get the last business day of each month in 2016, at 9am:

  ```
    months_2016 = pd.period_range("2016", periods=12, freq="M")
    one_day_after_last_days = months_2016.asfreq("D") + 1
    last_bdays = one_day_after_last_days.to_pd.Timestamp() - pd.tseries.offsets.BDay()
    last_bdays.to_period("H") + 9
  ```

  + which outputs:

  ```
    PeriodIndex(['2016-01-29 09:00', '2016-02-29 09:00', '2016-03-31 09:00',
                 '2016-04-29 09:00', '2016-05-31 09:00', '2016-06-30 09:00',
                 '2016-07-29 09:00', '2016-08-31 09:00', '2016-09-30 09:00',
                 '2016-10-31 09:00', '2016-11-30 09:00', '2016-12-30 09:00'],
                dtype='period[H]', freq='H')
  ```

## `DataFrame` objects

* A DataFrame object represents a spreadsheet, with cell values, column names and row index labels. You can define expressions to compute columns based on other columns, create pivot-tables, group rows, draw graphs, etc. You can see `DataFrame`s as dictionaries of `Series`.

### Creating a `DataFrame`

* You can create a DataFrame by passing a dictionary of `Series` objects:

  ```
    import pandas as pd

    people_dict = {
        "weight": pd.Series([68, 83, 112], index=["alice", "bob", "charles"]),
        "birthyear": pd.Series([1984, 1985, 1992], index=["bob", "alice", "charles"], name="year"),
        "children": pd.Series([0, 3], index=["charles", "bob"]),
        "hobby": pd.Series(["Biking", "Dancing"], index=["alice", "bob"]),
    }

    people = pd.DataFrame(people_dict)
    people
  ```

  + which outputs:

  ```
             weight  birthyear  children    hobby
    alice        68       1985       NaN   Biking
    bob          83       1984       3.0  Dancing
    charles     112       1992       0.0      NaN
  ```
* A few things to note:

  + The `Series` were automatically aligned based on their index,
  + Missing values are represented as `NaN`,
  + `Series` names are ignored (the name `"year"` was dropped),
  + `DataFrame`s are displayed nicely in Jupyter notebooks, woohoo!
* You can access columns pretty much as you would expect. They are returned as `Series` objects:

  ```
    people["birthyear"]
  ```

  + which outputs:

  ```
    alice      1985
    bob        1984
    charles    1992
    Name: birthyear, dtype: int64
  ```
* You can also get multiple columns at once:

  ```
    people[["birthyear", "hobby"]]
  ```

  + which outputs:

  ```
             birthyear    hobby
    alice         1985   Biking
    bob           1984  Dancing
    charles       1992      NaN
  ```
* If you pass a list of columns and/or index row labels to the `DataFrame` constructor, it will guarantee that these columns and/or rows will exist, in that order, and no other column/row will exist. For example:

  ```
    d2 = pd.DataFrame(
            people_dict,
            columns=["birthyear", "weight", "height"],
            index=["bob", "alice", "eugene"]
         )
    d2
  ```

  + which outputs:

  ```
            birthyear  weight height
    bob        1984.0    83.0    NaN
    alice      1985.0    68.0    NaN
    eugene        NaN     NaN    NaN
  ```
* Another convenient way to create a `DataFrame` is to pass all the values to the constructor as an `ndarray`, or a list of lists, and specify the column names and row index labels separately:

  ```
    import numpy as np

    values = [
                [1985, np.nan, "Biking",   68],
                [1984, 3,      "Dancing",  83],
                [1992, 0,      np.nan,    112]
             ]
    d3 = pd.DataFrame(
            values,
            columns=["birthyear", "children", "hobby", "weight"],
            index=["alice", "bob", "charles"]
         )
    d3
  ```

  + which outputs:

  ```
             birthyear  children    hobby  weight
    alice         1985       NaN   Biking      68
    bob           1984       3.0  Dancing      83
    charles       1992       0.0      NaN     112
  ```
* To specify missing values, you can either use `np.nan` or NumPy’s masked arrays:

  ```
    masked_array = np.ma.asarray(values, dtype=np.object)
    masked_array[(0, 2), (1, 2)] = np.ma.masked
    d3 = pd.DataFrame(
            masked_array,
            columns=["birthyear", "children", "hobby", "weight"],
            index=["alice", "bob", "charles"]
         )
    d3
  ```

  + which outputs:

  ```
            birthyear children    hobby weight
    alice        1985      NaN   Biking     68
    bob          1984        3  Dancing     83
    charles      1992        0      NaN    112
  ```
* Instead of an `ndarray`, you can also pass a `DataFrame` object:

  ```
    d4 = pd.DataFrame(
             d3,
             columns=["hobby", "children"],
             index=["alice", "bob"]
         )
    d4
  ```

  + which outputs:

  ```
             hobby children
    alice   Biking      NaN
    bob    Dancing        3
  ```
* It is also possible to create a `DataFrame` with a dictionary (or list) of dictionaries (or list):

  ```
    people = pd.DataFrame({
        "birthyear": {"alice":1985, "bob": 1984, "charles": 1992},
        "hobby": {"alice":"Biking", "bob": "Dancing"},
        "weight": {"alice":68, "bob": 83, "charles": 112},
        "children": {"bob": 3, "charles": 0}
    })
    people
  ```

  + which outputs:

  ```
             birthyear    hobby  weight  children
    alice         1985   Biking      68       NaN
    bob           1984  Dancing      83       3.0
    charles       1992      NaN     112       0.0
  ```

### Multi-indexing

* If all columns are tuples of the same size, then they are understood as a multi-index. The same goes for row index labels. For example:

  ```
    import pandas as pd
    import numpy as np

    d5 = pd.DataFrame(
      {
        ("public", "birthyear"):
            {("Paris","alice"):1985, ("Paris","bob"): 1984, ("London","charles"): 1992},
        ("public", "hobby"):
            {("Paris","alice"):"Biking", ("Paris","bob"): "Dancing"},
        ("private", "weight"):
            {("Paris","alice"):68, ("Paris","bob"): 83, ("London","charles"): 112},
        ("private", "children"):
            {("Paris", "alice"):np.nan, ("Paris","bob"): 3, ("London","charles"): 0}
      }
    )
    d5
  ```

  + which outputs:

  ```
                      public          private
                   birthyear    hobby  weight children
    Paris  alice        1985   Biking      68      NaN
           bob          1984  Dancing      83      3.0
    London charles      1992      NaN     112      0.0
  ```
* You can now get a `DataFrame` containing all the `"public"` columns by simply doing:

  ```
    d5["public"]
  ```

  + which outputs:

  ```
                    birthyear    hobby
    Paris  alice         1985   Biking
           bob           1984  Dancing
    London charles       1992      NaN
  ```
* You can also now get a `DataFrame` containing all the `"hobby"` columns within the `"public"` columns by simply doing:

  ```
    d5["public", "hobby"] # Same result as d5["public"]["hobby"]
  ```

  + which outputs:

  ```
    Paris   alice       Biking
            bob        Dancing
    London  charles        NaN
    Name: (public, hobby), dtype: object
  ```

### Dropping a level

* Let’s look at `d5` again:

  ```
    import pandas as pd
    import numpy as np

    d5 = pd.DataFrame({('public', 'birthyear'): {('Paris', 'alice'): 1985, ('Paris', 'bob'): 1984, ('London', 'charles'): 1992}, ('public', 'hobby'): {('Paris', 'alice'): 'Biking', ('Paris', 'bob'): 'Dancing', ('London', 'charles'): np.nan}, ('private', 'weight'): {('Paris', 'alice'): 68, ('Paris', 'bob'): 83, ('London', 'charles'): 112}, ('private', 'children'): {('Paris', 'alice'): np.nan, ('Paris', 'bob'): 3.0, ('London', 'charles'): 0.0}})
  ```

  + which outputs:

  ```
                      public          private
                   birthyear    hobby  weight children
    Paris  alice        1985   Biking      68      NaN
           bob          1984  Dancing      83      3.0
    London charles      1992      NaN     112      0.0
  ```
* There are two levels of columns, and two levels of indices. We can drop a column level by calling `droplevel()` (the same goes for indices):

  ```
    d5.columns = d5.columns.droplevel(level = 0)
    d5
  ```

  + which outputs:

  ```
                    birthyear    hobby  weight  children
    Paris  alice         1985   Biking      68       NaN
           bob           1984  Dancing      83       3.0
    London charles       1992      NaN     112       0.0
  ```

### Transposing

* You can swap columns and indices using the `T` attribute:

  ```
    import pandas as pd

    d5 = pd.DataFrame({'birthyear': {('Paris', 'alice'): 1985, ('Paris', 'bob'): 1984, ('London', 'charles'): 1992}, 'hobby': {('Paris', 'alice'): 'Biking', ('Paris', 'bob'): 'Dancing', ('London', 'charles'): nan}, 'weight': {('Paris', 'alice'): 68, ('Paris', 'bob'): 83, ('London', 'charles'): 112}, 'children': {('Paris', 'alice'): nan, ('Paris', 'bob'): 3.0, ('London', 'charles'): 0.0}})

    d6 = d5.T
    d6
  ```

  + which outputs:

  ```
                Paris           London
                alice      bob charles
    birthyear    1985     1984    1992
    hobby      Biking  Dancing     NaN
    weight         68       83     112
    children      NaN        3       0
  ```

### Stacking and unstacking levels

* Calling the `stack()` method will push the lowest column level after the lowest index:

  ```
    import pandas as pd

    d6 = pd.DataFrame({('Paris', 'alice'): {'birthyear': 1985, 'hobby': 'Biking', 'weight': 68, 'children': nan}, ('Paris', 'bob'): {'birthyear': 1984, 'hobby': 'Dancing', 'weight': 83, 'children': 3.0}, ('London', 'charles'): {'birthyear': 1992, 'hobby': nan, 'weight': 112, 'children': 0.0}})

    d7 = d6.stack()
    d7
  ```

  + which outputs:

  ```
                      London    Paris
    birthyear alice      NaN     1985
              bob        NaN     1984
              charles   1992      NaN
    hobby     alice      NaN   Biking
              bob        NaN  Dancing
    weight    alice      NaN       68
              bob        NaN       83
              charles    112      NaN
    children  bob        NaN        3
              charles      0      NaN
  ```
* Note that many `NaN` values appeared. This makes sense because many new combinations did not exist before (eg. there was no `bob` in `London`).
* Calling `unstack()` will do the reverse, once again creating many `NaN` values.

  ```
    d8 = d7.unstack()
    d8
  ```

  + which outputs:

  ```
              London                Paris
               alice  bob charles   alice      bob charles
    birthyear    NaN  NaN    1992    1985     1984     NaN
    hobby        NaN  NaN     NaN  Biking  Dancing     NaN
    weight       NaN  NaN     112      68       83     NaN
    children     NaN  NaN       0     NaN        3     NaN
  ```
* If we call `unstack` again, we end up with a `Series` object:

  ```
    d9 = d8.unstack()
    d9
  ```

  + which outputs:

  ```
    London  alice    birthyear        NaN
                     hobby            NaN
                     weight           NaN
                     children         NaN
            bob      birthyear        NaN
                     hobby            NaN
                     weight           NaN
                     children         NaN
            charles  birthyear       1992
                     hobby            NaN
                     weight           112
                     children           0
    Paris   alice    birthyear       1985
                     hobby         Biking
                     weight            68
                     children         NaN
            bob      birthyear       1984
                     hobby        Dancing
                     weight            83
                     children           3
            charles  birthyear        NaN
                     hobby            NaN
                     weight           NaN
                     children         NaN
    dtype: object
  ```
* The `stack()` and `unstack()` methods let you select the `level` to stack/unstack. You can even stack/unstack multiple levels at once:

  ```
    d10 = d9.unstack(level = (0,1))
    d10
  ```

  + which outputs:

  ```
              London                Paris
               alice  bob charles   alice      bob charles
    birthyear    NaN  NaN    1992    1985     1984     NaN
    hobby        NaN  NaN     NaN  Biking  Dancing     NaN
    weight       NaN  NaN     112      68       83     NaN
    children     NaN  NaN       0     NaN        3     NaN
  ```

### Most methods return modified copies

* As you may have noticed, the `stack()` and `unstack()` methods do not modify the object they apply to. Instead, they work on a copy and return that copy. This is true of most methods in pandas.

### Accessing rows

* Let’s go back to the `people` `DataFrame`:

  ```
    import pandas as pd

    people_dict = {
        "birthyear": pd.Series([1984, 1985, 1992], index=["bob", "alice", "charles"], name="year"),
        "hobby": pd.Series(["Biking", "Dancing"], index=["alice", "bob"]),
        "weight": pd.Series([68, 83, 112], index=["alice", "bob", "charles"]),
        "children": pd.Series([0, 3], index=["charles", "bob"]),
    }

    people = pd.DataFrame(people_dict)
    people
  ```

  + which outputs:

  ```
             birthyear    hobby  weight  children
    alice         1985   Biking      68       NaN
    bob           1984  Dancing      83       3.0
    charles       1992      NaN     112       0.0
  ```
* The `loc` attribute lets you access rows instead of columns. The result is a `Series` object in which the `DataFrame`’s column names are mapped to row index labels:

  ```
    people.loc["charles"]
  ```

  + which outputs:

  ```
    birthyear    1992
    hobby         NaN
    weight        112
    children        0
    Name: charles, dtype: object
  ```
* You can also access rows by integer location using the `iloc` attribute:

  ```
    people.iloc[2]
  ```

  + which outputs:

  ```
    birthyear    1992
    hobby         NaN
    weight        112
    children        0
    Name: charles, dtype: object
  ```
* You can also get a slice of rows, and this returns a `DataFrame` object:

  ```
    people.iloc[1:3]
  ```

  + which outputs:

  ```
             birthyear    hobby  weight  children
    bob           1984  Dancing      83       3.0
    charles       1992      NaN     112       0.0
  ```
* Finally, you can pass a boolean array to get the matching rows:

  ```
    people[np.array([True, False, True])]
  ```

  + which outputs:

  ```
             birthyear   hobby  weight  children
    alice         1985  Biking      68       NaN
    charles       1992     NaN     112       0.0
  ```
* This is most useful when combined with boolean expressions:

  ```
    people[people["birthyear"] < 1990]
  ```

  + which outputs:

  ```
           birthyear    hobby  weight  children
    alice       1985   Biking      68       NaN
    bob         1984  Dancing      83       3.0
  ```

### Adding and removing columns

* Again, let’s go back to the `people` `DataFrame`:

  ```
    import pandas as pd

    people_dict = {
        "birthyear": pd.Series([1984, 1985, 1992], index=["bob", "alice", "charles"], name="year"),
        "hobby": pd.Series(["Biking", "Dancing"], index=["alice", "bob"]),
        "weight": pd.Series([68, 83, 112], index=["alice", "bob", "charles"]),
        "children": pd.Series([0, 3], index=["charles", "bob"]),
    }

    people = pd.DataFrame(people_dict)
    people
  ```

  + which outputs:

  ```
             birthyear    hobby  weight  children
    alice         1985   Biking      68       NaN
    bob           1984  Dancing      83       3.0
    charles       1992      NaN     112       0.0
  ```
* You can generally treat `DataFrame` objects like dictionaries of `Series`, so adding new columns can be accomplished using:

  ```
    people["age"] = 2018 - people["birthyear"] # adds a new column "age"
    people["over 30"] = people["age"] > 30     # adds another column "over 30"
    birthyears = people.pop("birthyear")
    del people["children"]
    people
  ```

  + which outputs:

  ```
               hobby  weight  age  over 30
    alice     Biking      68   33     True
    bob      Dancing      83   34     True
    charles      NaN     112   26    False
  ```
* We can print `birthyears` using:

  ```
    birthyears
  ```

  + which outputs:

  ```
    alice      1985
    bob        1984
    charles    1992
    Name: birthyear, dtype: int64
  ```
* When you add a new column, it must have the same number of rows. Missing rows are filled with NaN, and extra rows are ignored:

  ```
    people["pets"] = pd.Series({"bob": 0, "charles": 5, "eugene": 1}) # alice is missing, eugene is ignored
    people
  ```

  + which outputs:

  ```
               hobby  weight  age  over 30  pets
    alice     Biking      68   33     True   NaN
    bob      Dancing      83   34     True   0.0
    charles      NaN     112   26    False   5.0
  ```
* When adding a new column, it is added at the end (on the right) by default. You can also insert a column anywhere else using the `insert()` method:

  ```
    people.insert(1, "height", [172, 181, 185])
    people
  ```

  + which outputs:

  ```
               hobby  height  weight  age  over 30  pets
    alice     Biking     172      68   33     True   NaN
    bob      Dancing     181      83   34     True   0.0
    charles      NaN     185     112   26    False   5.0
  ```

#### Assigning new columns

* Again, let’s go back to the `people` `DataFrame`:

  ```
    import pandas as pd

    people_dict = {
        "hobby": pd.Series(["Biking", "Dancing"], index=["alice", "bob"]),
        "height": pd.Series([172, 181, 185], index=["alice", "bob", "charles"]),
        "weight": pd.Series([68, 83, 112], index=["alice", "bob", "charles"]),
        "age": pd.Series([33, 34, 26], index=["alice", "bob", "charles"]),
        "over 30": pd.Series([True, True, False], index=["alice", "bob", "charles"]),
        "pets": pd.Series({"bob": 0.0, "charles": 5.0}),
    }

    people = pd.DataFrame(people_dict)
    people
  ```

  + which outputs:

  ```
               hobby  height  weight  age  over 30  pets
    alice     Biking     172      68   33     True   NaN
    bob      Dancing     181      83   34     True   0.0
    charles      NaN     185     112   26    False   5.0
  ```
* You can also create new columns by calling the `assign()` method. Note that this returns a new `DataFrame` object, the original is not modified:

  ```
    people.assign(
        body_mass_index = people["weight"] / (people["height"] / 100) ** 2,
        has_pets = people["pets"] > 0
    )
  ```

  + which outputs:

  ```
             weight  height    hobby  age  over 30  pets  body_mass_index  has_pets
    alice        68     172   Biking   33     True   NaN        22.985398     False
    bob          83     181  Dancing   34     True   0.0        25.335002     False
    charles     112     185      NaN   26    False   5.0        32.724617      True
  ```
* Note that you cannot access columns created within the same assignment:

  ```
    try:
        people.assign(
            body_mass_index = people["weight"] / (people["height"] / 100) ** 2,
            overweight = people["body_mass_index"] > 25
        )
    except KeyError as e:
        print("Key error:", e)
  ```

  + which outputs:

  ```
    Key error: 'body_mass_index'
  ```
* The solution is to split this assignment in two consecutive assignments:

  ```
    d6 = people.assign(body_mass_index = people["weight"] / (people["height"] / 100) ** 2)
    d6.assign(overweight = d6["body_mass_index"] > 25)
  ```

  + which outputs:

  ```
               hobby  height  weight  age  over 30  pets  body_mass_index  overweight
    alice     Biking     172      68   33     True   NaN        22.985398       False
    bob      Dancing     181      83   34     True   0.0        25.335002        True
    charles      NaN     185     112   26    False   5.0        32.724617        True
  ```
* Having to create a temporary variable `d6` is not very convenient. You may want to just chain the assigment calls, but it does not work because the `people` object is not actually modified by the first assignment:

  ```
    try:
        (people
             .assign(body_mass_index = people["weight"] / (people["height"] / 100) ** 2)
             .assign(overweight = people["body_mass_index"] > 25)
        )
    except KeyError as e:
        print("Key error:", e)
  ```
* which outputs:

  ```
    Key error: 'body_mass_index'
  ```
* But fear not, there is a simple solution. You can pass a function to the `assign()` method (typically a `lambda` function), and this function will be called with the `DataFrame` as a parameter:

  ```
    (people
         .assign(body_mass_index = lambda df: df["weight"] / (df["height"] / 100) ** 2)
         .assign(overweight = lambda df: df["body_mass_index"] > 25)
    )
  ```
* which outputs:

  ```
               hobby  height  weight  age  over 30  pets  body_mass_index  overweight
    alice     Biking     172      68   33     True   NaN        22.985398       False
    bob      Dancing     181      83   34     True   0.0        25.335002        True
    charles      NaN     185     112   26    False   5.0        32.724617        True
  ```
* Problem solved!

#### Evaluating an expression

* A great feature supported by pandas is expression evaluation. This relies on the `numexpr` library which must be installed.

  ```
    import pandas as pd

    people.eval("weight / (height/100) ** 2 > 25")
  ```

  + which outputs:

  ```
    alice      False
    bob         True
    charles     True
    dtype: bool
  ```
* Assignment expressions are also supported. Let’s set `inplace=True` to directly modify the `DataFrame` rather than getting a modified copy:

  ```
    people.eval("body_mass_index = weight / (height/100) ** 2", inplace=True)
    people
  ```

  + which outputs:

  ```
               hobby  height  weight  age  over 30  pets  body_mass_index
    alice     Biking     172      68   33     True   NaN        22.985398
    bob      Dancing     181      83   34     True   0.0        25.335002
    charles      NaN     185     112   26    False   5.0        32.724617
  ```
* You can use a local or global variable in an expression by prefixing it with `'@'`:

  ```
    overweight_threshold = 30
    people.eval("overweight = body_mass_index > @overweight_threshold", inplace=True)
    people
  ```

  + which outputs:

  ```
               hobby  height  weight  age  over 30  pets  body_mass_index  overweight
    alice     Biking     172      68   33     True   NaN        22.985398       False
    bob      Dancing     181      83   34     True   0.0        25.335002       False
    charles      NaN     185     112   26    False   5.0        32.724617        True
  ```

#### Querying a `DataFrame`

* The `query()` method lets you filter a `DataFrame` based on a query expression:

  ```
    people.query("age > 30 and pets == 0")
  ```

  + which outputs:

  ```
           hobby  height  weight  age  over 30  pets  body_mass_index  overweight
    bob  Dancing     181      83   34     True   0.0        25.335002       False
  ```

#### Sorting a `DataFrame`

* You can sort a `DataFrame` by calling its `sort_index` method. By default, it sorts the rows by their index label in ascending order, but let’s reverse the order:

  ```
    people.sort_index(ascending=False)
  ```

  + which outputs:

  ```
               hobby  height  weight  age  over 30  pets  body_mass_index  overweight
    charles      NaN     185     112   26    False   5.0        32.724617        True
    bob      Dancing     181      83   34     True   0.0        25.335002       False
    alice     Biking     172      68   33     True   NaN        22.985398       False
  ```
* Note that `sort_index` returned a sorted **copy** of the `DataFrame`. To modify `people` directly, we can set the `inplace` argument to `True`. Also, we can sort the columns instead of the rows by setting `axis=1`:

  ```
    people.sort_index(axis=1, inplace=True)
    people
  ```

  + which outputs:

  ```
             age  body_mass_index  height    hobby  over 30  overweight  pets  weight
    alice     33        22.985398     172   Biking     True       False   NaN      68
    bob       34        25.335002     181  Dancing     True       False   0.0      83
    charles   26        32.724617     185      NaN    False        True   5.0     112
  ```
* To sort the `DataFrame` by the values instead of the labels, we can use `sort_values` and specify the column to sort by:

  ```
    people.sort_values(by="age", inplace=True)
    people
  ```

  + which outputs:

  ```
             age  body_mass_index  height    hobby  over 30  overweight  pets  weight
    charles   26        32.724617     185      NaN    False        True   5.0     112
    alice     33        22.985398     172   Biking     True       False   NaN      68
    bob       34        25.335002     181  Dancing     True       False   0.0      83
  ```

#### Plotting a `DataFrame`

* Just like for `Series`, pandas makes it easy to draw nice graphs based on a `DataFrame`.
* For example, it is trivial to create a line plot from a `DataFrame`’s data by calling its `plot` method:

  ```
    import pandas as pd
      
    people.plot(kind = "line", x = "body_mass_index", y = ["height", "weight"])
    plt.show()
  ```

  + which outputs:
* You can pass extra arguments supported by matplotlib’s functions. For example, we can create scatterplot and pass it a list of sizes using the `s` argument of matplotlib’s `scatter()` function:

  ```
    people.plot(kind = "scatter", x = "height", y = "weight", s=[40, 120, 200])
    plt.show()
  ```

  + which outputs:
* Again, there are way too many options to list here: the best option is to scroll through the [Visualization](http://pandas.pydata.org/pandas-docs/stable/visualization.html) page in pandas’ documentation, find the plot you are interested in and look at the example code.

#### Operations on `DataFrame`s

* Although `DataFrame`s do not try to mimick NumPy arrays, there are a few similarities. Let’s create a `DataFrame` to demonstrate this:

  ```
    import pandas as pd

    grades_array = np.array([[8, 8, 9], [10, 9, 9], [4, 8, 2], [9, 10, 10]])
    grades = pd.DataFrame(grades_array, columns=["sep", "oct", "nov"], index=["alice","bob","charles","darwin"])
    grades
  ```

  + which outputs:

  ```
             sep  oct  nov
    alice      8    8    9
    bob       10    9    9
    charles    4    8    2
    darwin     9   10   10
  ```
* You can apply NumPy mathematical functions on a `DataFrame`: the function is applied to all values:

  ```
    np.sqrt(grades)
  ```

  + which outputs:

  ```
                  sep       oct       nov
    alice    2.828427  2.828427  3.000000
    bob      3.162278  3.000000  3.000000
    charles  2.000000  2.828427  1.414214
    darwin   3.000000  3.162278  3.162278
  ```
* Similarly, adding a single value to a `DataFrame` will add that value to all elements in the `DataFrame`. This is called **broadcasting**:

  ```
    grades + 1
  ```

  + which outputs:

  ```
             sep  oct  nov
    alice      9    9   10
    bob       11   10   10
    charles    5    9    3
    darwin    10   11   11
  ```
* Of course, the same is true for all other binary operations, including arithmetic (`*`,`/`,`**`…) and conditional (`>`, `==`…) operations:

  ```
    grades >= 5
  ```

  + which outputs:

  ```
               sep   oct    nov
    alice     True  True   True
    bob       True  True   True
    charles  False  True  False
    darwin    True  True   True
  ```
* Aggregation operations, such as computing the `max`, the `sum` or the `mean` of a `DataFrame`, apply to each column, and you get back a `Series` object:

  ```
    grades.mean()
  ```

  + which outputs:

  ```
    sep    7.75
    oct    8.75
    nov    7.50
    dtype: float64
  ```
* The `all` method is also an aggregation operation: it checks whether all values are `True` or not. Let’s see during which months all students got a grade greater than `5`:

  ```
    (grades > 5).all()
  ```

  + which outputs:

  ```
    sep    False
    oct     True
    nov    False
    dtype: bool
  ```
* Most of these functions take an optional `axis` parameter which lets you specify along which axis of the `DataFrame` you want the operation executed. The default is `axis=0`, meaning that the operation is executed vertically (on each column). You can set `axis=1` to execute the operation horizontally (on each row). For example, let’s find out which students had all grades greater than `5`:

  ```
    (grades > 5).all(axis = 1)
  ```

  + which outputs:

  ```
    alice       True
    bob         True
    charles    False
    darwin      True
    dtype: bool
  ```
* The `any` method returns `True` if any value is True. Let’s see who got at least one grade 10:

  ```
    (grades == 10).any(axis = 1)
  ```

  + which outputs:

  ```
    alice      False
    bob         True
    charles    False
    darwin      True
    dtype: bool
  ```
* If you add a `Series` object to a `DataFrame` (or execute any other binary operation), pandas attempts to broadcast the operation to all **rows** in the `DataFrame`. This only works if the `Series` has the same size as the `DataFrame`s rows. For example, let’s subtract the `mean` of the `DataFrame` (a `Series` object) from the `DataFrame`:

  ```
    grades - grades.mean() # equivalent to: grades - [7.75, 8.75, 7.50]
  ```

  + which outputs:

  ```
              sep   oct  nov
    alice    0.25 -0.75  1.5
    bob      2.25  0.25  1.5
    charles -3.75 -0.75 -5.5
    darwin   1.25  1.25  2.5
  ```
* We subtracted `7.75` from all September grades, `8.75` from October grades and `7.50` from November grades. It is equivalent to substracting this `DataFrame`:

  ```
    pd.DataFrame([[7.75, 8.75, 7.50]]*4, index=grades.index, columns=grades.columns)
  ```

  + which outputs:

  ```
              sep   oct  nov
    alice    7.75  8.75  7.5
    bob      7.75  8.75  7.5
    charles  7.75  8.75  7.5
    darwin   7.75  8.75  7.5
  ```
* If you want to subtract the global mean from every grade, here is one way to do it:

  ```
    grades - grades.values.mean() # subtracts the global mean (8.00) from all grades
  ```

  + which outputs:

  ```
             sep  oct  nov
    alice    0.0  0.0  1.0
    bob      2.0  1.0  1.0
    charles -4.0  0.0 -6.0
    darwin   1.0  2.0  2.0
  ```

#### Automatic alignment

* Similar to `Series`, when operating on multiple `DataFrame`s, pandas automatically aligns them by row index label, but also by column names. Let’s start with our previous grades `DataFrame` to demonstrate this:

  ```
    import pandas as pd

    grades_array = np.array([[8, 8, 9], [10, 9, 9], [4, 8, 2], [9, 10, 10]])
    grades = pd.DataFrame(grades_array, columns=["sep", "oct", "nov"], index=["alice", "bob", "charles", "darwin"])
    grades
  ```

  + which outputs:

  ```
             sep  oct  nov
    alice      8    8    9
    bob       10    9    9
    charles    4    8    2
    darwin     9   10   10
  ```
* Now, let’s create a new `DataFrame` that holds the bonus points for each person from October to December:

  ```
    import numpy as np

    bonus_array = np.array([[0, np.nan, 2],[np.nan, 1, 0],[0, 1, 0], [3, 3, 0]])
    bonus_points = pd.DataFrame(bonus_array, columns=["oct", "nov", "dec"], index=["bob", "colin", "darwin", "charles"])
    bonus_points
  ```

  + which outputs:

  ```
             oct  nov  dec
    bob      0.0  NaN  2.0
    colin    NaN  1.0  0.0
    darwin   0.0  1.0  0.0
    charles  3.0  3.0  0.0
  ```
* Now, let’s combine both `DataFrame`s:

  ```
    grades + bonus_points
  ```

  + which outputs:

  ```
             dec   nov   oct  sep
    alice    NaN   NaN   NaN  NaN
    bob      NaN   NaN   9.0  NaN
    charles  NaN   5.0  11.0  NaN
    colin    NaN   NaN   NaN  NaN
    darwin   NaN  11.0  10.0  NaN
  ```
* Looks like the addition worked in some cases but way too many elements are now empty. That’s because when aligning the `DataFrame`s, some columns and rows were only present on one side, and thus they were considered missing on the other side (`NaN`). Then adding `NaN` to a number results in `NaN`, hence the result.

#### Handling missing data

* Dealing with missing data is a frequent task when working with real life data. Pandas offers a few tools to handle missing data.
* Let’s try to fix the problem seen in the above section on [automatic alignment](#automatic-alignment). Let’s start with our previous grades `DataFrame` to demonstrate this:

  ```
    import pandas as pd

    grades = pd.DataFrame({'sep': {'alice': 8, 'bob': 10, 'charles': 4, 'darwin': 9}, 'oct': {'alice': 8, 'bob': 9, 'charles': 8, 'darwin': 10}, 'nov': {'alice': 9, 'bob': 9, 'charles': 2, 'darwin': 10}})
    grades
  ```

  + which outputs:

  ```
             sep  oct  nov
    alice      8    8    9
    bob       10    9    9
    charles    4    8    2
    darwin     9   10   10
  ```
* Now, let’s create a new `DataFrame` that holds the bonus points for each person from October to December:

  ```
    import numpy as np

    bonus_points = pd.DataFrame({'oct': {'bob': 0.0, 'colin': np.nan, 'darwin': 0.0, 'charles': 3.0}, 'nov': {'bob': np.nan, 'colin': 1.0, 'darwin': 1.0, 'charles': 3.0}, 'dec': {'bob': 2.0, 'colin': 0.0, 'darwin': 0.0, 'charles': 0.0}})
    bonus_points
  ```

  + which outputs:

  ```
             oct  nov  dec
    bob      0.0  NaN  2.0
    colin    NaN  1.0  0.0
    darwin   0.0  1.0  0.0
    charles  3.0  3.0  0.0
  ```
* For example, we can decide that missing data should result in a zero, instead of `NaN`. We can replace all `NaN` values by a any value using the `fillna()` method:

  ```
    (grades + bonus_points).fillna(0)
  ```

  + which outputs:

  ```
             dec   nov   oct  sep
    alice    0.0   0.0   0.0  0.0
    bob      0.0   0.0   9.0  0.0
    charles  0.0   5.0  11.0  0.0
    colin    0.0   0.0   0.0  0.0
    darwin   0.0  11.0  10.0  0.0
  ```
* It’s a bit unfair that we’re setting grades to zero in September, though. Perhaps we should decide that missing grades are missing grades, but missing bonus points should be replaced by zeros:

  ```
    fixed_bonus_points = bonus_points.fillna(0)
    fixed_bonus_points.insert(0, "sep", 0)
    fixed_bonus_points.loc["alice"] = 0
    grades + fixed_bonus_points
  ```

  + which outputs:

  ```
             dec   nov   oct   sep
    alice    NaN   9.0   8.0   8.0
    bob      NaN   9.0   9.0  10.0
    charles  NaN   5.0  11.0   4.0
    colin    NaN   NaN   NaN   NaN
    darwin   NaN  11.0  10.0   9.0
  ```
* That’s much better: although we made up some data, we have not been too unfair.
* Another way to handle missing data is to interpolate. Let’s look at the `bonus_points` `DataFrame` again:

  ```
    bonus_points
  ```

  + which outputs:

  ```
             oct  nov  dec
    bob      0.0  NaN  2.0
    colin    NaN  1.0  0.0
    darwin   0.0  1.0  0.0
    charles  3.0  3.0  0.0
  ```
* Now let’s call the `interpolate` method. By default, it interpolates vertically (`axis=0`), so let’s tell it to interpolate horizontally (`axis=1`).

  ```
    bonus_points.interpolate(axis=1)
  ```

  + which outputs:

  ```
             oct  nov  dec
    bob      0.0  1.0  2.0
    colin    NaN  1.0  0.0
    darwin   0.0  1.0  0.0
    charles  3.0  3.0  0.0
  ```
* Bob had 0 bonus points in October, and 2 in December. When we interpolate for November, we get the mean: 1 bonus point. Colin had 1 bonus point in November, but we do not know how many bonus points he had in September, so we cannot interpolate, this is why there is still a missing value in October after interpolation. To fix this, we can set the September bonus points to 0 before interpolation.

  ```
    better_bonus_points = bonus_points.copy()
    better_bonus_points.insert(0, "sep", 0)
    better_bonus_points.loc["alice"] = 0
    better_bonus_points = better_bonus_points.interpolate(axis=1)
    better_bonus_points
  ```

  + which outputs:

  ```
             sep  oct  nov  dec
    bob      0.0  0.0  1.0  2.0
    colin    0.0  0.5  1.0  0.0
    darwin   0.0  0.0  1.0  0.0
    charles  0.0  3.0  3.0  0.0
    alice    0.0  0.0  0.0  0.0
  ```
* Great, now we have reasonable bonus points everywhere. Let’s find out the final grades:

  ```
    grades + better_bonus_points
  ```

  + which outputs:

  ```
             dec   nov   oct   sep
    alice    NaN   9.0   8.0   8.0
    bob      NaN  10.0   9.0  10.0
    charles  NaN   5.0  11.0   4.0
    colin    NaN   NaN   NaN   NaN
    darwin   NaN  11.0  10.0   9.0
  ```
* It is slightly annoying that the September column ends up on the right. This is because the `DataFrame`s we are adding do not have the exact same columns (the `grades` `DataFrame` is missing the `"dec"` column), so to make things predictable, pandas orders the final columns alphabetically. To fix this, we can simply add the missing column before adding:

  ```
    import numpy as np

    grades["dec"] = np.nan
    final_grades = grades + better_bonus_points
    final_grades
  ```

  + which outputs:

  ```
              sep   oct   nov  dec
    alice     8.0   8.0   9.0  NaN
    bob      10.0   9.0  10.0  NaN
    charles   4.0  11.0   5.0  NaN
    colin     NaN   NaN   NaN  NaN
    darwin    9.0  10.0  11.0  NaN
  ```
* There’s not much we can do about December and Colin: it’s bad enough that we are making up bonus points, but we can’t reasonably make up grades (well I guess some teachers probably do). So let’s call the `dropna()` method to get rid of rows that are full of `NaN`s:

  ```
    final_grades_clean = final_grades.dropna(how="all")
    final_grades_clean
  ```

  + which outputs:

  ```
              sep   oct   nov  dec
    alice     8.0   8.0   9.0  NaN
    bob      10.0   9.0  10.0  NaN
    charles   4.0  11.0   5.0  NaN
    darwin    9.0  10.0  11.0  NaN
  ```
* Now let’s remove columns that are full of `NaN`s by setting the `axis` argument to `1`:

  ```
    final_grades_clean = final_grades_clean.dropna(axis=1, how="all")
    final_grades_clean
  ```

  + which outputs:

  ```
              sep   oct   nov
    alice     8.0   8.0   9.0
    bob      10.0   9.0  10.0
    charles   4.0  11.0   5.0
    darwin    9.0  10.0  11.0
  ```

#### Aggregating with `groupby`

* Similar to the SQL language, pandas allows grouping your data into groups to run calculations over each group.
* First, let’s add some extra data about each person so we can group them, and let’s go back to the `final_grades` `DataFrame` so we can see how `NaN` values are handled:

  ```
    import numpy as np

    final_grades = pd.DataFrame({'sep': {'alice': 8.0, 'bob': 10.0, 'charles': 4.0, 'colin': np.nan, 'darwin': 9.0}, 'oct': {'alice': 8.0, 'bob': 9.0, 'charles': 11.0, 'colin': np.nan, 'darwin': 10.0}, 'nov': {'alice': 9.0, 'bob': 10.0, 'charles': 5.0, 'colin': np.nan, 'darwin': 11.0}, 'dec': {'alice': np.nan, 'bob': np.nan, 'charles': np.nan, 'colin': np.nan, 'darwin': np.nan}})
    final_grades
  ```
* Adding a new column “hobby” to `final_grades`:

  ```
    final_grades["hobby"] = ["Biking", "Dancing", np.nan, "Dancing", "Biking"]
    final_grades
  ```

  + which outputs:

  ```
              sep   oct   nov  dec    hobby
    alice     8.0   8.0   9.0  NaN   Biking
    bob      10.0   9.0  10.0  NaN  Dancing
    charles   4.0  11.0   5.0  NaN      NaN
    colin     NaN   NaN   NaN  NaN  Dancing
    darwin    9.0  10.0  11.0  NaN   Biking
  ```
* Now let’s group data in this `DataFrame` by hobby:

  ```
    grouped_grades = final_grades.groupby("hobby")
    grouped_grades
  ```

  + which outputs:

  ```
    <pandas.core.groupby.generic.DataFrameGroupBy object at [address]>
  ```
* We are ready to compute the average grade per hobby:

  ```
    grouped_grades.mean()
  ```

  + which outputs:

  ```
              sep  oct   nov  dec
    hobby
    Biking    8.5  9.0  10.0  NaN
    Dancing  10.0  9.0  10.0  NaN
  ```
* That was easy! Note that the `NaN` values have simply been skipped when computing the means.

#### Pivot tables

* Pandas supports spreadsheet-like [pivot tables](https://en.wikipedia.org/wiki/Pivot_table) that allow quick data summarization. To illustrate this, let’s start with our `DataFrame`:

  ```
    final_grades_clean = {'sep': {'alice': 8.0, 'bob': 10.0, 'charles': 4.0, 'darwin': 9.0}, 'oct': {'alice': 8.0, 'bob': 9.0, 'charles': 11.0, 'darwin': 10.0}, 'nov': {'alice': 9.0, 'bob': 10.0, 'charles': 5.0, 'darwin': 11.0}}
    final_grades_clean
  ```

  + which outputs:

  ```
             oct  nov  dec
    bob      0.0  NaN  2.0
    colin    NaN  1.0  0.0
    darwin   0.0  1.0  0.0
    charles  3.0  3.0  0.0
  ```
* Now let’s restructure the data:

  ```
    more_grades = final_grades_clean.stack().reset_index()
    more_grades.columns = ["name", "month", "grade"]
    more_grades["bonus"] = [np.nan, np.nan, np.nan, 0, np.nan, 2, 3, 3, 0, 0, 1, 0]
    more_grades
  ```

  + which outputs:

  ```
           name month  grade  bonus
    0     alice   sep    8.0    NaN
    1     alice   oct    8.0    NaN
    2     alice   nov    9.0    NaN
    3       bob   sep   10.0    0.0
    4       bob   oct    9.0    NaN
    5       bob   nov   10.0    2.0
    6   charles   sep    4.0    3.0
    7   charles   oct   11.0    3.0
    8   charles   nov    5.0    0.0
    9    darwin   sep    9.0    0.0
    10   darwin   oct   10.0    1.0
    11   darwin   nov   11.0    0.0
  ```
* Now we can call the `pd.pivot_table()` function for this `DataFrame`, asking to group by the `name` column. By default, `pivot_table()` computes the mean of each numeric column:

  ```
    pd.pivot_table(more_grades, index="name")
  ```

  + which outputs:

  ```
                bonus      grade
    name
    alice         NaN   8.333333
    bob      1.000000   9.666667
    charles  2.000000   6.666667
    darwin   0.333333  10.000000
  ```
* We can change the aggregation function by setting the `aggfunc` argument, and we can also specify the list of columns whose values will be aggregated:

  ```
    pd.pivot_table(more_grades, index="name", values=["grade","bonus"], aggfunc=np.max)
  ```

  + which outputs:

  ```
             bonus  grade
    name
    alice      NaN    9.0
    bob        2.0   10.0
    charles    3.0   11.0
    darwin     1.0   11.0
  ```
* We can also specify the `columns` to aggregate over horizontally, and request the grand totals for each row and column by setting `margins=True`:

  ```
    pd.pivot_table(more_grades, index="name", values="grade", columns="month", margins=True)
  ```

  + which outputs:

  ```
    month      nov   oct    sep        All
    name
    alice     9.00   8.0   8.00   8.333333
    bob      10.00   9.0  10.00   9.666667
    charles   5.00  11.0   4.00   6.666667
    darwin   11.00  10.0   9.00  10.000000
    All       8.75   9.5   7.75   8.666667
  ```
* Finally, we can specify multiple index or column names, and pandas will create multi-level indices:

  ```
    pd.pivot_table(more_grades, index=("name", "month"), margins=True)
  ```

  + which outputs:

  ```
                   bonus  grade
    name    month
    alice   nov      NaN   9.00
            oct      NaN   8.00
            sep      NaN   8.00
    bob     nov    2.000  10.00
            oct      NaN   9.00
            sep    0.000  10.00
    charles nov    0.000   5.00
            oct    3.000  11.00
            sep    3.000   4.00
    darwin  nov    0.000  11.00
            oct    1.000  10.00
            sep    0.000   9.00
    All            1.125   8.75
  ```

#### Overview functions

* When dealing with large `DataFrames`, it is useful to get a quick overview of its content. Pandas offers a few functions for this. First, let’s create a large `DataFrame` with a mix of numeric values, missing values and text values. Notice how Jupyter displays only the corners of the `DataFrame`:

  ```
    much_data = np.fromfunction(lambda x,y: (x+y*y)%17*11, (10000, 26))
    large_df = pd.DataFrame(much_data, columns=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    large_df[large_df % 16 == 0] = np.nan
    large_df.insert(3,"some_text", "Blabla")
    large_df
  ```

  + which outputs:

  ```
             A     B     C some_text      D  ...      V      W     X      Y      Z
    0      NaN  11.0  44.0    Blabla   99.0  ...    NaN   88.0  22.0  165.0  143.0
    1     11.0  22.0  55.0    Blabla  110.0  ...    NaN   99.0  33.0    NaN  154.0
    2     22.0  33.0  66.0    Blabla  121.0  ...   11.0  110.0  44.0    NaN  165.0
    3     33.0  44.0  77.0    Blabla  132.0  ...   22.0  121.0  55.0   11.0    NaN
    4     44.0  55.0  88.0    Blabla  143.0  ...   33.0  132.0  66.0   22.0    NaN
    ...    ...   ...   ...       ...    ...  ...    ...    ...   ...    ...    ...
    9995   NaN   NaN  33.0    Blabla   88.0  ...  165.0   77.0  11.0  154.0  132.0
    9996   NaN  11.0  44.0    Blabla   99.0  ...    NaN   88.0  22.0  165.0  143.0
    9997  11.0  22.0  55.0    Blabla  110.0  ...    NaN   99.0  33.0    NaN  154.0
    9998  22.0  33.0  66.0    Blabla  121.0  ...   11.0  110.0  44.0    NaN  165.0
    9999  33.0  44.0  77.0    Blabla  132.0  ...   22.0  121.0  55.0   11.0    NaN

    [10000 rows x 27 columns]
  ```
* The `head()` method returns the top 5 rows:

  ```
    large_df.head()
  ```

  + which outputs:

  ```
          A     B     C some_text      D  ...     V      W     X      Y      Z
    0   NaN  11.0  44.0    Blabla   99.0  ...   NaN   88.0  22.0  165.0  143.0
    1  11.0  22.0  55.0    Blabla  110.0  ...   NaN   99.0  33.0    NaN  154.0
    2  22.0  33.0  66.0    Blabla  121.0  ...  11.0  110.0  44.0    NaN  165.0
    3  33.0  44.0  77.0    Blabla  132.0  ...  22.0  121.0  55.0   11.0    NaN
    4  44.0  55.0  88.0    Blabla  143.0  ...  33.0  132.0  66.0   22.0    NaN

    [5 rows x 27 columns]
  ```
* Similarly, there’s also a `tail()` function to view the bottom 5 rows. You can pass the number of rows you want:

  ```
    large_df.tail(n=2)
  ```

  + which outputs:

  ```
             A     B     C some_text      D  ...     V      W     X     Y      Z
    9998  22.0  33.0  66.0    Blabla  121.0  ...  11.0  110.0  44.0   NaN  165.0
    9999  33.0  44.0  77.0    Blabla  132.0  ...  22.0  121.0  55.0  11.0    NaN

    [2 rows x 27 columns]
  ```
* The `info()` method prints out a summary of each columns contents:

  ```
    large_df.info()
  ```

  + which outputs:

  ```
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 10000 entries, 0 to 9999
    Data columns (total 27 columns):
    A            8823 non-null float64
    B            8824 non-null float64
    C            8824 non-null float64
    some_text    10000 non-null object
    D            8824 non-null float64
    E            8822 non-null float64
    F            8824 non-null float64
    G            8824 non-null float64
    H            8822 non-null float64
    I            8823 non-null float64
    J            8823 non-null float64
    K            8822 non-null float64
    L            8824 non-null float64
    M            8824 non-null float64
    N            8822 non-null float64
    O            8824 non-null float64
    P            8824 non-null float64
    Q            8824 non-null float64
    R            8823 non-null float64
    S            8824 non-null float64
    T            8824 non-null float64
    U            8824 non-null float64
    V            8822 non-null float64
    W            8824 non-null float64
    X            8824 non-null float64
    Y            8822 non-null float64
    Z            8823 non-null float64
    dtypes: float64(26), object(1)
    memory usage: 2.1+ MB
  ```
* Finally, the `describe()` method gives a nice overview of the main aggregated values over each column:

  + `count`: number of non-null (not NaN) values
  + `mean`: mean of non-null values
  + `std`: [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation)
    of non-null values
  + `min`: minimum of non-null values
  + `25%`, `50%`, `75%`: 25th, 50th and 75th
    [percentile](https://en.wikipedia.org/wiki/Percentile) of non-null values
  + `max`: maximum of non-null values

  ```
    large_df.describe()
  ```

  + which outputs:

  ```
                     A            B  ...            Y            Z
    count  8823.000000  8824.000000  ...  8822.000000  8823.000000
    mean     87.977559    87.972575  ...    88.000000    88.022441
    std      47.535911    47.535523  ...    47.536879    47.535911
    min      11.000000    11.000000  ...    11.000000    11.000000
    25%      44.000000    44.000000  ...    44.000000    44.000000
    50%      88.000000    88.000000  ...    88.000000    88.000000
    75%     132.000000   132.000000  ...   132.000000   132.000000
    max     165.000000   165.000000  ...   165.000000   165.000000

    [8 rows x 26 columns]
  ```

## Saving & loading

* Pandas can save `DataFrame`s to various backends, including file formats such as CSV, Excel, JSON, HTML and HDF5, or to a SQL database. Let’s create a `DataFrame` to demonstrate this:

  ```
    my_df = pd.DataFrame(
        [["Biking", 68.5, 1985, np.nan], ["Dancing", 83.1, 1984, 3]], 
        columns=["hobby","weight","birthyear","children"],
        index=["alice", "bob"]
    )
    my_df
  ```

  + which outputs:

  ```
             hobby  weight  birthyear  children
    alice   Biking    68.5       1985       NaN
    bob    Dancing    83.1       1984       3.0
  ```

#### Saving

* Let’s save it to CSV, HTML and JSON:

  ```
    my_df.to_csv("my_df.csv")
    my_df.to_html("my_df.html")
    my_df.to_json("my_df.json")
  ```
* Done! Let’s take a peek at what was saved:

  ```
    for filename in ("my_df.csv", "my_df.html", "my_df.json"):
        print("##", filename)
        with open(filename, "rt") as f:
            print(f.read())
            print()
  ```

  + which outputs:

  ```
    ## my_df.csv
    ,hobby,weight,birthyear,children
    alice,Biking,68.5,1985,
    bob,Dancing,83.1,1984,3.0

    ## my_df.html
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>hobby</th>
          <th>weight</th>
          <th>birthyear</th>
          <th>children</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>alice</th>
          <td>Biking</td>
          <td>68.5</td>
          <td>1985</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>bob</th>
          <td>Dancing</td>
          <td>83.1</td>
          <td>1984</td>
          <td>3.0</td>
        </tr>
      </tbody>
    </table>

    ## my_df.json
    {"hobby":{"alice":"Biking","bob":"Dancing"},"weight":{"alice":68.5,"bob":83.1},"birthyear":{"alice":1985,"bob":1984},"children":{"alice":null,"bob":3.0}}
  ```
* Note that the index is saved as the first column (with no name) in a CSV file, as `<th>` tags in HTML and as keys in JSON.
* Saving to other formats works very similarly, but some formats require extra libraries to be installed. For example, saving to Excel requires the `openpyxl` library:

  ```
    try:
        my_df.to_excel("my_df.xlsx", sheet_name='People')
    except ImportError as e:
        print(e)
  ```

  + which outputs:

  ```
    No module named 'openpyxl'
  ```

#### Loading

* Now let’s load our CSV file back into a `DataFrame`:

  ```
    my_df_loaded = pd.read_csv("my_df.csv", index_col=0)
    my_df_loaded
  ```

  + which outputs:

  ```
             hobby  weight  birthyear  children
    alice   Biking    68.5       1985       NaN
    bob    Dancing    83.1       1984       3.0
  ```
* As you might guess, there are similar `read_json`, `read_html`, `read_excel` functions as well. We can also read data straight from the Internet. For example, let’s load all U.S. cities from [simplemaps.com](http://simplemaps.com/):

  ```
    us_cities = None
    try:
        csv_url = "https://raw.githubusercontent.com/datasets/world-cities/master/data/world-cities.csv"
        us_cities = pd.read_csv(csv_url, index_col=0)
        us_cities = us_cities.head()
    except IOError as e:
        print(e)
          
    us_cities
  ```

  + which outputs:

  ```
                                   country          subcountry  geonameid
    name
    les Escaldes                   Andorra  Escaldes-Engordany    3040051
    Andorra la Vella               Andorra    Andorra la Vella    3041563
    Umm al Qaywayn    United Arab Emirates      Umm al Qaywayn     290594
    Ras al-Khaimah    United Arab Emirates     Raʼs al Khaymah     291074
    Khawr Fakkān      United Arab Emirates        Ash Shāriqah     291696
  ```
* There are more options available, in particular regarding datetime format. Check out the [documentation](http://pandas.pydata.org/pandas-docs/stable/io.html) for more details.

## Combining `DataFrame`s

#### SQL-like joins

* One powerful feature of pandas is it’s ability to perform SQL-like joins on `DataFrame`s. Various types of joins are supported: inner joins, left/right outer joins and full joins. To illustrate this, let’s start by creating a couple of simple `DataFrame`s.
* Here’s the city\_loc `DataFrame`:

  ```
    city_loc = pd.DataFrame(
        [
            ["CA", "San Francisco", 37.781334, -122.416728],
            ["NY", "New York", 40.705649, -74.008344],
            ["FL", "Miami", 25.791100, -80.320733],
            ["OH", "Cleveland", 41.473508, -81.739791],
            ["UT", "Salt Lake City", 40.755851, -111.896657]
        ], columns=["state", "city", "lat", "lng"])

    city_loc
  ```

  + which outputs:

  ```
      state            city        lat         lng
    0    CA   San Francisco  37.781334 -122.416728
    1    NY        New York  40.705649  -74.008344
    2    FL           Miami  25.791100  -80.320733
    3    OH       Cleveland  41.473508  -81.739791
    4    UT  Salt Lake City  40.755851 -111.896657
  ```

  ```
    city_pop = pd.DataFrame(
        [
            [808976, "San Francisco", "California"],
            [8363710, "New York", "New-York"],
            [413201, "Miami", "Florida"],
            [2242193, "Houston", "Texas"]
        ], index=[3,4,5,6], columns=["population", "city", "state"])

    city_pop
  ```

  + which outputs:

  ```
       population           city       state
    3      808976  San Francisco  California
    4     8363710       New York    New-York
    5      413201          Miami     Florida
    6     2242193        Houston       Texas
  ```
* Now let’s join these `DataFrame`s using the `merge()` function:

  ```
    pd.merge(left=city_loc, right=city_pop, on="city")
  ```

  + which outputs:

  ```
      state_x           city        lat         lng  population     state_y
    0      CA  San Francisco  37.781334 -122.416728      808976  California
    1      NY       New York  40.705649  -74.008344     8363710    New-York
    2      FL          Miami  25.791100  -80.320733      413201     Florida
  ```
* Note that both `DataFrame`s have a column named `state`, so in the result they got renamed to `state_x` and `state_y`.
* Also, note that Cleveland, Salt Lake City and Houston were dropped because they don’t exist in **both** `DataFrame`s. This is the equivalent of a SQL `INNER JOIN`. If you want a `FULL OUTER JOIN`, where no city gets dropped and `NaN` values are added, you must specify `how="outer"`:

  ```
    all_cities = pd.merge(left=city_loc, right=city_pop, on="city", how="outer")
    all_cities
  ```

  + which outputs:

  ```
      state_x            city        lat         lng  population     state_y
    0      CA   San Francisco  37.781334 -122.416728    808976.0  California
    1      NY        New York  40.705649  -74.008344   8363710.0    New-York
    2      FL           Miami  25.791100  -80.320733    413201.0     Florida
    3      OH       Cleveland  41.473508  -81.739791         NaN         NaN
    4      UT  Salt Lake City  40.755851 -111.896657         NaN         NaN
    5     NaN         Houston        NaN         NaN   2242193.0       Texas
  ```
* Of course `LEFT OUTER JOIN` is also available by setting `how="left"`: only the cities present in the left `DataFrame` end up in the result. Similarly, with `how="right"` only cities in the right `DataFrame` appear in the result. For example:

  ```
    pd.merge(left=city_loc, right=city_pop, on="city", how="right")
  ```

  + which outputs:

  ```
      state_x           city        lat         lng  population     state_y
    0      CA  San Francisco  37.781334 -122.416728      808976  California
    1      NY       New York  40.705649  -74.008344     8363710    New-York
    2      FL          Miami  25.791100  -80.320733      413201     Florida
    3     NaN        Houston        NaN         NaN     2242193       Texas
  ```
* If the key to join on is actually in one (or both) `DataFrame`’s index, you must use `left_index=True` and/or `right_index=True`. If the key column names differ, you must use `left_on` and `right_on`. For example:

  ```
    city_pop2 = city_pop.copy()
    city_pop2.columns = ["population", "name", "state"]
    pd.merge(left=city_loc, right=city_pop2, left_on="city", right_on="name")
  ```

  + which outputs:

  ```
      state_x           city        lat  ...  population           name     state_y
    0      CA  San Francisco  37.781334  ...      808976  San Francisco  California
    1      NY       New York  40.705649  ...     8363710       New York    New-York
    2      FL          Miami  25.791100  ...      413201          Miami     Florida

    [3 rows x 7 columns]
  ```

#### Concatenation

* Rather than joining `DataFrame`s, we may just want to concatenate them. That’s what `concat()` is for:

  ```
    result_concat = pd.concat([city_loc, city_pop])
    result_concat
  ```

  + which outputs:

  ```
                 city        lat         lng  population       state
    0   San Francisco  37.781334 -122.416728         NaN          CA
    1        New York  40.705649  -74.008344         NaN          NY
    2           Miami  25.791100  -80.320733         NaN          FL
    3       Cleveland  41.473508  -81.739791         NaN          OH
    4  Salt Lake City  40.755851 -111.896657         NaN          UT
    3   San Francisco        NaN         NaN    808976.0  California
    4        New York        NaN         NaN   8363710.0    New-York
    5           Miami        NaN         NaN    413201.0     Florida
    6         Houston        NaN         NaN   2242193.0       Texas
  ```
* Note that this operation aligned the data horizontally (by columns) but not vertically (by rows). In this example, we end up with multiple rows having the same index (eg. 3). Pandas handles this rather gracefully:

  ```
    result_concat.loc[3]
  ```

  + which outputs:

  ```
                city        lat        lng  population       state
    3      Cleveland  41.473508 -81.739791         NaN          OH
    3  San Francisco        NaN        NaN    808976.0  California
  ```
* Or you can tell pandas to just ignore the index:

  ```
    pd.concat([city_loc, city_pop], ignore_index=True)
  ```

  + which outputs:

  ```
                 city        lat         lng  population       state
    0   San Francisco  37.781334 -122.416728         NaN          CA
    1        New York  40.705649  -74.008344         NaN          NY
    2           Miami  25.791100  -80.320733         NaN          FL
    3       Cleveland  41.473508  -81.739791         NaN          OH
    4  Salt Lake City  40.755851 -111.896657         NaN          UT
    5   San Francisco        NaN         NaN    808976.0  California
    6        New York        NaN         NaN   8363710.0    New-York
    7           Miami        NaN         NaN    413201.0     Florida
    8         Houston        NaN         NaN   2242193.0       Texas
  ```
* Notice that when a column does not exist in a `DataFrame`, it acts as if it was filled with `NaN` values. If we set `join="inner"`, then only columns that exist in **both** `DataFrame`s are returned:

  ```
    pd.concat([city_loc, city_pop], join="inner")
  ```

  + which outputs:

  ```
            state            city
    0          CA   San Francisco
    1          NY        New York
    2          FL           Miami
    3          OH       Cleveland
    4          UT  Salt Lake City
    3  California   San Francisco
    4    New-York        New York
    5     Florida           Miami
    6       Texas         Houston
  ```
* You can concatenate `DataFrame`s horizontally instead of vertically by setting `axis=1`:

  ```
    pd.concat([city_loc, city_pop], axis=1)
  ```

  + which outputs:

  ```
      state            city        lat  ...  population           city       state
    0    CA   San Francisco  37.781334  ...         NaN            NaN         NaN
    1    NY        New York  40.705649  ...         NaN            NaN         NaN
    2    FL           Miami  25.791100  ...         NaN            NaN         NaN
    3    OH       Cleveland  41.473508  ...    808976.0  San Francisco  California
    4    UT  Salt Lake City  40.755851  ...   8363710.0       New York    New-York
    5   NaN             NaN        NaN  ...    413201.0          Miami     Florida
    6   NaN             NaN        NaN  ...   2242193.0        Houston       Texas

    [7 rows x 7 columns]
  ```
* In this case it really does not make much sense because the indices do not align well (eg. Cleveland and San Francisco end up on the same row, because they shared the index label `3`). So let’s reindex the `DataFrame`s by city name before concatenating:

  ```
    pd.concat([city_loc.set_index("city"), city_pop.set_index("city")], axis=1)
  ```

  + which outputs:

  ```
                   state        lat         lng  population       state
    Cleveland         OH  41.473508  -81.739791         NaN         NaN
    Houston          NaN        NaN         NaN   2242193.0       Texas
    Miami             FL  25.791100  -80.320733    413201.0     Florida
    New York          NY  40.705649  -74.008344   8363710.0    New-York
    Salt Lake City    UT  40.755851 -111.896657         NaN         NaN
    San Francisco     CA  37.781334 -122.416728    808976.0  California
  ```
* This looks a lot like a `FULL OUTER JOIN`, except that the `state` columns were not renamed to `state_x` and `state_y`, and the `city` column is now the index.
* The `append()` method is a useful shorthand for concatenating `DataFrame`s vertically:

  ```
    city_loc.append(city_pop)
  ```

  + which outputs:

  ```
                 city        lat         lng  population       state
    0   San Francisco  37.781334 -122.416728         NaN          CA
    1        New York  40.705649  -74.008344         NaN          NY
    2           Miami  25.791100  -80.320733         NaN          FL
    3       Cleveland  41.473508  -81.739791         NaN          OH
    4  Salt Lake City  40.755851 -111.896657         NaN          UT
    3   San Francisco        NaN         NaN    808976.0  California
    4        New York        NaN         NaN   8363710.0    New-York
    5           Miami        NaN         NaN    413201.0     Florida
    6         Houston        NaN         NaN   2242193.0       Texas
  ```
* As always in pandas, the `append()` method does **not** actually modify `city_loc`: it works on a copy and returns the modified copy.

## Categories

* It is quite frequent to have values that represent categories, for example `1` for female and `2` for male, or `"A"` for Good, `"B"` for Average, `"C"` for Bad. These categorical values can be hard to read and cumbersome to handle, but fortunately pandas makes it easy. To illustrate this, let’s take the `city_pop` `DataFrame` we created earlier, and add a column that represents a category:

  ```
    city_eco = city_pop.copy()
    city_eco["eco_code"] = [17, 17, 34, 20]
    city_eco
  ```

  + which outputs:

  ```
       population           city       state  eco_code
    3      808976  San Francisco  California        17
    4     8363710       New York    New-York        17
    5      413201          Miami     Florida        34
    6     2242193        Houston       Texas        20
  ```
* Right now the `eco_code` column is full of apparently meaningless codes. Let’s fix that. First, we will create a new categorical column based on the `eco_code`s:

  ```
    city_eco["economy"] = city_eco["eco_code"].astype('category')
    city_eco["economy"].cat.categories
  ```

  + which outputs:

  ```
    Int64Index([17, 20, 34], dtype='int64')
  ```
* Now we can give each category a meaningful name:

  ```
    city_eco["economy"].cat.categories = ["Finance", "Energy", "Tourism"]
    city_eco
  ```

  + which outputs:

  ```
       population           city       state  eco_code  economy
    3      808976  San Francisco  California        17  Finance
    4     8363710       New York    New-York        17  Finance
    5      413201          Miami     Florida        34  Tourism
    6     2242193        Houston       Texas        20   Energy
  ```
* Note that categorical values are sorted according to their categorical order, \*not\*\* their alphabetical order:

  ```
    city_eco.sort_values(by="economy", ascending=False)
  ```

  + which outputs:

  ```
       population           city       state  eco_code  economy
    5      413201          Miami     Florida        34  Tourism
    6     2242193        Houston       Texas        20   Energy
    3      808976  San Francisco  California        17  Finance
    4     8363710       New York    New-York        17  Finance
  ```

## Practical example using a sample dataset

* To demonstrate the use of pandas, we’ll be using the interview reviews scraped from Glassdoor in 2019. The data is available [here](../assets/pandas/interviews.csv).

### Dataset at a glance

* Let’s check out the dataset :

  ```
    import pandas as pd
    df = pd.read_csv("../assets/pandas/interviews.csv")

    print(df.shape)
    df.head()
  ```

  + which outputs:

  ```
      Company              Title                Job     Level          Date  Upvotes           Offer  Experience Difficulty                                             Review
    0   Apple  Software Engineer  Software Engineer  Engineer   Aug 7, 2019        0        No offer         0.0     Medium  Application  I applied through a staffing agen...
    1   Apple  Software Engineer  Software Engineer  Engineer   Aug 8, 2019        0  Accepted offer         1.0       Hard  Application  I applied online. The process too...
    2   Apple  Software Engineer  Software Engineer  Engineer           NaN        0  Declined offer         0.0     Medium  Application  The process took 4 weeks. I inter...
    3   Apple  Software Engineer  Software Engineer  Engineer           NaN        9  Declined offer        -1.0     Medium  Application  The process took a week. I interv...
    4   Apple  Software Engineer  Software Engineer  Engineer  May 29, 2009        2        No offer         0.0     Medium  Application  I applied through an employee ref...
  ```

### Iterating over rows

#### `.apply()`

* pandas documentation has [a warning box](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#iteration) that basically tells you not to iterate over rows because it’s slow.
* Before iterating over rows, think about what you want to do with each row, pack that into a function and use methods like `.apply()` to apply the function to all rows.
* For example, to scale the “Experience” column by the number of “Upvotes” each review has, one way is to iterate over rows and multiple the “Upvotes” value by the “Experience” value of that row. But you can also use `.apply()` with a `lambda` function.
* Run the following code snippet in a Colab/Jupyter notebook:

  ```
    %timeit -n1 df.apply(lambda x: x["Experience"] * x["Upvotes"], axis=1)
  ```

  + which outputs:

  ```
    180 ms ± 16.5 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
  ```

#### `.iterrows()` and `.itertuples()`

* If you really want to iterate over rows, one naive way is to use `.iterrows()`. It returns a generator that generates row by row and it’s very slow. Run the following code snippet in a Colab/Jupyter notebook:

  ```
    %timeit -n1 [row for index, row in df.iterrows()]
  ```

  + which outputs:

  ```
    1.42 s ± 107 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
  ```
* Using `.iterrows()`:

  ```
    # This is what a row looks like as a pandas object
    for index, row in df.iterrows():
        print(row)
        break
  ```

  + which outputs:

  ```
    Company                                                   Apple
    Title                                         Software Engineer
    Job                                           Software Engineer
    Level                                                  Engineer
    Date                                                Aug 7, 2019
    Upvotes                                                       0
    Offer                                                  No offer
    Experience                                                    0
    Difficulty                                               Medium
    Review        Application  I applied through a staffing agen...
    Name: 0, dtype: object
  ```
* `.itertuples()` returns rows in the `namedtuple` format. It still lets you access each row and it’s about 40x faster than `.iterrows()`. Run the following code snippet in a Colab/Jupyter notebook:

  ```
    %timeit -n1 [row for row in df.itertuples()]
  ```

  + which outputs:

  ```
    24.2 ms ± 709 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)
  ```
* Using `.iterrows()`:

  ```
    # This is what a row looks like as a namedtuple.
    for row in df.itertuples():
        print(row)
        break
  ```

  + which outputs:

  ```
    Pandas(Index=0, Company='Apple', Title='Software Engineer', Job='Software Engineer', Level='Engineer', Date='Aug 7, 2019', Upvotes=0, Offer='No offer', Experience=0.0, Difficulty='Medium', Review='Application  I applied through a staffing agency. I interviewed at Apple (Sunnyvale, CA) in March 2019.  Interview  The interviewer asked me about my background. Asked few questions from the resume. Asked about my proficiency on data structures. Asked me how do you sort hashmap keys based on values.  Interview Questions Write a program that uses two threads to print the numbers from 1 to n.')
  ```

#### Ordering slicing operations

* Because pandas is column-major, if you want to do multiple slicing operations, always do the column-based slicing operations first.
* For example, if you want to get the review from the first row of the data, there are two slicing operations:
  + get row (row-based operation)
  + get review (column-based operation)
* Get row -> get review is 25x slower than get review -> get row.
* **Note**: You can also just use `df.loc[0, "Review"]` to calculate the memory address to retrieve the item. Its performance is comparable to get review then get row.

  ```
    %timeit -n1000 df["Review"][0]
    %timeit -n1000 df.iloc[0]["Review"]
    %timeit -n1000 df.loc[0, "Review"]
  ```

  + which outputs:

  ```
    5.55 µs ± 1.05 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    136 µs ± 2.57 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    6.23 µs ± 264 ns per loop (mean ± std. dev. of 7 runs, 1000 loops each)
  ```

### SettingWithCopyWarning

* Sometimes, when you try to assign values to a subset of data in a DataFrame, you get `SettingWithCopyWarning`. Don’t ignore the warning because it means sometimes, the assignment works (example 1), but sometimes, it doesn’t (example 2).
* Example 1: Changing the review of the first row:

  ```
    df["Review"][0] = "I like Orange better."
    # Even though with the warning, the assignment works. The review is updated.
    df.head(1)
  ```

  + which outputs:

  ```
    /Users/chip/miniconda3/envs/py3/lib/python3.6/site-packages/ipykernel_launcher.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame

    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

      Company              Title                Job     Level         Date  Upvotes     Offer  Experience Difficulty                 Review
    0   Apple  Software Engineer  Software Engineer  Engineer  Aug 7, 2019        0  No offer         0.0     Medium  I like Orange better.
  ```
* Example 2: Changing the company name Apple to Orange:

  ```
    df[df["Company"] == "Apple"]["Company"] = "Orange"
    # With the warning, the assignment doesn't work. The company name is still Apple.
    df.head(1)
  ```

  + which outputs:

  ```
    /Users/chip/miniconda3/envs/py3/lib/python3.6/site-packages/ipykernel_launcher.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead

    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

      Company              Title                Job     Level         Date  Upvotes     Offer  Experience Difficulty                 Review
    0   Apple  Software Engineer  Software Engineer  Engineer  Aug 7, 2019        0  No offer         0.0     Medium  I like Orange better.
  ```

#### `View` vs. `Copy`

* To understand this weird behavior, we need to understand two concepts in pandas: `View` vs. `Copy`.
  + `View` is the actual `DataFrame` you want to work with.
  + `Copy` is a copy of that actual `DataFrame`, which will be thrown away as soon as the operation is done.
* So if you try to do an assignment on a `Copy`, the assignment won’t work.
* `SettingWithCopyWarning` doesn’t mean you’re making changes to a `Copy`. It means that the thing you’re making changes to might be a `Copy` or a `View`, and pandas can’t tell you.
* The ambiguity happens because of `__getitem__` operation. `__getitem__` sometimes returns a `Copy`, sometimes a `View`, and pandas makes no guarantee.

  ```
    # df["Review"][0] = "I like Orange better."
    # can be understood as
    # `df.__getitem__("Review").__setitem__(0, "I like Orange better.")`
  ```

  ```
    # df[df["Company"] == "Apple"]["Company"] = "Orange"
    # can be understood as
    # df.__getitem__(where df["Company"] == "Apple").__setitem__("Company", "Orange")
  ```

#### Solutions

##### Combine all chained operations into one single operation

* To avoid `__getitem__` ambiguity, you can combine all your operations into one single operation. `.loc[]` is usually great for that.
* Changing the review of the first row:

  ```
    df.loc[0, "Review"] = "Orange is love. Orange is life."
    df.head()
  ```

  + which outputs:

  ```
      Company              Title                Job     Level          Date  Upvotes           Offer  Experience Difficulty                                             Review
    0   Apple  Software Engineer  Software Engineer  Engineer   Aug 7, 2019        0        No offer         0.0     Medium                    Orange is love. Orange is life.
    1   Apple  Software Engineer  Software Engineer  Engineer   Aug 8, 2019        0  Accepted offer         1.0       Hard  Application  I applied online. The process too...
    2   Apple  Software Engineer  Software Engineer  Engineer           NaN        0  Declined offer         0.0     Medium  Application  The process took 4 weeks. I inter...
    3   Apple  Software Engineer  Software Engineer  Engineer           NaN        9  Declined offer        -1.0     Medium  Application  The process took a week. I interv...
    4   Apple  Software Engineer  Software Engineer  Engineer  May 29, 2009        2        No offer         0.0     Medium  Application  I applied through an employee ref...
  ```
* Changing the company name `Apple` to `Orange`:

  ```
    df.loc[df["Company"] == "Apple", "Company"] = "Orange"
    df.head()
  ```

  + which outputs:

  ```
    Company              Title                Job     Level          Date  Upvotes           Offer  Experience Difficulty                                             Review
    0  Orange  Software Engineer  Software Engineer  Engineer   Aug 7, 2019        0        No offer         0.0     Medium                    Orange is love. Orange is life.
    1  Orange  Software Engineer  Software Engineer  Engineer   Aug 8, 2019        0  Accepted offer         1.0       Hard  Application  I applied online. The process too...
    2  Orange  Software Engineer  Software Engineer  Engineer           NaN        0  Declined offer         0.0     Medium  Application  The process took 4 weeks. I inter...
    3  Orange  Software Engineer  Software Engineer  Engineer           NaN        9  Declined offer        -1.0     Medium  Application  The process took a week. I interv...
    4  Orange  Software Engineer  Software Engineer  Engineer  May 29, 2009        2        No offer         0.0     Medium  Application  I applied through an employee ref...
  ```

##### Raise an error

* `SettingWithCopyWarning` should ideally be an Exception instead of a warning. You can change this warning into an exception with pandas’ magic `set_option()`.

  ```
    pd.set_option("mode.chained_assignment", "raise")
    # Running this will show you an Exception
    # df["Review"][0] = "I like Orange better."
  ```

### Indexing and slicing

#### `.iloc[]`: selecting rows based on integer indices

* `.iloc[]` lets you select rows by integer indices.
* Accessing the third row of a `DataFrame`:

  ```
    df.iloc[3]
  ```

  + which outputs:

  ```
    Company                                                  Orange
    Title                                         Software Engineer
    Job                                           Software Engineer
    Level                                                  Engineer
    Date                                                        NaN
    Upvotes                                                       9
    Offer                                            Declined offer
    Experience                                                   -1
    Difficulty                                               Medium
    Review        Application  The process took a week. I interv...
    Name: 3, dtype: object
  ```
* Slicing with `.iloc[]` is similar to slicing in Python. If you want a refresh on how slicing in Python works, see our [Python Tutorial](../python3).
* Selecting the last 6 rows:

  ```
    df.iloc[-6:]
  ```

  + which outputs:

  ```
           Company              Title                Job     Level          Date  Upvotes           Offer  Experience Difficulty                                             Review
    17648  Tencent  Software Engineer  Software Engineer  Engineer   Nov 4, 2012        0        No offer         NaN        NaN  Application  I applied online. The process too...
    17649  Tencent  Software Engineer  Software Engineer  Engineer  May 25, 2012        0  Declined offer         0.0     Medium  Application  I applied online. The process too...
    17650  Tencent  Software Engineer  Software Engineer  Engineer  Mar 15, 2014        0        No offer         NaN        NaN  Application  I applied through college or univ...
    17651  Tencent  Software Engineer  Software Engineer  Engineer  Sep 22, 2015        0  Accepted offer         1.0     Medium  Application  I applied through college or univ...
    17652  Tencent  Software Engineer  Software Engineer  Engineer   Jul 4, 2017        0  Declined offer         1.0     Medium  Application  I applied through college or univ...
    17653  Tencent  Software Engineer  Software Engineer  Engineer  Sep 30, 2016        0  Declined offer         0.0       Easy  Application  I applied online. The process too...
  ```
* Selecting 1 from every 2 rows in the last 6 rows:

  ```
    df.iloc[-6::2]
  ```

  + which outputs:

  ```
        Company Title   Job Level   Date    Upvotes Offer   Experience  Difficulty  Review
    17648   Tencent Software Engineer   Software Engineer   Engineer    Nov 4, 2012 0   No offer    NaN NaN Application I applied online. The process too...
    17650   Tencent Software Engineer   Software Engineer   Engineer    Mar 15, 2014    0   No offer    NaN NaN Application I applied through college or univ...
    17652   Tencent Software Engineer   Software Engineer   Engineer    Jul 4, 2017 0   Declined offer  1.0 Medium  Application I applied through college or univ...
  ```

#### `.loc[]`: selecting rows by labels or boolean masks

* `.loc[]` lets you select rows based on one of the two things:
  + boolean masks
  + labels

##### Selecting rows by boolean masks

* If you want to select all the rows where candidates declined offer, you can do it with two steps:
  1. Create a boolean mask on whether the “Offer” column equals to “Declined offer”
  2. Use that mask to select rows

  ```
    df.loc[df["Offer"] == "Declined offer"]
    # This is equivalent to:
    # mask = df["Offer"] == "Declined offer"
    # df.loc[mask]
  ```

  + which outputs:

  ```
           Company              Title                Job     Level          Date  Upvotes           Offer  Experience Difficulty                                             Review
    2       Orange  Software Engineer  Software Engineer  Engineer           NaN        0  Declined offer         0.0     Medium  Application  The process took 4 weeks. I inter...
    3       Orange  Software Engineer  Software Engineer  Engineer           NaN        9  Declined offer        -1.0     Medium  Application  The process took a week. I interv...
    7       Orange  Software Engineer  Software Engineer  Engineer  Jul 26, 2019        1  Declined offer        -1.0     Medium  Application  The process took 4+ weeks. I inte...
    17      Orange  Software Engineer  Software Engineer  Engineer  Feb 27, 2010        7  Declined offer        -1.0     Medium  Application  The process took 1 day. I intervi...
    65      Orange  Software Engineer  Software Engineer  Engineer   May 6, 2012        1  Declined offer         1.0       Easy  Application  The process took 2 days. I interv...
    ...        ...                ...                ...       ...           ...      ...             ...         ...        ...                                                ...
    17643  Tencent  Software Engineer  Software Engineer  Engineer   Apr 9, 2016        0  Declined offer         1.0     Medium  Application  I applied online. I interviewed a...
    17646  Tencent  Software Engineer  Software Engineer  Engineer  May 28, 2010        0  Declined offer         0.0       Easy  Application  I applied through an employee ref...
    17649  Tencent  Software Engineer  Software Engineer  Engineer  May 25, 2012        0  Declined offer         0.0     Medium  Application  I applied online. The process too...
    17652  Tencent  Software Engineer  Software Engineer  Engineer   Jul 4, 2017        0  Declined offer         1.0     Medium  Application  I applied through college or univ...
    17653  Tencent  Software Engineer  Software Engineer  Engineer  Sep 30, 2016        0  Declined offer         0.0       Easy  Application  I applied online. The process too...

    [1135 rows × 10 columns]
  ```

##### Selecting rows by labels

###### Creating labels

* Currently, our `DataFrame` has no labels yet. To create labels, use `.set_index()`.

  1. Labels can be integers or strings
  2. A `DataFrame` can have multiple labels

  ```
    # Adding label "Hardware" if the company name is "Orange", "Dell", "IDM", or "Siemens".
    # "Orange" because we changed "Apple" to "Orange" above.
    # Adding label "Software" otherwise.

    def company_type(x):
        hardware_companies = set(["Orange", "Dell", "IBM", "Siemens"])
        return "Hardware" if x["Company"] in hardware_companies else "Software"
    df["Type"] = df.apply(lambda x: company_type(x), axis=1)

    # Setting "Type" to be labels. We call ""
    df = df.set_index("Type")
    df
    # Label columns aren't considered part of the DataFrame's content.
    # After adding labels to your DataFrame, it still has 10 columns, same as before.
  ```

  + which outputs:

  ```
           Company              Title                Job     Level          Date  Upvotes           Offer  Experience Difficulty                                             Review
    0       Orange  Software Engineer  Software Engineer  Engineer   Aug 7, 2019        0        No offer         0.0     Medium                    Orange is love. Orange is life.
    1       Orange  Software Engineer  Software Engineer  Engineer   Aug 8, 2019        0  Accepted offer         1.0       Hard  Application  I applied online. The process too...
    2       Orange  Software Engineer  Software Engineer  Engineer           NaN        0  Declined offer         0.0     Medium  Application  The process took 4 weeks. I inter...
    3       Orange  Software Engineer  Software Engineer  Engineer           NaN        9  Declined offer        -1.0     Medium  Application  The process took a week. I interv...
    4       Orange  Software Engineer  Software Engineer  Engineer  May 29, 2009        2        No offer         0.0     Medium  Application  I applied through an employee ref...
    ...        ...                ...                ...       ...           ...      ...             ...         ...        ...                                                ...
    17649  Tencent  Software Engineer  Software Engineer  Engineer  May 25, 2012        0  Declined offer         0.0     Medium  Application  I applied online. The process too...
    17650  Tencent  Software Engineer  Software Engineer  Engineer  Mar 15, 2014        0        No offer         NaN        NaN  Application  I applied through college or univ...
    17651  Tencent  Software Engineer  Software Engineer  Engineer  Sep 22, 2015        0  Accepted offer         1.0     Medium  Application  I applied through college or univ...
    17652  Tencent  Software Engineer  Software Engineer  Engineer   Jul 4, 2017        0  Declined offer         1.0     Medium  Application  I applied through college or univ...
    17653  Tencent  Software Engineer  Software Engineer  Engineer  Sep 30, 2016        0  Declined offer         0.0       Easy  Application  I applied online. The process too...

    [17654 rows x 10 columns]
  ```
* **Warning**: labels in `DataFrame` are stored as normal columns when you write the `DataFrame` to file using `.to_csv()`, and will need to be explicitly set after loading files, so if you send your CSV file to other people without explaining, they’ll have no way of knowing which columns are labels. This might cause reproducibility issues. See [Stack Overflow answer](https://stackoverflow.com/questions/20109391/how-to-make-good-reproducible-pandas-examples).

###### Selecting rows by labels

* Selecting rows with label “Hardware”:

  ```
    df.loc["Hardware"]
  ```

  + which outputs:

  ```
        Company Title   Job Level   Date    Upvotes Offer   Experience  Difficulty  Review
    Type                                        
    Hardware    Orange  Software Engineer   Software Engineer   Engineer    Aug 7, 2019 0   No offer    0.0 Medium  Orange is love. Orange is life.
    Hardware    Orange  Software Engineer   Software Engineer   Engineer    Aug 8, 2019 0   Accepted offer  1.0 Hard    Application I applied online. The process too...
    Hardware    Orange  Software Engineer   Software Engineer   Engineer    NaN 0   Declined offer  0.0 Medium  Application The process took 4 weeks. I inter...
    Hardware    Orange  Software Engineer   Software Engineer   Engineer    NaN 9   Declined offer  -1.0    Medium  Application The process took a week. I interv...
    Hardware    Orange  Software Engineer   Software Engineer   Engineer    May 29, 2009    2   No offer    0.0 Medium  Application I applied through an employee ref...
    ... ... ... ... ... ... ... ... ... ... ...
    Hardware    IBM Senior Software Engineer    Software Engineer   Senior  Sep 20, 2015    0   No offer    -1.0    Easy    Application I applied through a recruiter. Th...
    Hardware    IBM Senior Software Engineer    Software Engineer   Senior  Sep 14, 2015    0   Accepted offer  -1.0    Medium  Application I applied in-person. The process ...
    Hardware    IBM Senior Software Engineer    Software Engineer   Senior  Aug 6, 2015 0   Accepted offer  1.0 Hard    Application I applied through a recruiter. Th...
    Hardware    IBM Senior Software Engineer    Software Engineer   Senior  Dec 13, 2015    0   Accepted offer  1.0 Medium  Application I applied online. The process too...
    Hardware    IBM Senior Software Engineer    Software Engineer   Senior  Feb 15, 2016    11  Accepted offer  1.0 Easy    Application I applied online. The process too...

    [1676 rows × 10 columns]
  ```
* To drop a label, you need to use `reset_index` with `drop=True`:

  ```
    df.reset_index(drop=True, inplace=True)
    df
  ```

  + which outputs:

  ```
        Company Title   Job Level   Date    Upvotes Offer   Experience  Difficulty  Review
    0   Orange  Software Engineer   Software Engineer   Engineer    Aug 7, 2019 0   No offer    0.0 Medium  Orange is love. Orange is life.
    1   Orange  Software Engineer   Software Engineer   Engineer    Aug 8, 2019 0   Accepted offer  1.0 Hard    Application I applied online. The process too...
    2   Orange  Software Engineer   Software Engineer   Engineer    NaN 0   Declined offer  0.0 Medium  Application The process took 4 weeks. I inter...
    3   Orange  Software Engineer   Software Engineer   Engineer    NaN 9   Declined offer  -1.0    Medium  Application The process took a week. I interv...
    4   Orange  Software Engineer   Software Engineer   Engineer    May 29, 2009    2   No offer    0.0 Medium  Application I applied through an employee ref...
    ... ... ... ... ... ... ... ... ... ... ...
    17649   Tencent Software Engineer   Software Engineer   Engineer    May 25, 2012    0   Declined offer  0.0 Medium  Application I applied online. The process too...
    17650   Tencent Software Engineer   Software Engineer   Engineer    Mar 15, 2014    0   No offer    NaN NaN Application I applied through college or univ...
    17651   Tencent Software Engineer   Software Engineer   Engineer    Sep 22, 2015    0   Accepted offer  1.0 Medium  Application I applied through college or univ...
    17652   Tencent Software Engineer   Software Engineer   Engineer    Jul 4, 2017 0   Declined offer  1.0 Medium  Application I applied through college or univ...
    17653   Tencent Software Engineer   Software Engineer   Engineer    Sep 30, 2016    0   Declined offer  0.0 Easy    Application I applied online. The process too...

    [17654 rows × 10 columns]
  ```

#### Slicing Series

* Slicing pandas `Series` is similar to slicing in Python.

  ```
    series = df.Company
    # The first 1000 companies, picking every 100th companies
    series[:1000:100]
  ```

  + which outputs:

  ```
    0      Orange
    100    Orange
    200    Orange
    300    Orange
    400     Intel
    500     Intel
    600     Intel
    700     Intel
    800      Uber
    900      Uber
    Name: Company, dtype: object
  ```

### Accessors

#### string accessor

* `.str` allows you to apply built-in string functions to all strings in a column (aka a pandas Series). These built-in functions come in handy when you want to do some basic string processing. For instance, if you want to lowercase all the reviews in the `Reviews` column:

  ```
    df["Review"].str.lower()
  ```

  + which outputs:

  ```
    0                          orange is love. orange is life.
    1        application  i applied online. the process too...
    2        application  the process took 4 weeks. i inter...
    3        application  the process took a week. i interv...
    4        application  i applied through an employee ref...
                                   ...                        
    17649    application  i applied online. the process too...
    17650    application  i applied through college or univ...
    17651    application  i applied through college or univ...
    17652    application  i applied through college or univ...
    17653    application  i applied online. the process too...
    Name: Review, Length: 17654, dtype: object
  ```
* Or if you want to get the length of all the reviews:

  ```
    df.Review.str.len()
  ```

  + which outputs:

  ```
    0         31
    1        670
    2        350
    3        807
    4        663
            ... 
    17649    470
    17650    394
    17651    524
    17652    391
    17653    784
    Name: Review, Length: 17654, dtype: int64
  ```
* `.str` can be very powerful if you use it with Regex. Imagine you want to get a sense of how long the interview process takes for each review. You notice that each review mentions how long it takes such as “the process took 4 weeks”. So you use these heuristics:
  + A process is short if it takes days.
  + A process is average is if it takes weeks.
  + A process is long if it takes at least 4 weeks.

  ```
    df.loc[df["Review"].str.contains("days"), "Process"] = "Short"
    df.loc[df["Review"].str.contains("week"), "Process"] = "Average"
    df.loc[df["Review"].str.contains("month|[4-9]+[^ ]* weeks|[1-9]\d{1,}[^ ]* weeks"), "Process"] = "Long"
    df[~df.Process.isna()][["Review", "Process"]]
  ```

  + which outputs:

  ```
        Review  Process
    1   Application I applied online. The process too...    Long
    2   Application The process took 4 weeks. I inter...    Long
    3   Application The process took a week. I interv...    Average
    5   Application I applied through college or univ...    Long
    6   Application The process took 2 days. I interv...    Short
    ... ... ...
    17645   Application I applied online. The process too...    Average
    17647   Application I applied through college or univ...    Average
    17648   Application I applied online. The process too...    Short
    17649   Application I applied online. The process too...    Average
    17653   Application I applied online. The process too...    Average

    [12045 rows × 2 columns]
  ```
* We want to sanity check if `Process` corresponds to `Review`, but `Review` is cut off in the display above. To show longer columns, you can set `display.max_colwidth` to `100`. **Note**: set\_option has several great options you should check out.

  ```
    pd.set_option('display.max_colwidth', 100)
    df[~df.Process.isna()][["Review", "Process"]]
  ```

  + which outputs:

  ```
    Review  Process
    1   Application I applied online. The process took 2+ months. I interviewed at Apple (San Jose, CA)...  Long
    2   Application The process took 4 weeks. I interviewed at Apple (San Antonio, TX) in February 2016...  Long
    3   Application The process took a week. I interviewed at Apple (Cupertino, CA) in December 2008. ...   Average
    5   Application I applied through college or university. The process took 6 weeks. I interviewed at...  Long
    6   Application The process took 2 days. I interviewed at Apple (Cupertino, CA) in March 2009. Int...   Short
    ... ... ...
    17645   Application I applied online. The process took a week. I interviewed at Tencent (Palo Alto, CA)...  Average
    17647   Application I applied through college or university. The process took 4+ weeks. I interviewed a...  Average
    17648   Application I applied online. The process took 2 days. I interviewed at Tencent. Interview I ...    Short
    17649   Application I applied online. The process took a week. I interviewed at Tencent (Beijing, Beiji...  Average
    17653   Application I applied online. The process took 3+ weeks. I interviewed at Tencent (Beijing, Bei...  Average

    [12045 rows × 2 columns]
  ```
* To see the built-in functions available for `.str`, use this:

  ```
    pd.Series.str.__dict__.keys()
  ```

  + which outputs:

  ```
    dict_keys(['__module__', '__annotations__', '__doc__', '__init__', '_validate', '__getitem__', '__iter__', '_wrap_result', '_get_series_list', 'cat', 'split', 'rsplit', 'partition', 'rpartition', 'get', 'join', 'contains', 'match', 'fullmatch', 'replace', 'repeat', 'pad', 'center', 'ljust', 'rjust', 'zfill', 'slice', 'slice_replace', 'decode', 'encode', 'strip', 'lstrip', 'rstrip', 'wrap', 'get_dummies', 'translate', 'count', 'startswith', 'endswith', 'findall', 'extract', 'extractall', 'find', 'rfind', 'normalize', 'index', 'rindex', 'len', '_doc_args', 'lower', 'upper', 'title', 'capitalize', 'swapcase', 'casefold', 'isalnum', 'isalpha', 'isdigit', 'isspace', 'islower', 'isupper', 'istitle', 'isnumeric', 'isdecimal', '_make_accessor'])
  ```

#### Other accessors

* pandas `Series` has three other accessors:
  + `.dt`: handles date formats.
  + `.cat`: handles categorical data.
  + `.sparse`: handles sparse matrices.

  ```
    pd.Series._accessors
  ```

  + which outputs:

  ```
    {'cat', 'dt', 'sparse', 'str'}
  ```

### Data exploration

* When analyzing data, you might want to take a look at the data. pandas has some great built-in functions for that.

#### `.head()`, `.tail()`, `.describe()`, `.info()`

* You’re probably familiar with `.head()` and `.tail()` methods for showing the first/last rows of `DataFrame`. By default, five rows are shown, but you can specify the exact number.

  ```
    df.tail(8)
  ```

  + which outputs:

  ```
    Company Title   Job Level   Date    Upvotes Offer   Experience  Difficulty  Review  Process
    17646   Tencent Software Engineer   Software Engineer   Engineer    May 28, 2010    0   Declined offer  0.0 Easy    Application I applied through an employee referral. The process took 1 day. I interviewed at Te...  NaN
    17647   Tencent Software Engineer   Software Engineer   Engineer    Apr 11, 2019    0   Accepted offer  1.0 Medium  Application I applied through college or university. The process took 4+ weeks. I interviewed a...  Average
    17648   Tencent Software Engineer   Software Engineer   Engineer    Nov 4, 2012 0   No offer    NaN NaN Application I applied online. The process took 2 days. I interviewed at Tencent. Interview I ...    Short
    17649   Tencent Software Engineer   Software Engineer   Engineer    May 25, 2012    0   Declined offer  0.0 Medium  Application I applied online. The process took a week. I interviewed at Tencent (Beijing, Beiji...  Average
    17650   Tencent Software Engineer   Software Engineer   Engineer    Mar 15, 2014    0   No offer    NaN NaN Application I applied through college or university. I interviewed at Tencent. Interview Prof...    NaN
    17651   Tencent Software Engineer   Software Engineer   Engineer    Sep 22, 2015    0   Accepted offer  1.0 Medium  Application I applied through college or university. The process took 1 day. I interviewed at T...  NaN
    17652   Tencent Software Engineer   Software Engineer   Engineer    Jul 4, 2017 0   Declined offer  1.0 Medium  Application I applied through college or university. I interviewed at Tencent (London, England ...  NaN
    17653   Tencent Software Engineer   Software Engineer   Engineer    Sep 30, 2016    0   Declined offer  0.0 Easy    Application I applied online. The process took 3+ weeks. I interviewed at Tencent (Beijing, Bei...  Average
  ```
* You can generate statistics about numeric columns using `.describe()`.

  ```
    df.describe()
  ```

  + which outputs:

  ```
    Upvotes Experience
    count   17654.000000    16365.000000
    mean    2.298459    0.431714
    std 28.252562   0.759964
    min 0.000000    -1.000000
    25% 0.000000    0.000000
    50% 0.000000    1.000000
    75% 1.000000    1.000000
    max 1916.000000 1.000000
  ```
* However, note that `.describe()` ignores all non-numeric columns. It doesn’t take into account NaN values. So, the number shown in `count` above is the number of non-NaN entries.
* To show non-null count and types of all columns, use `.info()`. Note that pandas treats the `String` type as an object.

  ```
    df.info()
  ```

  + which outputs:

  ```
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 17654 entries, 0 to 17653
    Data columns (total 11 columns):
     #   Column      Non-Null Count  Dtype  
    ---  ------      --------------  -----  
     0   Company     17654 non-null  object 
     1   Title       17654 non-null  object 
     2   Job         17654 non-null  object 
     3   Level       17654 non-null  object 
     4   Date        17652 non-null  object 
     5   Upvotes     17654 non-null  int64  
     6   Offer       17654 non-null  object 
     7   Experience  16365 non-null  float64
     8   Difficulty  16376 non-null  object 
     9   Review      17654 non-null  object 
     10  Process     12045 non-null  object 
    dtypes: float64(1), int64(1), object(9)
    memory usage: 1.5+ MB
  ```
* You can also see how much space your DataFrame is taking up using :

  ```
    import sys
    df.apply(sys.getsizeof)
  ```

  + which outputs:

  ```
    Company        1126274
    Title          1358305
    Job            1345085
    Level          1144784
    Date           1212964
    Upvotes         141384
    Offer          1184190
    Experience      141384
    Difficulty     1058008
    Review        20503467
    Process        1274180
    dtype: int64
  ```

#### Count unique values

* You can get the number of unique values in a row (excluding NaN) with `nunique()`. For instance, to get the number of unique companies in our data:

  ```
    df.Company.nunique()
  ```

  + which outputs:

  ```
    28
  ```

  + You can also see how many reviews are for each company, sorted in descending order:

  ```
    df.Company.value_counts()
  ```

  + which outputs:

  ```
    Amazon        3469
    Google        3445
    Facebook      1817
    Microsoft     1790
    IBM            873
    Cisco          787
    Oracle         701
    Uber           445
    Yelp           404
    Orange         363
    Intel          338
    Salesforce     313
    SAP            275
    Twitter        258
    Dell           258
    Airbnb         233
    NVIDIA         229
    Adobe          211
    Intuit         203
    PayPal         193
    Siemens        182
    Square         177
    Samsung        159
    eBay           148
    Symantec       147
    Snap           113
    Netflix        109
    Tencent         14
    Name: Company, dtype: int64
  ```

#### Plotting

* If you want to see the break down of process lengths for different companies, you can use `.plot()` with `.groupby()`.
* **Note**: Plotting in pandas is both mind-boggling and mind-blowing. If you’re not familiar, you might want to check out some tutorials, e.g. [this simple tutorial](https://realpython.com/pandas-plot-python/) or [this saiyan-level pandas plotting with seaborn](https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html).

  ```
    # Group the DataFrame by "Company" and "Process", count the number of elements,
    # then unstack by "Process", then plot a bar chart
    df.groupby(["Company", "Process"]).size().unstack(level=1).plot(kind="bar", figsize=(15, 8))
  ```

  + which outputs:

### Common pitfalls

* pandas is great for most day-to-day data analysis. There is an active community that is working on regular updates to the library. However, some of the design decisions can seen a bit questionable.
* Some of the common pandas pitfalls:

#### NaNs as floats

* NaNs are stored as floats in pandas, so when an operation fails because of NaNs, it doesn’t say that there’s a NaN but because that operation isn’t defined for floats.

#### Changes aren’t in-place by default

* Most pandas operations aren’t in-place by default, so if you make changes to your `DataFrame`, you need to assign the changes back to your DataFrame. You can make changes in-place by setting argument `inplace=True`.

  ```
    # "Process" column is still in df
    df.drop(columns=["Process"])
    df.columns
  ```

  + which outputs:

  ```
    Index(['Company', 'Title', 'Job', 'Level', 'Date', 'Upvotes', 'Offer',
           'Experience', 'Difficulty', 'Review', 'Process'],
          dtype='object')
  ```

  + To make changes to df, set `inplace=True`:

  ```
    df.drop(columns=["Process"], inplace=True)
    df.columns
    # This is equivalent to
    # df = df.drop(columns=["Process"])
  ```

  + which outputs:

  ```
    Index(['Company', 'Title', 'Job', 'Level', 'Date', 'Upvotes', 'Offer',
           'Experience', 'Difficulty', 'Review'],
          dtype='object')
  ```

#### Reproducibility issues

* Especially with dumping and loading `DataFrame` to/from files. There are two main causes:

  + Problem with [labels](#creating-labels) (see the section about labels above).
  + [Weird rounding issues for floats](https://stackoverflow.com/questions/47368296/pandas-read-csv-file-with-float-values-results-in-weird-rounding-and-decimal-dig).

#### Not GPU compatible

* pandas can’t take advantage of GPUs, so if your computations are on on GPUs and your feature engineering is on CPUs, it can become a time bottleneck to move data from CPUs to GPUs. If you want something like pandas but works on GPUs, check out [dask](https://dask.org/) and [modin](https://github.com/modin-project/modin).

## What next?

* As you probably noticed by now, pandas is quite a large library with **many** features. Although we went through the most important features, there is still a lot to discover. Probably the best way to learn more is to get your hands dirty with some real-life data. It is also a good idea to go through pandas’ excellent [documentation](http://pandas.pydata.org/pandas-docs/stable/index.html), in particular the [Cookbook](http://pandas.pydata.org/pandas-docs/stable/cookbook.html).

## References and Credits

* Aurélien Geron’s [Notebook on Matplotlib](https://github.com/ageron/handson-ml2/blob/master/tools_matplotlib.ipynb) and [Hands-on Machine Learning with Scikit-Learn, Keras and TensorFlow](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/) served as a major inspiration for this tutorial.
* [pandas.DataFrame.to\_dict()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html)
* [Constructing pandas DataFrame from values in variables gives “ValueError: If using all scalar values, you must pass an index”](https://stackoverflow.com/questions/17839973/constructing-pandas-dataframe-from-values-in-variables-gives-valueerror-if-usi)

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledPandasTutorial,
  title   = {Pandas Tutorial},
  author  = {Chadha, Aman},
  journal = {Distilled AI},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
