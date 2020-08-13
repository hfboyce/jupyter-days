import pandas as pd 

# This code will run relative to the root of the repo, so we can load files from the root or a url 

data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/beers.csv')

# display the first 5 rows 
data.head()