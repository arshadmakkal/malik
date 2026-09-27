import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def draw_line_plot():
    # Copy the data
    df = data.copy()

    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df.index, df['value'])

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save and return image
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy the data
    df = data.copy()

    # Create year and month columns
    df['year'] = df.index.year
    df['month'] = df.index.month

    # Average page views by year and month
    df_bar = df.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw bar plot
    fig = df_bar.plot(
        kind='bar',
        figsize=(12, 6)
    ).figure

    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(
        title='Months',
        labels=[
            'January', 'February', 'March', 'April',
            'May', 'June', 'July', 'August',
            'September', 'October', 'November', 'December'
        ]
    )

    # Save and return image
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Copy the data
    df = data.copy()

    # Prepare data
    df.reset_index(inplace=True)
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.strftime('%b')

    # Order months
    month_order = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]

    df['month'] = pd.Categorical(
        df['month'],
        categories=month_order,
        ordered=True
    )

    # Draw box plots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    sns.boxplot(
        data=df,
        x='year',
        y='value',
        ax=axes[0]
    )

    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(
        data=df,
        x='month',
        y='value',
        ax=axes[1]
    )

    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save and return image
    fig.savefig('box_plot.png')
    return fig


# Import data
data = pd.read_csv(
    'fcc-forum-pageviews.csv',
    parse_dates=['date'],
    index_col='date'
)

# Clean data
data = data[
    (data['value'] >= data['value'].quantile(0.025)) &
    (data['value'] <= data['value'].quantile(0.975))
]
