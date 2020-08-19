import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from pandastable import Table
import math

abalone_data = pd.read_csv("abalone.data.csv")
# load csv file into project folder, use .read_csv function to create pandas dataframe

abalone_data.columns = ["sex", "length", "diameter", "height", "whole weight", "shucked weight", "viscera weight",
                        "shell weight", "rings"]
abalone_data.index = range(1, abalone_data.shape[0] + 1)
abalone_data.name = "abalone data"


# if using new data make sure to update column names, indices, and dataframe name


# print(abalone_data)


def display_plot(dataframe, col1: str, col2: str):  # creates scatter plot between two columns in dataframe
    correlation = dataframe[col1].corr(dataframe[col2])
    # if col1 or col2 not in dataframe.columns:
    # return tk.messagebox.showerror(title="String Entry Warning!",
    # message="Warning, the string you entered is not a column name")
    img = dataframe.plot(x=col1, y=col2, kind="scatter", title=f"relationship between {col1} and {col2}")
    img.text(.1, .05, f"R={round(correlation, 4)}")  # shows the correlation between the variables on the side
    plt.show()


def display_histogram(dataframe, col1: str):  # creates a histogram for one column in the dataframe
    plt.hist(dataframe[col1], bins=math.floor(abalone_data.shape[0] ** .5))
    plt.title(f"Histogram for {col1}")
    plt.xlabel(col1)  # column we're analyzing forms the x axis
    plt.ylabel("frequency")
    plt.gcf().text(.1, .01, f"mean={round(dataframe[col1].mean(), 3)}, std ={round(dataframe[col1].std(), 2)}")
    # line 35 shows the mean and standard deviation of the sample.  For large sample sizes this can act as a visual
    # test for whether or not the sample has a Gaussian distribution
    plt.show()


def display_whisker(dataframe, col):  # creates a box-and-whisker plot for a single column in the dataframe
    dataframe.boxplot(column=col)
    plt.title(f"box and whisker plot for {col}")
    plt.show()


def get_stats(dataframe):
    # creates a new tkinter window (using the pandastable module)
    # with all the pandas descriptive statistics for the dataframe
    root = tk.Tk()

    frame1 = tk.Frame(root)
    frame1.pack(side="top")
    frame2 = tk.Frame(root)
    frame2.pack(side="bottom")

    root.title(f"Stats table for {dataframe.name}")

    tk.Label(frame1, text="1: count, 2: mean, 3: standard deviation, 4: minimum, 5: 25% quartile, "
                          "6: median, 7: 75% quartile, 8: max").pack()
    # row indexes can't be changed in pandastable, so we need to make a tkinter Label to display this information

    table = Table(frame2, dataframe=dataframe.describe(), width=750, height=200)
    table.show()

    root.mainloop()


def get_stats_for_var(dataframe, column: str):  # displays descriptive statistics for a single column in new window
    new_dataframe = ((dataframe.loc[:, [column]]).describe())
    new_dataframe.index = ["count", "mean", "standard deviation", "minimum", "25% quartile",
                           "median", "75% quartile", "max"]
    root = tk.Tk()
    root.title(f"descriptive statistics for {column}")

    frame1 = tk.Frame(root)
    frame1.pack(side="top")
    frame2 = tk.Frame(root)
    frame2.pack(side="bottom")

    tk.Label(frame1, text="1: count, 2: mean, 3: standard deviation, 4: minimum, 5: 25% quartile, "
                          "6: median, 7: 75% quartile, 8: max").pack()

    table = Table(frame2, dataframe=new_dataframe, width=300, height=200)
    table.show()

    root.mainloop()


def display_table(dataframe):
    # creates a pandastable for our entire dataframe in a new window
    # complete with buttons that execute the functions defined above
    root = tk.Tk()
    root.title(f"table for {dataframe.name}")

    frame1 = tk.Frame(root)
    frame1.pack(side="top")

    frame2 = tk.Frame(root)
    frame2.pack(side="bottom")  # can't display pandastable and label in same frame, must partition window

    tk.Label(frame1, text="choose a variable to analyze", justify="left").grid(row=0, column=0)

    var1 = tk.Entry(frame1, justify="left")
    var1.grid(row=0, column=1)

    tk.Label(frame1, text="choose another variable to analyze", justify="left").grid(row=1, column=0)

    var2 = tk.Entry(frame1, justify="left")
    var2.grid(row=1, column=1)

    tk.Button(frame1, text="create graph between variables",
              command=lambda: display_plot(dataframe, var1.get(), var2.get())).grid(row=2, column=0)
    # button displays scatter plot for the two entries above

    tk.Label(frame1, text="analyze single variable", justify="left").grid(row=0, column=2)

    var3 = tk.Entry(frame1, justify="left")
    var3.grid(row=0, column=3)

    tk.Button(frame1, text="get histogram", justify="center",
              command=lambda: display_histogram(dataframe, var3.get())) \
        .grid(row=2, column=2)

    tk.Button(frame1, text="get box-and-whisker plot", justify="center",
              command=lambda: display_whisker(dataframe, var3.get())) \
        .grid(row=2, column=3)

    tk.Button(frame1, text="get stats for single variable", justify="center",
              command=lambda: get_stats_for_var(dataframe, var3.get())) \
        .grid(row=0, column=4)
    # above 3 buttons use the single var3 entry to make the single-variable statistics plots

    tk.Button(frame1, text="get stats for all variables", justify="center",
              command=lambda: get_stats(dataframe)) \
        .grid(row=1, column=4)
    # above button opens new window with all descriptive statistics

    table = Table(frame2, dataframe=dataframe, width=750, height=600)  # creates table with dataframe
    table.show()

    root.mainloop()


display_table(abalone_data)
# all you need to do is execute the display_table function on any dataframe and you can do all the above analysis.
