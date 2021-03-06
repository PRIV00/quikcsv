# QuikCSV
Python package for quickly creating temporary csv files to help with testing. The CSV file exists in memory only so you can create files on the fly without needing to cleanup or delete files later. No need to use with statements or close resources, that is taken care of.

## Installation

```
pip install quikcsv
```

## Sample

Take a function that takes an open CSV file as its argument. Instead of creating and opening an actual CSV file on the disk, decorate the function.

```python
from quikcsv import QuikCSV


@QuikCSV([dict(
    data=[
        ['Column A', 'Column B', 'Column C'],
        ['100',      '101',      '102']
    ]
)])
def csv_func(csv_file):
    # Work with csv file here.
    #
    # QuikCSV.one will map the data above to mimic a csv file with the 
    # respective columns and rows, passing the file to the csv_file argument
    # (or by default, the first argument if there are multiple.)

```

If you want, you can specify the argument that the CSV mock file will be passed to.
```python

@QuikCSV([dict(
    data=[
        ['Column A', 'Column B', 'Column C'],
        ['100',      '101',      '102']
    ],
    arg='csv_file'
)])
def csv_func(first_arg, csv_file, third_arg):
    # Mock CSV will be accessible on the csv_file variable.

```

Options can be passed via the opts argument to quickly generate additional rows of data from existing rows.
```python

@QuikCSV([dict(
    data=[
        ['Column A', 'Column B', 'Column C'],
        ['100',      '101',      '102']
    ], 
    opts=dict(
        add_rows=2,
        row_pattern='copy',
        base_row_index=1
    )
)])
def csv_func(csv_file):
    # Output csv file will look like this:
    # 
    # Column A, Column B, Column C
    # 100,      101,      102
    # 100,      101,      102
    # 100,      101,      102
    # 
    # 2 rows of data are added, copied from index 1 of the passed data.

```
'copy' is a predefined row creation pattern to make things easy, but you can also pass a custom function
```python

@QuikCSV([dict(
    data=[
        ['Column A', 'Column B', 'Column C'],
        ['100',      '101',      '102']
    ], 
    opts=dict(
        add_rows=2,
        row_pattern=lambda x: [n + 1 for n in x],
        base_row_index=1
    )
)])
def csv_func(csv_file):
    # Output csv file will look like this:
    # 
    # Column A, Column B, Column C
    # 100,      101,      102
    # 101,      102,      103
    # 101,      102,      103
    # 
    # The passed function should apply against the row of data, not the 
    # individual element.

```
The above example applies the same function to the same row again and again, but by setting the 'incremental' option to True, the function will apply the newly created row of data on the next iteration. 
```python

@QuikCSV([dict(
    data=[
        ['Column A', 'Column B', 'Column C'],
        ['100',      '101',      '102']
    ], 
    opts=dict(
        add_rows=2,
        row_pattern=lambda x: [n + 1 for n in x],
        base_row_index=1,
        increment=True
    )
)])
def csv_func(csv_file):
    # Output csv file will look like this:
    # 
    # Column A, Column B, Column C
    # 100,      101,      102
    # 101,      102,      103
    # 102,      103,      104
    # 

```

#### Features in the works
* Random data generation - completely random or pseudo-random via user defined options