def generate_insights(df, column):
    insights = []

    insights.append(f"Column Name: {column}")

    insights.append(f"Mean Value: {round(df[column].mean(), 2)}")

    insights.append(f"Median Value: {round(df[column].median(), 2)}")

    insights.append(f"Minimum Value: {round(df[column].min(), 2)}")

    insights.append(f"Maximum Value: {round(df[column].max(), 2)}")

    insights.append(f"Missing Values: {round(df[column].isnull().sum())}")

    return insights