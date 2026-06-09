def generate_summary(df, column):

    count = df[column].count()
    mean = round(df[column].mean(), 2)
    median = round(df[column].median(), 2)
    minimum = round(df[column].min(), 2)
    maximum = round(df[column].max(), 2)
    missing = df[column].isnull().sum()



    summary = f"""
The '{column} column contains {count} observations.

The average value is {mean}, while the median value is {median}.

The minimum value observed is {minimum}, and the maximum value is {maximum}.

"""
    return summary
