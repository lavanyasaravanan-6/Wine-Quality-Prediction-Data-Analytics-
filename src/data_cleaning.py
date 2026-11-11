def clean_data(wine):

    wine = wine.copy()

    print("\nMissing Values:")
    print(wine.isnull().sum())

    print("\nDuplicate Rows:", wine.duplicated().sum())

    wine.drop_duplicates(inplace=True)
    wine.dropna(inplace=True)

    wine.reset_index(drop=True, inplace=True)

    print("\nData Cleaning Completed!")

    return wine