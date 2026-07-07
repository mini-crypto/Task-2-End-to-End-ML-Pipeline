import joblib
import pandas as pd

# Load trained pipeline
model = joblib.load("churn_pipeline.joblib")

# Example input (replace with actual customer data)
sample = pd.read_csv("sample_customer.csv")

prediction = model.predict(sample)

print(prediction)
