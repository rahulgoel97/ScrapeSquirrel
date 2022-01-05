import pandas as pd
from scrapesquirrel import ScrapeSquirrel

# Create dataframes
df1 = pd.DataFrame()
df2 = pd.DataFrame()

# Dummy data
df1['url']=[1,2,3,4]
df1['links']=[5,6,7,8]
df2['name']=['a','b','c','d']
df2['suffix']=['mr','mr','mrs','ms']

# Create one SQL database with 2 tables...

sqrl1 = ScrapeSquirrel(df1, 'datadb', 'first')
sqrl1.store()

sqrl2 = ScrapeSquirrel(df2, 'datadb', 'second')
sqrl2.store()