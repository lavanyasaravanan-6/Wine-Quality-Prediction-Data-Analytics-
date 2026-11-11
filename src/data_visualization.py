
import os
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(wine):

    os.makedirs("outputs", exist_ok=True)

    # 1. Wine Quality Distribution
    plt.figure(figsize=(8, 5))
    sns.countplot(data=wine, x="quality")
    plt.title("Wine Quality Distribution")
    plt.xlabel("Quality Score")
    plt.ylabel("Number of Wines")
    plt.tight_layout()
    plt.savefig("outputs/01_wine_quality_distribution.png")
    plt.show()

    # 2. Red vs White Wine Distribution
    plt.figure(figsize=(7, 5))
    sns.countplot(data=wine, x="Wine_Type")
    plt.title("Red vs White Wine Distribution")
    plt.tight_layout()
    plt.savefig("outputs/02_wine_type_distribution.png")
    plt.show()

    # 3. Correlation Heatmap
    numeric_data = wine.select_dtypes(include="number")
    plt.figure(figsize=(12, 8))
    sns.heatmap(
        numeric_data.corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )
    plt.title("Wine Features Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("outputs/03_correlation_heatmap.png")
    plt.show()

    # 4. Alcohol vs Quality
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=wine, x="quality", y="alcohol")
    plt.title("Alcohol Content vs Wine Quality")
    plt.tight_layout()
    plt.savefig("outputs/04_alcohol_vs_quality.png")
    plt.show()

    # 5. Volatile Acidity vs Quality
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=wine, x="quality", y="volatile acidity")
    plt.title("Volatile Acidity vs Wine Quality")
    plt.tight_layout()
    plt.savefig("outputs/05_acidity_vs_quality.png")
    plt.show()

    # 6. Residual Sugar Distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(data=wine, x="residual sugar", bins=30, kde=True)
    plt.title("Residual Sugar Distribution")
    plt.tight_layout()
    plt.savefig("outputs/06_sugar_distribution.png")
    plt.show()

    # 7. pH Distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(data=wine, x="pH", bins=30, kde=True)
    plt.title("Wine pH Distribution")
    plt.tight_layout()
    plt.savefig("outputs/07_ph_distribution.png")
    plt.show()

    # 8. Sulphates vs Quality
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=wine, x="quality", y="sulphates")
    plt.title("Sulphates vs Wine Quality")
    plt.tight_layout()
    plt.savefig("outputs/08_sulphates_vs_quality.png")
    plt.show()

    # 9. Alcohol vs Density
    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data=wine,
        x="alcohol",
        y="density",
        hue="Wine_Type",
        alpha=0.5
    )
    plt.title("Alcohol Content vs Density")
    plt.tight_layout()
    plt.savefig("outputs/09_alcohol_vs_density.png")
    plt.show()

    # 10. Quality by Wine Type
    plt.figure(figsize=(8, 5))
    sns.countplot(
        data=wine,
        x="quality",
        hue="Wine_Type"
    )
    plt.title("Wine Quality by Wine Type")
    plt.tight_layout()
    plt.savefig("outputs/10_quality_by_wine_type.png")
    plt.show()

    print("\nAll 10 visualizations created successfully!")
