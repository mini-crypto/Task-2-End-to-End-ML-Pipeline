# End-to-End ML Pipeline for Customer Churn Prediction

## Project Overview

This project demonstrates the development of a production-ready machine learning pipeline to predict customer churn using the Telco Customer Churn dataset. The project integrates data preprocessing, model training, hyperparameter tuning, evaluation, and model serialization into a reusable workflow using Scikit-learn's Pipeline API.

---

## Objective

The objective of this project is to build a reusable machine learning pipeline capable of accurately predicting whether a customer is likely to churn. The complete pipeline automates preprocessing and prediction, making it suitable for deployment in real-world applications.

---

## Dataset

**Dataset:** Telco Customer Churn Dataset

The dataset contains customer demographic information, subscribed services, account details, and whether the customer has churned.

**Target Variable:**

* Churn

  * 0 = No Churn
  * 1 = Churn

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Jupyter Notebook

---

## Project Workflow

1. Import required libraries.
2. Load and inspect the dataset.
3. Perform exploratory data analysis (EDA).
4. Handle missing values and clean the data.
5. Convert data types where necessary.
6. Separate features and target variable.
7. Split the dataset into training and testing sets.
8. Build preprocessing pipelines using:

   * SimpleImputer
   * StandardScaler
   * OneHotEncoder
   * ColumnTransformer
9. Train the following machine learning models:

   * Logistic Regression
   * Random Forest Classifier
10. Perform hyperparameter tuning using GridSearchCV.
11. Evaluate model performance using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

12. Compare model performance.
13. Export the best-performing pipeline using Joblib.

---

## Machine Learning Models

* Logistic Regression
* Random Forest Classifier

Both models were trained using Scikit-learn's Pipeline API to ensure that preprocessing and prediction occur within a single reusable workflow.

---

## Evaluation Metrics

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

GridSearchCV was used to optimize model hyperparameters through cross-validation.

---

## Model Export

The best-performing pipeline was saved using Joblib:

```python
joblib.dump(best_model, "churn_pipeline.joblib")
```

The saved model can later be loaded for predictions without retraining.

---

## Repository Structure

```
Task-2-End-to-End-ML-Pipeline/
│
├── Task2_End_to_End_ML_Pipeline.ipynb
├── README.md
├── requirements.txt
├── churn_pipeline.joblib
├── telco_churn.csv
└── images/
```

---

## Key Results

* Successfully built an end-to-end machine learning pipeline.
* Automated preprocessing using Pipeline and ColumnTransformer.
* Compared Logistic Regression and Random Forest models.
* Improved model performance through GridSearchCV.
* Exported the trained pipeline for future inference and deployment.

---

## Conclusion

This project demonstrates the implementation of a production-ready machine learning workflow using Scikit-learn. The final pipeline combines preprocessing, model training, hyperparameter tuning, evaluation, and model export into a single reusable solution suitable for customer churn prediction.
