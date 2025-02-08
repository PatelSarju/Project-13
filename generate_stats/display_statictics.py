from load_dataset import load_data

def display_stats():
    try:
        print(load_data.df.describe())
    except:
        print("\nDataset is not loaded yet!")