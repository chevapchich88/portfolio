import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates = ['date'], index_col = 'date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

# Draw line plot
def draw_line_plot():
    fig, ax = plt.subplots(figsize = (15,8))
    ax.plot(df.index, df['value'], c = 'r', linewidth = 2)
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    fig.savefig('line_plot.png')
    return fig

# Draw bar plot
def draw_bar_plot():
    df['Year'] = df.index.year
    df['Months'] = df.index.month_name()
    df_bar = df.groupby(['Year', 'Months'])['value'].mean().unstack()
    df_bar = df_bar[['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']]
    fig = df_bar.plot.bar(figsize = (10, 10), ylabel = 'Average Page Views', xlabel = 'Years').figure
    fig.savefig('bar_plot.png')
    return fig

# Draw box plots
def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    fig, axes = plt.subplots(ncols = 2, nrows = 1, figsize = (16, 8))
    axes[0] = sns.boxplot(data = df_box, x = 'year', y = 'value', ax = axes[0])
    axes[1] = sns.boxplot(data = df_box, x = 'month', y = 'value', ax = axes[1], order = ['Jan', 'Feb', 'Mar', 'Apr','May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[0].set_xlabel('Year')
    axes[1].set_xlabel('Month')
    axes[0].set_ylabel('Page Views')
    axes[1].set_ylabel('Page Views')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    fig.savefig('box_plot.png')
    return fig
