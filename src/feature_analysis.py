def analyze_features(wine):

    print("\nAverage Feature Values by Wine Quality:")

    print(
        wine.groupby("quality")
        .mean(numeric_only=True)
        .round(2)
    )

    print("\nCorrelation with Wine Quality:")

    correlation = wine.select_dtypes(include="number").corr()

    print(
        correlation["quality"]
        .sort_values(ascending=False)
    )