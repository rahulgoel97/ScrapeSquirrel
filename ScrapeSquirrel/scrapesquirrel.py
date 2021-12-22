# Import requirements
import pandas as pd
import sqlite3
from os.path import exists

# Define the class

class ScrapeSquirrel():
    
    # Constructor
    def __init__(self, df, db_name):
        
        # The pandas dataframe 
        self.df = df

        # String of database name
        self.db_name = str(db_name) 
    
    # User facing function to invoke
    def store(self, remove_duplicates=True):
        

        """ 
         Stores the dataframe into an SQL database. Creates db if it doesn't     already exist. If exists, remove dups and save into SQL

        ===
        Inputs: remove_duplicates, default is True
        Output: No output but data saved in a sqlite .db 
        """



        # Check if database already exists
        path_to_file = self.db_name+'.db' # Path to the db on local folder
        
        if(exists(path_to_file)==True): # Exists already
            db_exists=True
        else:
            db_exists=False        
         
        # If database does not exist, create SQL database with df columns
        # If database exists, call pickleandsave()

        if(db_exists==False):
            self.create_sql()
        else:
            self.pickle_and_save()
    
    # Helper function to create SQL dataabse
    def create_sql(self):
        print(f"Trying to creating SQL db with name {self.db_name}.db")
        
        # Create the database
        db_full_name = str(self.db_name)+'.db'
        
        try: 
            conn = sqlite3.connect(db_full_name)
            c = conn.cursor()
            
            # Access the dataframe provided
            df = self.df
            df = df.drop_duplicates() # Bye, bye dups!!!

            # DEBUG - ----!!!!!!!!!!!!!!!!
            print("Dropped dups")
            
            # Save as pickle with matching name
            pickle_name = str(self.db_name)+".pkl"
            df.to_pickle(pickle_name)

            # Build the SQL querty
            col_names = df.columns # Columns required
            sql_query = "'''CREATE TABLE data_table ("
            
            # Add all the colmns as TEXT
            for col_name in col_names:
                sql_query = sql_query+f"{col_name} TEXT,\n"
            
            # Close out the querty
            sql_query = sql_query+");'''"
            
            # DEBUG!!!!!!!!!!!!!!!!!! ======++++++ %%%%%

            print(sql_query)
            
            # Now, execute the SQL query
            
            c.execute(sql_query)

            # Table created successfully
            print("Successfully created SQL database with table data_table")
        except:
            print("Error - couldn't create SQL database")


    # Helper function to pickle and save
    def pickle_and_save(self):
        print(f"Save the pickle as {self.db_name}.pkl and insert to {self.db_name}.db")

df = pd.DataFrame()
df['Name'] = ['Rahul', 'bigOther', 'Verve']
df['Sig'] = ['RealName', 'djName', 'idkman']

sqrl = ScrapeSquirrel(df=df, db_name="db_info")
sqrl.store()
