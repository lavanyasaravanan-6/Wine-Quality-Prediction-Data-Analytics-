def explore_data(wine):

    print("\nDataset Information:")
    print(wine.info())

    print("\nDataset Shape:")
    print(wine.shape)

    print("\nStatistical Summary:")
    print(wine.describe())

    print("\nWine Quality Distribution:")
    print(wine["quality"].value_counts().sort_index())

    print("\nWine Type Distribution:")
    print(wine["Wine_Type"].value_counts())