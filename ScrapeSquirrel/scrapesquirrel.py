# Import requirements
import pandas as pd
import sqlite3
from os.path import exists

# Define the class

class ScrapeSquirrel():
    
    # Constructor
    def __init__(self, df, db_name, table_name):
        
        # The pandas dataframe 
        self.df = df

        # String of database name
        self.db_name = str(db_name) 

        # Table nname
        self.table_name = str(table_name)
    
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

        # Variables

        db_name = self.db_name
        table_name = self.table_name

        # Message to user

        print(f"Trying to creating SQL db with name {db_name}_{table_name}.db")
        
        # Create the database
        db_full_name = str(self.db_name)+'.db'
        
        try: 
            conn = sqlite3.connect(db_full_name)
            c = conn.cursor()
            
            # Access the dataframe provided
            df = self.df
            df = df.drop_duplicates() # Bye, bye dups!!
            
            # Save as pickle with matching name
            pickle_name = str(self.db_name)+"_"+str(self.table_name)+".pkl"
            df.to_pickle(pickle_name)

            # Build the SQL querty
            col_names = df.columns # Columns required
            sql_query = f'''CREATE TABLE {table_name} ('''
            
            # Add all the colmns as TEXT
            for idx, col_name in enumerate(col_names):
                total_columns = len(col_names)
                total_column_indices = total_columns-1
    
                if(idx!=total_column_indices):
                    sql_query = sql_query+f'''\n\t{col_name} TEXT,'''
                else:
                    sql_query = sql_query+f'''\n\t{col_name} TEXT''' # no comma

            # Close out the querty
            sql_query = sql_query+'''\n);'''
            
            
            # Now, execute the SQL query
            
            c.execute(sql_query)
            
            # Add the pickle info
            df.to_sql(str(self.table_name), conn, if_exists="replace", index=False)

            # Table created successfully
            print(f"Successfully created SQL database {db_full_name} with table {table_name}")
        except Exception as e:
            print("Error - couldn't create SQL database: ", e)


    # Helper function to pickle and save
    def pickle_and_save(self):

        # Variables
        table_name = self.table_name
        db_name = self.db_name
        
        print(f"Detected {db_name}.db to be updated")


        # Retrieve the old dataframe and append to create unified source
        pickle_name = str(self.db_name)+"_"+str(self.table_name)+'.pkl'
        
        try: # Assuming this is already a table
            
            df_old = pd.read_pickle(pickle_name)
            print(f"Existing table {table_name} detected")
    
            # Add the new data to the older pickle file
            new_df = df_old.append(self.df)
            
            
            # Overwrite the older pickle file
            new_df.to_pickle(pickle_name)

            new_df = new_df.drop_duplicates() # This is the new df with no dups

        except: # New Table
            print(f"Creating a new table {table_name}...")

            new_df = self.df

            # Save as pickle with matching name
            pickle_name = str(self.db_name)+"_"+str(self.table_name)+".pkl"
            new_df.to_pickle(pickle_name)

            new_df = new_df.drop_duplicates() # This is the new df with no dups

        # Open up SQL database
        db_path = str(self.db_name)+'.db'
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        # Replace the data with the uniques
        new_df.to_sql(self.table_name, conn, if_exists="replace", index=False)

        # Output a success message

        print(f"Successfully updated the SQL database.")


