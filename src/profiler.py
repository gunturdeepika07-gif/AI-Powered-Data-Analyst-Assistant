def get_shape(df):
    return df.shape


def get_dtypes(df):
    return df.dtypes

def get_misssing_values(df):
    return df.isnull().sum()

