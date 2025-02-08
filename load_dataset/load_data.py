import pandas as pd

def load_dataset():
    global df
    try:
        file=input("\nEnter the path of the dataset (CSV file):")
        df=pd.read_csv(file)
        if df.empty!=True:
            print("Dataset loaded successfully!")
        else:
            print("Failed to load dataset!")
    except FileNotFoundError:
        print("\nYour entered file is not found!")