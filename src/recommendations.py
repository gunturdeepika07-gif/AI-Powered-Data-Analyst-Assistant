def generate_recommendations(df):
    recommendations = []

    missing = df.isnull().sum()
    for column, count in missing.items():
        if count>0:
            recommendations.append(f"Consider handiling {count} missing values in '{column}'.")

        numeric_df = df.select_dtypes(include=['int64', 'float64'])

        corr_matrix = numeric_df.corr()

        for col in corr_matrix.columns:
            for row in corr_matrix.index:
                if(col != row and abs(corr_matrix.loc[row, col]) > 0.8):
                    recommendations.append(f"'{row}' and '{col}' are strongly correlated.")
        if len(recommendations) == 0:
            recommendations.append("Dataset quality appears good.")

        return list(set(recommendations))                    