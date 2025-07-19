import pandas as pd

df = pd.read_csv("Data.csv")
df.info()

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(subset=['TotalCharges'], inplace=True)
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
df['SeniorCitizen'] = df['SeniorCitizen'].map({1: 'Yes', 0: 'No'})

cols_to_clean = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
                 'TechSupport', 'StreamingTV', 'StreamingMovies', 'MultipleLines']
for col in cols_to_clean:
    df[col] = df[col].replace({'No internet service': 'No', 'No phone service': 'No'})

df.reset_index(drop=True, inplace=True)
df.to_csv("cleaned_churn.csv", index=False)

print("Cleaned Dataset Shape:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nNull Values:\n", df.isnull().sum())
print("\nSample Rows:\n", df.head())

df1 = pd.read_csv("cleaned_churn.csv")
# Show top rows and dtypes
print("\n🧾 Data Types in CSV:")
print(df1.dtypes)
