
import os
import sys
import joblib

print("Starting Wine Quality Prediction Project...", flush=True)

try:
    from src.data_loading import load_data
    from src.data_cleaning import clean_data
    from src.data_exploration import explore_data
    from src.data_visualization import visualize_data
    from src.feature_analysis import analyze_features
    from src.model_training import train_model
    from src.model_evaluation import evaluate_model
    from src.prediction import predict_wine_quality

    print("All modules imported successfully!", flush=True)

    # Create output folder
    os.makedirs("outputs", exist_ok=True)

    # STEP 1: Load Dataset
    print("\nSTEP 1: LOADING DATASET", flush=True)

    wine = load_data()
    print("Dataset shape:", wine.shape, flush=True)

    # STEP 2: Clean Dataset
    print("\nSTEP 2: DATA CLEANING", flush=True)

    wine = clean_data(wine)
    print("Cleaned shape:", wine.shape, flush=True)

    # STEP 3: Explore Dataset
    print("\nSTEP 3: DATA EXPLORATION", flush=True)

    explore_data(wine)

    # STEP 4: Visualization
    print("\nSTEP 4: DATA VISUALIZATION", flush=True)

    visualize_data(wine)

    # STEP 5: Feature Analysis
    print("\nSTEP 5: FEATURE ANALYSIS", flush=True)

    analyze_features(wine)

    # STEP 6: Model Training
    print("\nSTEP 6: MODEL TRAINING", flush=True)

    model, X_test, y_test = train_model(wine)

    # STEP 7: Model Evaluation
    print("\nSTEP 7: MODEL EVALUATION", flush=True)

    accuracy = evaluate_model(model, X_test, y_test)

    # STEP 8: Save Model
    print("\nSTEP 8: SAVING MODEL", flush=True)

    joblib.dump(model, "outputs/wine_quality_model.pkl")

    print("Model saved successfully!", flush=True)

    # STEP 9: Sample Prediction
    print("\nSTEP 9: SAMPLE PREDICTION", flush=True)

    sample_wine = X_test.iloc[0].tolist()

    predicted_quality = predict_wine_quality(
        model,
        sample_wine
    )

    print("Predicted Quality:", predicted_quality, flush=True)

    # STEP 10: Save Cleaned Dataset
    wine.to_csv("outputs/cleaned_wine_data.csv", index=False)

    print("\nCleaned dataset saved!", flush=True)

    print("\n========================================")
    print(" PROJECT EXECUTION COMPLETED SUCCESSFULLY!")
    print("========================================")

except Exception as error:
    print("\nPROJECT ERROR:", error, flush=True)
    import traceback
    traceback.print_exc()
