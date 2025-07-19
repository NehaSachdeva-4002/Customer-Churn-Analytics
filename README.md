# 📉 Customer Churn Prediction Dashboard (Power BI)

Welcome to my Customer Churn Dashboard project! This interactive Power BI dashboard is built to help businesses understand why customers leave — and how we can predict it before it happens.

By combining **SQL**, **Machine Learning**, and **Power BI**, this project tells a data story that helps stakeholders make smarter, proactive decisions.

---
<img width="1288" height="715" alt="image" src="https://github.com/user-attachments/assets/4a32c675-6e83-4a37-b57d-144406ffaa2f" />
<img width="1289" height="737" alt="image" src="https://github.com/user-attachments/assets/9dfb7fb9-4df7-4d7f-8ba7-f975e50dc4be" />



## 💡 Why This Project?

Customer churn is a major challenge for many companies. So, I set out to build a tool that could:

- Analyze existing churn trends (Who’s leaving? When? Why?)
- Predict future churn using ML probabilities
- Help business teams take action before it’s too late

---

## 🧭 What's Inside?

### 1️⃣ **Customer Churn Overview**

A quick glance at actual churn data:
- Churn % by Gender, Age Group, Subscription Type, etc.
- How tenure and monthly charges influence churn
- Simple slicers to filter and compare across segments

### 2️⃣ **Churn Predictions & Model Evaluation**

Using machine learning outputs:
- See how well the model performed (accuracy, precision, recall, F1-score)
- Explore a breakdown of predicted churn probabilities
- Customers are grouped into **5 churn risk buckets**:
  - 🔵 Very Low (0–0.2)
  - 🟢 Low (0.2–0.4)
  - 🟡 Medium (0.4–0.6)
  - 🟠 High (0.6–0.8)
  - 🔴 Very High (0.8–1.0)

---

## 🧮 How SQL Was Used

SQL played a key role in data preprocessing and filtering before loading it into Power BI. Specifically:

- Querying and transforming raw customer data
- Calculating churn indicators based on historical transactions
- Creating clean views/tables for ML predictions and dashboard visuals
- Joining predictions with customer metadata for richer segmentation

The final dataset was then connected to Power BI for visualization and analysis.

---

## 📊 Tech Stack

| Tool | Purpose |
|------|---------|
| **SQL** | Data extraction, joins, and preprocessing |
| **Python** | Built ML model to predict churn probability |
| **Power BI** | Dashboard design, interactivity, storytelling |
| **DAX** | Used for dynamic calculations and risk segmentation |

Here’s an example of a DAX measure used for churn risk bucketing:

```dax
Churn_Risk_Bucket = 
SWITCH(
    TRUE(),
    customer_churn_predictions[ChurnProbability] <= 0.2, "Very Low (0–0.2)",
    customer_churn_predictions[ChurnProbability] <= 0.4, "Low (0.2–0.4)",
    customer_churn_predictions[ChurnProbability] <= 0.6, "Medium (0.4–0.6)",
    customer_churn_predictions[ChurnProbability] <= 0.8, "High (0.6–0.8)",
    "Very High (0.8–1.0)"
)
