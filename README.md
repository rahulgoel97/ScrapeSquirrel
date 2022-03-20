# ScrapeSquirrel 🐿️
The world's easiest way of saving scraped data in an SQL database. Automatically creates SQL database &amp; treats duplicates.


# About
- Dumps scraped pandas dataframes into SQL databases and mostly abstracts away SQL related code
- Could be used to scrape information over time. All entered data is stored even if the scraped data changes, such as data from a daily stock price API
- Built scrapesquirrel based on my personal workflows, but hope it works for you

# Usage

```
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
# "Store df1 in a database called datadb, in a table called first"
sqrl1 = ScrapeSquirrel(df1, 'datadb', 'first')
sqrl1.store()

# "Store df1 in a database called datadb, in a table called second"
sqrl2 = ScrapeSquirrel(df2, 'datadb', 'second')
sqrl2.store()
```

- You can seamlessly change the database and table names as required
