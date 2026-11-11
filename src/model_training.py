from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_model(wine):

    # Separate input features and target
    X = wine.drop(columns=["quality", "Wine_Type"])
    y = wine["quality"]

    # Split dataset into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Create Random Forest model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight="balanced"
    )

    # Train the model
    model.fit(X_train, y_train)

    print("\nModel Training Completed!")

    return model, X_test, y_test