from load_dataset import load_data

def display_first_rows():
    try:    
        print(load_data.df.head())
    except:
        print("\nDataset is not loaded yet!")

def display_last_rows():
    try:
        print(load_data.df.tail())
    except:
        print("\nDataset is not loaded yet!")

def display_column_names():
    try:
        print(load_data.df.columns)
    except:
        print("\nDataset is not loaded yet!")

def display_data_types():
    try:
        print(load_data.df.dtypes)
    except:
        print("\nDataset is not loaded yet!")
    
def display_basic_info():
    try:
        load_data.df.info()
    except:
        print("\nDataset is not loaded yet!")