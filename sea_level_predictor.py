import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    df.plot.scatter(x='Year', y='CSIRO Adjusted Sea Level')
    # Create first line of best fit
    slope, intercept = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])[:2]
    x_data_2050 = np.arange(min(df['Year']), 2051)
    y_data_2050 = slope * x_data_2050 + intercept

    plt.plot(x_data_2050, y_data_2050, color='red')


    # Create second line of best fit
    data_2000 = df[df['Year'] >= 2000]
    x_data_2000 = data_2000['Year']
    y_data_2000 = data_2000['CSIRO Adjusted Sea Level']
    x_data_2050 = np.arange(min(x_data_2000), 2051)
    slope, intercept = linregress(x_data_2000, y_data_2000)[:2]
    y_data_2050 = slope * x_data_2050 + intercept
    plt.plot(x_data_2050, y_data_2050, color='green')
   
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()