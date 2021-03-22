import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date']=pd.to_datetime(df['date'])
#df['month']=df['date'].dt.month
#df['year']=df['date'].dt.year
df.set_index('date',inplace=True)
#print(df.dtypes)
#print(df.index)
#print (df.info())

# Clean data
df = df[(df['value']<=df['value'].quantile(0.975))& (df['value']>=df['value'].quantile(0.025))]
print(df)

def draw_line_plot():
    # Draw line plot
    fig,axs=plt.subplots(1,1)
    fig.set_figwidth(15)
    fig.set_figheight(5)
    df['value'].plot(color='maroon')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    #plt.show()
  
   
    #ax=fig.axes[0].legend()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot

    """#I change the way of doing. Still in this way some errors detected.
    df_b=df.copy()
    df_b.reset_index(inplace=True)
    df_b['year']= df_b['date'].dt.year
    df_b['Months']= df_b['date'].dt.month
    df_b.set_index('date', inplace=True)
    df_bar=df_b.resample('M').mean()
    df_bar['year']=df_bar['year'].astype(int)

    df_bar['Months']=df_bar['Months'].replace(1.0,'January')
    df_bar['Months']=df_bar['Months'].replace(2.0,'February')
    df_bar['Months']=df_bar['Months'].replace(3.0,'March')
    df_bar['Months']=df_bar['Months'].replace(4.0,'April')
    df_bar['Months']=df_bar['Months'].replace(5.0,'May')
    df_bar['Months']=df_bar['Months'].replace(6.0,'June')
    df_bar['Months']=df_bar['Months'].replace(7.0,'July')
    df_bar['Months']=df_bar['Months'].replace(8.0,'August')
    df_bar['Months']=df_bar['Months'].replace(9.0,'September')
    df_bar['Months']=df_bar['Months'].replace(10.0,'October')
    df_bar['Months']=df_bar['Months'].replace(11.0,'November')
    df_bar['Months']=df_bar['Months'].replace(12.0,'Dicember')

    #df_b = df.groupby(df['month']).mean()
    #print(df_b)
    #print(df_bar)

   # Draw bar plot

    g=sns.catplot(x='year', y='value', data=df_bar, kind='bar', hue='Months')
    g.set(xlabel="Years")
    g.set(ylabel="Average Page Views")

    #plt.show()
    
    fig,axs=plt.subplots(1,1)"""
    
    df_bar = df.copy()

    # Draw bar plot
    leglab = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    labels = [2016, 2017, 2018, 2019]
    months = np.zeros([12, 4])

    for i in range(12):
        for j, year in enumerate(labels):
            t = df[df.index.year == year]
            months[i][j] = t[t.index.month == i].value.mean()

    x = np.arange(len(labels))
    width = 0.7
    fig, ax = plt.subplots()
    fig.set_figwidth(10)
    fig.set_figheight(8)
    for i, month in enumerate(months):
        ax.bar(x - (width * (12 - i) / 12), months[i], width / 12, label=leglab[i])

    ax.set_ylabel("Average Page Views")
    ax.set_xlabel("Years")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(title='Months')

   # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_figwidth(10)
    fig.set_figheight(5)
    
    ax1=sns.boxplot(x=df_box['year'], y=df_box['value'], ax=ax1)
    ax1.set(xlabel='Year', ylabel='Page Views')
    ax1.axes.set_title('Year-wise Box Plot (Trend)')

    ax2=sns.boxplot(x='month', y='value', data=df_box, order=['Jan','Feb','Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ax=ax2)
    ax2.set (xlabel='Month', ylabel='Page Views')
    ax2.axes.set_title('Month-wise Box Plot (Seasonality)')
    #plt.show()

    #fig=plt.figure()

   # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

