import pandas as pd
from scrapesquirrel import ScrapeSquirrel

df2 = pd.DataFrame()

# Let's say we got some more data from an API
df2['column1']=['x','y','z']
df2['column2']=['22','23','24']

# Dump into the older SQL from the first squirrel_test
sqrl = ScrapeSquirrel(df2, 'test')
sqrl.store()

