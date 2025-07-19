import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# 🔄 Load predictions dataset
df = pd.read_csv("churn_with_predictions.csv")

# 📊 Actual and predicted
y_true = df["Churn"]
y_pred = df["PredictedChurn"]

# 🧮 Metrics calculation
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# 📋 Save metrics in a DataFrame
metrics_df = pd.DataFrame({
    "Metric": ["Accuracy", "Precision", "Recall", "F1 Score", "True Positive", "False Positive", "False Negative", "True Negative"],
    "Value": [accuracy, precision, recall, f1, tp, fp, fn, tn]
})

# 💾 Save metrics to CSV for Power BI
metrics_df.to_csv("ml_metrics.csv", index=False)

print("✅ Metrics calculated and saved to 'ml_metrics.csv'")
