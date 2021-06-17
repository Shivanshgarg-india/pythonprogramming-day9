import pandas as pd
import numpy as np
# .DataFrame is a constructor

# create a dictionary
ex_dic = {
    'id': [100, 101, 102],
    'color': ['red', 'blue', 'red']
}

# create a list of strings
columns = ['id', 'color']

index = ['a', 'b', 'c']

# Passing a dictionary
# key: column name
# value: series of values
df = pd.DataFrame(ex_dict, columns=columns, index=index)
# list of lists
list_of_lists = [
    [100, 'red'],
    [101, 'blue'],
    [102, 'red']
]

# columns
columns = ['id', 'color']

pd.DataFrame(list_of_lists, columns=columns)


# create 4x2 random array
# array is a list of lists
arr = np.random.rand(4, 2)
arr

# columns
columns_new = ['one', 'two']

# pass in array and columns
pd.DataFrame(arr, columns=columns_new)

dict_new = {
    'student': np.arange(100, 110, 1),
    'test': np.random.randint(60, 101, 10)
}

pd.DataFrame(dict_new)
# we can set the index
pd.DataFrame(dict_new).set_index('student')
# creating a series

lst = ['round', 'square']
ind = ['c', 'b']
series_name = 'shape'

s = pd.Series(lst, index=ind, name=series_name)
