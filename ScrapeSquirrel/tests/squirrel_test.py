import pandas as pd
import sqlite3
from scrapesquirrel import ScrapeSquirrel


# Create a database
df = pd.DataFrame()
df['column1']  =['a', 'b', 'c']
df['column2'] = ['1','2','3']

# Try and dump into the database
sqrl = ScrapeSquirrel(df, 'test')
sqrl.store()


