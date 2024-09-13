import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', index_col='Year')

    # Create scatter plot
    fig, ax = plt.subplots()
    fig.set_size_inches(10,7)
    ax.scatter(df.index, df['CSIRO Adjusted Sea Level'], s=4, c='b')

    # Create first line of best fit
    def line_equation(x, line_constants):
        return line_constants.intercept + (line_constants.slope * x)

    l1_vals = linregress(df.index, df['CSIRO Adjusted Sea Level'])
    x1_list = range(df.index.min(), 2051)
    y1_list = line_equation(x1_list, l1_vals)
    ax.plot(x1_list, y1_list, 'y-')


    # Create second line of best fit
    df2 = df.loc[df.index >= 2000]
    l2_vals = linregress(df2.index, df2['CSIRO Adjusted Sea Level'])
    x2_list = range(2000, 2051)
    y2_list = line_equation(x2_list, l2_vals)
    ax.plot(x2_list, y2_list, 'r-')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()