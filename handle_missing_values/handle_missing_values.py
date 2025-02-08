from load_dataset import load_data

def display_rows_with_missing_values():
    try:
        global null_rows
        null_rows=load_data.df[load_data.df.isnull().any(axis=1)]
        print(null_rows)
    except:
        print("\nDataset is not loaded yet!")
    
def fill_values_with_mean():
    try:
        global null_rows
        if null_rows.empty==True:
            print("\nDataframe is empty!")
        else:
            null_rows['ID'].fillna(null_rows['ID'].mean(),inplace=True)
            null_rows['Margin'].fillna(null_rows['Margin'].mean(),inplace=True)
            print("\nValues filled successfully!")
    except:
        print("\nDataset is not loaded yet!")

def drop_rows_with_missing_values():
    try:
        global null_rows
        null_rows.dropna(inplace=True)
        print(null_rows)
        print("\nRows dropped successfully!")
    except:
        print("\nDataset is not loaded yet!")
    
def replace_missing_values_with_specific_values():
    try:
        global null_rows
        if null_rows.empty==True:
            print("\nDataframe is empty!")
        else:
            value=float(input("Enter the value by which you want to fill the missing values:"))
            null_rows.fillna(value,inplace=True)
            print("\nValues filled successfully!")
    except:
        print("\nDataset is not loaded yet!")