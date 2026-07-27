# Adult Census Income Classification

## Overview

This project develops a machine learning model to predict whether an individual's annual income exceeds **$50,000** based on demographic, educational, and employment-related information. The project demonstrates a complete end-to-end machine learning workflow, including data preprocessing, feature engineering, model training, and comparative evaluation using multiple classification algorithms.

---

## Dataset

**Dataset:** Adult Census Income Dataset

The dataset is derived from the **1994 U.S. Census Database** and contains demographic and employment information used for income prediction.

### Dataset Sources

- UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/adult
- Kaggle: https://www.kaggle.com/datasets/uciml/adult-census-income

**Dataset Statistics**

- Approximately 32,500 records
- 15 input attributes
- Binary target variable (Income)

### Target Classes

- **<=50K**
- **>50K**

---

## Objective

Build and evaluate machine learning models capable of predicting whether an individual's annual income is greater than **$50K** based on personal and occupational attributes.

This is a **Supervised Binary Classification** problem.

---

## Input Features

The dataset includes attributes such as:

- Age
- Workclass
- Education
- Education Number
- Marital Status
- Occupation
- Relationship
- Race
- Sex
- Capital Gain
- Capital Loss
- Hours per Week
- Native Country
- Final Weight (fnlwgt)

**Target Variable**

- Income

---

## Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

---

## Project Workflow

### 1. Data Exploration

- Load the dataset
- Inspect data types and structure
- Analyze feature distributions
- Identify missing values
- Explore the target variable

### 2. Data Preprocessing

- Handle missing values
- Encode categorical variables
- Scale numerical features
- Prepare the dataset for training

### 3. Model Development

The following classification models were implemented and compared:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)

### 4. Model Evaluation

Each model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score

Performance comparison was used to determine the most effective classifier for the dataset.

---

## Repository Structure

```
Adult-Census-Income-Classification/
│
├── Adult_Census_Income.ipynb
├── README.md
```

---

## Results

Multiple machine learning algorithms were trained and evaluated on the Adult Census Income dataset. The comparative analysis highlights the strengths of different classifiers in predicting income categories, providing insights into model performance across several evaluation metrics.

---

## Future Enhancements

- Hyperparameter Optimization
- Cross-Validation
- Feature Selection Techniques
- Ensemble Learning Methods
- XGBoost
- LightGBM
- CatBoost

---

## Learning Outcomes

This project demonstrates practical experience in:

- Exploratory Data Analysis (EDA)
- Data Cleaning and Preprocessing
- Feature Engineering
- Binary Classification
- Machine Learning Model Comparison
- Performance Evaluation using Classification Metrics

---

## References

1. UCI Machine Learning Repository – Adult Census Income Dataset
2. Kaggle – Adult Census Income Dataset
3. Scikit-learn Documentation
4. Pandas Documentation
5. NumPy Documentation
