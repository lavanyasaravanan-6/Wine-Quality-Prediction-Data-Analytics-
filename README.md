# 🍷 Wine Quality Prediction – Data Analytics & Machine Learning

## 📌 Project Overview

The Wine Quality Prediction project focuses on analyzing the physicochemical properties of red and white wines to understand the factors that influence wine quality.

This project uses Python for data cleaning, exploratory data analysis, data visualization, and machine learning. A Random Forest Classifier is trained to predict wine quality based on its chemical properties.

## 🎯 Objectives

- Analyze red and white wine datasets.
- Clean and preprocess the collected data.
- Perform Exploratory Data Analysis (EDA).
- Identify important factors affecting wine quality.
- Visualize patterns and relationships using graphs.
- Build a machine learning model to predict wine quality.
- Evaluate model performance using classification metrics.

## 📂 Project Structure

```text
Wine_Quality_Prediction/
│
├── dataset/
│   ├── winequality-red.csv
│   └── winequality-white.csv
│
├── outputs/
│   ├── 01_wine_quality.png
│   ├── 02_wine_type.png
│   ├── 03_correlation_heatmap.png
│   ├── 04_alcohol_vs_quality.png
│   ├── 05_acidity_vs_quality.png
│   ├── 06_sugar_distribution.png
│   ├── 07_ph_distribution.png
│   ├── 08_sulphates_vs_quality.png
│   ├── 09_alcohol_vs_density.png
│   ├── 10_quality_by_type.png
│   ├── confusion_matrix.png
│   ├── cleaned_wine_data.csv
│   └── wine_quality_model.pkl
│
├── src/
│   ├── __init__.py
│   ├── data_loading.py
│   ├── data_cleaning.py
│   ├── data_exploration.py
│   ├── data_visualization.py
│   ├── feature_analysis.py
│   ├── model_training.py
│   ├── model_evaluation.py
│   └── prediction.py
│
├── main.py
├── requirements.txt
└── README.md

```

## 📊 Dataset Description

The project uses the Wine Quality dataset containing two datasets:

- Red Wine Dataset
- White Wine Dataset

The datasets contain physicochemical properties such as:

| Feature | Description |
|---|---|
| Fixed Acidity | Amount of fixed acids |
| Volatile Acidity | Amount of volatile acids |
| Citric Acid | Citric acid concentration |
| Residual Sugar | Remaining sugar content |
| Chlorides | Salt concentration |
| Free Sulfur Dioxide | Free sulfur dioxide level |
| Total Sulfur Dioxide | Total sulfur dioxide level |
| Density | Wine density |
| pH | Acidity or alkalinity level |
| Sulphates | Sulphate concentration |
| Alcohol | Alcohol percentage |
| Quality | Wine quality score |

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- VS Code

## ⚙️ Project Workflow

### 1. Data Loading
- Load red and white wine datasets using Pandas.
- Combine both datasets into a single DataFrame.
- Add a column to identify wine type.

### 2. Data Cleaning
- Check for missing values.
- Identify and remove duplicate records.
- Remove incomplete records.
- Reset the DataFrame index.

### 3. Exploratory Data Analysis (EDA)
- Understand dataset structure and dimensions.
- Generate descriptive statistics.
- Analyze wine quality distribution.
- Compare red and white wine counts.

### 4. Data Visualization

Create 10 visualizations to understand the dataset:

1. Wine Quality Distribution
2. Wine Type Distribution
3. Correlation Heatmap
4. Alcohol vs Wine Quality
5. Acidity vs Wine Quality
6. Sugar Distribution
7. pH Distribution
8. Sulphates vs Wine Quality
9. Alcohol vs Density
10. Wine Quality by Wine Type

### 5. Feature Analysis
- Calculate correlations between numerical features.
- Identify features associated with wine quality.
- Compare average chemical properties across quality scores.

### 6. Model Training
- Separate independent variables and target variable.
- Split the dataset into training and testing sets.
- Train a Random Forest Classifier.
- Use class balancing to address differences in class frequencies.

### 7. Model Evaluation

Evaluate the model using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- Confusion Matrix

### 8. Prediction

Use the trained model to predict the quality score of a wine sample.

## 📈 Results

After cleaning the combined dataset:

| Description | Result |
|---|---:|
| Initial Records | 6,497 |
| Records After Cleaning | 5,320 |
| Duplicate Records Removed | 1,177 |
| Visualizations Created | 10 |
| Machine Learning Algorithm | Random Forest Classifier |
| Model Accuracy | 51.41% |

**Note:** The reported accuracy is from the current baseline model and test split. Performance may vary with model settings and data preparation.

## 🔍 Key Findings

- Alcohol has the strongest positive correlation with wine quality in this dataset.
- Volatile acidity has a negative correlation with wine quality.
- Density also shows a negative correlation with quality.
- White wine records are more numerous than red wine records.
- Wine quality scores are concentrated mainly around 5 and 6.
- Rare quality classes have very few samples, making them harder to predict.

## 🚀 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the Project Folder

```bash
cd Wine_Quality_Prediction
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Project

```bash
python main.py
```

The program performs data loading, cleaning, exploration, visualization, feature analysis, model training, evaluation, and sample prediction.

Generated files are saved in the `outputs/` folder.

## 💡 Future Enhancements

- Compare multiple machine learning algorithms.
- Improve prediction performance.
- Build an interactive dashboard using Streamlit.
- Add user input for predicting custom wine samples.
- Perform more detailed statistical analysis.

## 👩‍💻 Author

**Lavanya S.**

Computer Science and Engineering Student

GitHub: [lavanyasaravanan-6](https://github.com/lavanyasaravanan-6)

## 🏷️ Internship

**Oasis Infobyte (OIBSIP)**

Data Analytics Internship – Level 2, Task 2

---

⭐ If you find this project useful, consider giving the repository a star!