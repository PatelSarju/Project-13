from load_dataset import load_data
from explore_dataset import explore_dataset
from dataframes_operations import data_frames_operations
from handle_missing_values import handle_missing_values
from generate_stats import display_statictics
from data_visualization import data_visualization

class DataAnalyzer:
    def __init__(self):
        while True:
            print("\nPlease select an option:")
            print("1. Load Dataset")
            print("2. Explore Data")
            print("3. Perform DataFrame Operations")
            print("4. Handle Missing Data")
            print("5. Generate Descriptive Statistics")
            print("6. Data Visualization")
            print("7. Exit")
            choice=int(input("Enter your choice:"))
            
            if choice==1:
                load_data.load_dataset()
            elif choice==2:
                while True:
                    print("\nExplore data")
                    print("1. Display the first 5 rows")
                    print("2. Display the last 5 rows")
                    print("3. Display column names")
                    print("4. Display data types")
                    print("5. Display basic info")
                    print("6. Back to main menu")
                    choice1=int(input("Enter your choice:"))
                    if choice1==1:
                        explore_dataset.display_first_rows()
                    elif choice1==2:
                        explore_dataset.display_last_rows()
                    elif choice1==3:
                        explore_dataset.display_column_names()
                    elif choice1==4:
                        explore_dataset.display_data_types()
                    elif choice1==5:
                        explore_dataset.display_basic_info()
                    elif choice1==6:
                        break
                    else:
                        print("\nInvalid choice...")  
            
            elif choice==3:
                while True:
                    print("\nDataFrame Operations:")
                    print("1. Slicing")
                    print("2. Re-index")            
                    print("3. Pivoting")
                    print("4. Back to main menu")
                    choice2=int(input("Enter your choice:"))
                    if choice2==1:
                        data_frames_operations.slicing()
                    elif choice2==2:
                        data_frames_operations.re_index()
                    elif choice2==3:
                        data_frames_operations.pivoting()
                    elif choice2==4:
                        break
                    else:
                        print("\nInvalid choice...")
                    
            elif choice==4:
                while True:
                    print("\nHandle missing values:")
                    print("1. Display rows with missing values")
                    print("2. Fill missing values with mean")
                    print("3. Drop rows with missing values")
                    print("4. Replace missing values with a specific value")
                    print("5. Back to main menu")
                    choice3=int(input("Enter your choice: "))
                    if choice3==1:
                        handle_missing_values.display_rows_with_missing_values()
                    elif choice3==2:
                        handle_missing_values.fill_values_with_mean()
                    elif choice3==3:
                        handle_missing_values.drop_rows_with_missing_values()
                    elif choice3==4:
                        handle_missing_values.replace_missing_values_with_specific_values()
                    elif choice3==5:
                        break    
                    else:       
                        print("\nInvalid choice...")
            
            elif choice==5:
                display_statictics.display_stats()
            elif choice==6: 
                data_visualization.ask_to_user()
            elif choice==7:
                print('\nYou are exit from the application!')
                break
            else:
                print("\nInvalid choice...")

analyzer=DataAnalyzer()