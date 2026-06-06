import matplotlib.pyplot as plt
import seaborn as sns

def create_histogram(df, column):
    fig, ax = plt.subplots()
    ax.hist(df[column])
    ax.set_title(f"{column} Distribution")
    return fig


def create_boxplot(df, column):
    fig, ax = plt.subplots()
    ax.boxplot(df[column])
    ax.set_title(column)
    return fig


def create_heatmap(df):

    numeric_df = df.select_dtypes(
        include=['int64', 'float64']
    )

    fig, ax = plt.subplots(figsize=(8, 6))

    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="coolwarm",
        ax=ax
    )

    return fig