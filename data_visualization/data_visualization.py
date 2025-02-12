import matplotlib.pyplot as plt
import numpy as np

def bar_plot():
    x_axis = ["A", "B", "C", "D"]
    y_axis = [3, 8, 1, 10]
    plt.bar(x_axis, y_axis)
    show_and_save_plot(plt.gcf())

def line_plot():
    y_axis = [3, 8, 1, 10]
    plt.plot(y_axis)
    show_and_save_plot(plt.gcf())

def scatter_plot():
    x_axis = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
    y_axis = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
    plt.scatter(x_axis, y_axis)
    show_and_save_plot(plt.gcf())

def pie_chart():
    x_axis = ["Apple", "Microsoft", "Google", "Amazon", "Meta"]
    y_axis = [25, 20, 30, 10, 15]
    plt.pie(y_axis, labels=x_axis, autopct="%.2f%%")
    show_and_save_plot(plt.gcf())

def box_plot():
    data_1 = np.random.normal(100, 10, 200)
    data_2 = np.random.normal(90, 20, 200)
    data_3 = np.random.normal(80, 30, 200)
    data_4 = np.random.normal(70, 40, 200)
    data = [data_1, data_2, data_3, data_4]
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.boxplot(data)
    show_and_save_plot(plt.gcf())

def hist_plot():
    data = [32, 96, 45, 67, 76, 28, 79, 62, 43, 81, 70, 61, 95, 44, 60, 69, 71, 23,
             69, 54, 76, 67, 82, 97, 26, 34, 18, 16, 59, 88, 29, 30, 66, 23, 65, 72,
             20, 78, 49, 73, 62, 87, 37, 68, 81, 80, 77, 92, 81, 52, 43, 68, 71, 86]
    plt.hist(data, color='red', edgecolor='green')
    show_and_save_plot(plt.gcf())

def stack_plot():
    days = [1, 2, 3, 4, 5]
    studying = [7, 8, 6, 11, 7]
    playing = [8, 5, 7, 8, 13]
    sleeping = [4, 8, 8, 10, 12]
    plt.stackplot(days, studying, playing, sleeping, labels=['Studying', 'Playing', 'Sleeping'])
    plt.legend(loc='upper left')
    show_and_save_plot(plt.gcf())

def show_and_save_plot(fig):
    plt.show()
    choice = input("\nDo you want to save this figure or not\nIf you want to save then enter the 'yes'\nIf you don't want to save this figure then enter the 'no'\nEnter your choice:").lower()
    if choice == 'yes':
        file_path = input("\nEnter the file path where you want to save this figure:")
        file_name = input("\nEnter the file name (without extension):")
        fig.savefig(f"{file_path}/{file_name}.png")
        print("Your file saved successfully!")
    elif choice == 'no':
        print("Thank you for use our application for visualization!")
    else:
        print("\nInvalid choice...")

def ask_to_user():
    while True:
        print("\nData Visualization")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Box Plot")
        print("6. Histogram")
        print("7. Stack Plot")
        print("8. Back to Main menu")
        graph_type = int(input("Enter your choice:"))

        if graph_type==1:
            bar_plot()
        elif graph_type==2:
            line_plot()
        elif graph_type==3:
            scatter_plot()
        elif graph_type==4:
            pie_chart()
        elif graph_type==5:
            box_plot()
        elif graph_type==6:
            hist_plot()
        elif graph_type==7:
            stack_plot()
        elif graph_type==8:
            break
        else:
            print("\nInvalid choice...")