def predict_wine_quality(model, features):

    prediction = model.predict([features])

    print("\nPredicted Wine Quality:", prediction[0])

    return prediction[0]