import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    result_linregress_first = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope_first = result_linregress_first.slope
    intercept_first = result_linregress_first.intercept
    xvalues_first = list(range(1880, 2051))
    yvalues_first = [slope_first * year + intercept_first for year in xvalues_first]
    plt.plot(xvalues_first, yvalues_first, '--')

    # Create second line of best fit
    result_linregress_second = linregress(df['Year'][(df[df['Year'] == 2000].index.values.astype(int)[0]):], df['CSIRO Adjusted Sea Level'][df[df['Year'] == 2000].index.values.astype(int)[0]:])
    slope_second = result_linregress_second.slope
    intercept_second = result_linregress_second.intercept
    xvalues_second = list(range(2000, 2051))
    yvalues_second = [slope_second * year + intercept_second for year in xvalues_second]
    plt.plot(xvalues_second, yvalues_second, '--')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()