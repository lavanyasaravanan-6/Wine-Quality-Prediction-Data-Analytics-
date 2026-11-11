import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

def evaluate_model(model, X_test, y_test):

    # Predict wine quality
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    print("\nModel Evaluation Results")
    print("------------------------")

    print("Accuracy:", round(accuracy * 100, 2), "%")

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, zero_division=0))

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")

    plt.title("Wine Quality Confusion Matrix")
    plt.xlabel("Predicted Quality")
    plt.ylabel("Actual Quality")

    plt.tight_layout()
    plt.savefig("outputs/confusion_matrix.png")
    plt.show()

    print("\nModel Evaluation Completed!")

    return accuracy