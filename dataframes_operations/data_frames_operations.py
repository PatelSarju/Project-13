from load_dataset import load_data

def slicing():
    try:
        start=0
        end=10
        print(load_data.df.iloc[[start,end],:])
    except:
        print("\nDataset is not loaded yet!")
    
def re_index():
    try:
        load_data.df['new_index']=[i for i in range(100,1050)]
        load_data.df.reset_index()
        udpated_df=load_data.df.set_index('new_index')
        load_data.df.drop(columns='new_index')
        print(udpated_df)
    except:
        print("\nDataset is not loaded yet!")

def pivoting():
    try:
        pivot_df=load_data.df.pivot_table(index='Team1',columns='Venue',values='Margin',aggfunc='mean')
        print(pivot_df)
    except:
        print("\nDataset is not loaded yet!")