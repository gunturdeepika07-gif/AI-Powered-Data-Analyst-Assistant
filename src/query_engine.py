def answer_question(df, question):

    question = question.lower()

    # Average
    if "average" in question or "mean" in question:
        for col in df.select_dtypes(include="number").columns:
            if col.lower() in question:
                return f"The average {col} is {round(df[col].mean(), 2)}"

        return "Please mention a numeric column."

    # Missing values
    elif "missing" in question:

        missing = df.isnull().sum()

        return missing.to_string()

    # Maximum value
    elif "maximum" in question or "highest" in question:

        results = {}

        for col in df.select_dtypes(include="number").columns:
            results[col] = df[col].max()

        highest_column = max(results, key=results.get)

        return (
            f"{highest_column} has the highest maximum value "
            f"({round(results[highest_column], 2)})"
        )

    # Unique values
    elif "unique" in question:

        unique_counts = df.nunique()

        highest_column = unique_counts.idxmax()

        return (
            f"{highest_column} has the most unique values "
            f"({unique_counts.max()})"
        )

    else:
        return "Sorry, I don't understand that question yet."