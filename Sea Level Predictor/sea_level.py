import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    lin = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    lin_y = lin.slope * df['Year'] + lin.intercept
    plt.plot(df['Year'], lin_y)
    # Create second line of best fit
    df_2000 = df.loc[df['Year'] >= 2000]
    lin_2000 = linregress(x=df_2000['Year'], y=df_2000['CSIRO Adjusted Sea Level'])
    lin_x_2000 = pd.Series([i for i in range(2000, 2051)])
    lin_y_2000 = lin_2000.slope * lin_x_2000 + lin_2000.intercept
    plt.plot(lin_x_2000, lin_y_2000, 'y')
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()
draw_plot()
