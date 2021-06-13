import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')

# Clean data
df = df[((df['value'] <= df['value'].quantile(0.975)) & \
	(df['value'] >= df['value'].quantile(0.025)))]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(15,5))
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.plot(df)
    ax = plt.gca()
    ax.axes.xaxis.set_ticklabels([i[:7] for i in df.index if (i[4:] == '-07-01') or (i[4:] == '-01-01')])
    ax.axes.xaxis.set_ticks([i for i in df.index if (i[4:] == '-07-01') or (i[4:] == '-01-01')])

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['date'] = pd.to_datetime(df_bar['date'])
    df_bar['year'] = [d.strftime('%Y') for d in df_bar.date]
    df_bar['month'] = [d.strftime('%B') for d in df_bar.date]
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().reset_index()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 10))
    labels_ordered = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ax = sns.barplot(data=df_bar, x='year', y='value', hue='month', hue_order=labels_ordered)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(loc='upper left', title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['date'] = pd.to_datetime(df_box['date'])
    df_box['year'] = [d.strftime('%Y') for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=True, figsize=(20, 8))
    ax1 = sns.boxplot(data=df_box, x='year', y='value', ax=ax1)
    ax1.title.set_text('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    labels_ordered = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ax2 = sns.boxplot(data=df_box, x='month', y='value', order=labels_ordered, ax=ax2)
    ax2.title.set_text('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig