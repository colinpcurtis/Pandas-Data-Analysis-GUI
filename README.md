# Pandas-Data-Analysis-GUI
We export csv files into a pandas dataframe and use pandastable and Tkinter to create a GUI that executes statistical analyses and creates plots using matplotlib.

This is used primarily as a data visualization tool by creating an easy to use table where we can select column names to either create plots or produce descriptive statistics. 

The data used in this project is a csv file of integer data atributes such as height, weight, sex, ect. from 4176 abalone, pulled from the UCI machine learning repository.  (https://data.world/uci/abalone)

If you decide to use this code on another dataset then you'll need to specify the column names and also the number of rows in the dataset, since the csv file does not have the column names pre-loaded and we don't want to zero-index our data.  Aside from that the GUI will execute any number of statistical analyses on your dataset.  
