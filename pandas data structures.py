import pandas as pd
import numpy as np
# series
dic = { 'Id': 1013, 'Name': 'MOhe',
	'State': 'Maniput','Age': 24}

res = pd.Series(dic)
print(res)

#dataframes
# Define a dictionary containing employee data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
		'Age': [27, 24, 22, 32],
		'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
		'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# select two columns
print(df[['Name', 'Qualification']])

# pannel

df1 = pd.DataFrame({'a': ['Garg', 'shivansh', 'is', 'real'],
					'b': [-11, +1.025, -114.48, 1333]})

df2 = pd.DataFrame({'a': ['I', 'am', 'dataframe', 'two'],
					'b': [100, 100, 100, 100]})

data = {'item1': df1, 'item2': df2}

# creating Panel
panel = pd.Panel.from_dict(data, orient='minor')
print("panel['b'] is - \n\n", panel['b'])

print("\nShape of panel['b'] is - ", panel['b'].shape)
