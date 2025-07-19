import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import VARCHAR, Integer, Float

# Load the enhanced CSV with ML predictions
df = pd.read_csv("churn_with_predictions.csv")

# Fix datatype if needed
df['SeniorCitizen'] = df['SeniorCitizen'].astype(int)

# Define SQL column types
dtype_mapping = {
    'customerID': VARCHAR(50),
    'gender': VARCHAR(10),
    'SeniorCitizen': Integer(),
    'Partner': VARCHAR(10),
    'Dependents': VARCHAR(10),
    'tenure': Integer(),
    'PhoneService': VARCHAR(10),
    'MultipleLines': VARCHAR(20),
    'InternetService': VARCHAR(20),
    'OnlineSecurity': VARCHAR(20),
    'OnlineBackup': VARCHAR(20),
    'DeviceProtection': VARCHAR(20),
    'TechSupport': VARCHAR(20),
    'StreamingTV': VARCHAR(20),
    'StreamingMovies': VARCHAR(20),
    'Contract': VARCHAR(20),
    'PaperlessBilling': VARCHAR(10),
    'PaymentMethod': VARCHAR(30),
    'MonthlyCharges': Float(),
    'TotalCharges': Float(),
    'Churn': Integer(),
    'PredictedChurn': Integer(),
    'ChurnProbability': Float()
}

# Create SQLAlchemy engine
engine = create_engine("mysql+pymysql://root:Neha%406283@localhost:3306/churn_db")

# Upload to MySQL
df.to_sql(
    name='customer_churn_predictions',
    con=engine,
    if_exists='replace',  # 'replace' recreates the table, use 'append' to add
    index=False,
    dtype=dtype_mapping
)

print("✅ ML predictions and customer data loaded into MySQL.")
