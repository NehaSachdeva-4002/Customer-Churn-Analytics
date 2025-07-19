import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report
import joblib

print("🔄 Loading data...")
df = pd.read_csv("cleaned_churn.csv")

# Encode categorical columns
print("🔤 Encoding categorical variables...")
label_encoders = {}
for col in df.columns:
    if df[col].dtype == "object" and col != "customerID":
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

# Define features and target
print("📊 Preparing features and target...")
X = df.drop(columns=["customerID", "Churn"])
y = df["Churn"]

# Split data
print("✂️ Splitting data into train and test...")
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# Train model
print("🧠 Training RandomForest model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate on test set
print("📈 Evaluating model on test set...")
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("\n✅ Evaluation Results:")
print(f"🔹 Accuracy       : {accuracy:.4f}")
print(f"🔹 F1 Score       : {f1:.4f}")
print(f"🔹 Confusion Matrix:\n{conf_matrix}")
print("\n🔹 Classification Report:")
print(classification_report(y_test, y_pred))

# Predict on full dataset
print("🤖 Making batch predictions...")
df["PredictedChurn"] = model.predict(X)
df["ChurnProbability"] = model.predict_proba(X)[:, 1]

# Save updated dataset
print("💾 Saving churn_with_predictions.csv...")
df.to_csv("churn_with_predictions.csv", index=False)

# Save the model
print("💾 Saving churn_model.pkl...")
joblib.dump(model, "churn_model.pkl")

# Save label encoders
print("💾 Saving label encoders...")
joblib.dump(label_encoders, "label_encoders.pkl")

print("✅ All steps completed successfully!")
