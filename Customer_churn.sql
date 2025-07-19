show databases;
# CREATE DATABASE churn_db;
CREATE TABLE customer_churn (
    customerID VARCHAR(50) PRIMARY KEY,
    gender VARCHAR(10),
    SeniorCitizen VARCHAR(5),
    Partner VARCHAR(10),
    Dependents VARCHAR(10),
    tenure INT,
    PhoneService VARCHAR(10),
    MultipleLines VARCHAR(20),
    InternetService VARCHAR(20),
    OnlineSecurity VARCHAR(20),
    OnlineBackup VARCHAR(20),
    DeviceProtection VARCHAR(20),
    TechSupport VARCHAR(20),
    StreamingTV VARCHAR(20),
    StreamingMovies VARCHAR(20),
    Contract VARCHAR(20),
    PaperlessBilling VARCHAR(10),
    PaymentMethod VARCHAR(30),
    MonthlyCharges DECIMAL(10,2),
    TotalCharges DECIMAL(10,2),
    Churn TINYINT
);
USE churn_db;
# C1 : Overall Churn Rate
SELECT 
  COUNT(*) AS total_customers,
  SUM(Churn) AS churned_customers,
  ROUND(100.0 * SUM(Churn) / COUNT(*), 2) AS churn_rate
FROM customer_churn;

# C2 Churn by Contract Type
SELECT 
  Contract,
  COUNT(*) AS total,
  SUM(Churn) AS churned,
  ROUND(100.0 * SUM(Churn) / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY Contract
ORDER BY churn_rate DESC;

# C3. Monthly Charges vs Churn
SELECT 
  Churn,
  ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charge,
  ROUND(AVG(TotalCharges), 2) AS avg_total_charge,
  COUNT(*) AS customers
FROM customer_churn
GROUP BY Churn;


# C4. Churn by Internet Service
SELECT 
  InternetService,
  COUNT(*) AS total_customers,
  SUM(Churn) AS churned_customers,
  ROUND(100.0 * SUM(Churn) / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY InternetService;


# C5. Churn by Tenure Bucket
SELECT 
  CASE
    WHEN tenure BETWEEN 0 AND 6 THEN '0-6 months'
    WHEN tenure BETWEEN 7 AND 12 THEN '7-12 months'
    WHEN tenure BETWEEN 13 AND 24 THEN '13-24 months'
    WHEN tenure BETWEEN 25 AND 48 THEN '25-48 months'
    ELSE '49+ months'
  END AS tenure_group,
  COUNT(*) AS total_customers,
  SUM(Churn) AS churned_customers,
  ROUND(100.0 * SUM(Churn) / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY tenure_group
ORDER BY tenure_group;


# C6. Churn by Payment Method
SELECT 
  PaymentMethod,
  COUNT(*) AS total_customers,
  SUM(Churn) AS churned,
  ROUND(100.0 * SUM(Churn) / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY PaymentMethod
ORDER BY churn_rate DESC;

# C7. Churn by Service Usage (e.g., Tech Support)
SELECT 
  TechSupport,
  COUNT(*) AS total_customers,
  SUM(Churn) AS churned,
  ROUND(100.0 * SUM(Churn) / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY TechSupport;


# C8 Overall Actual vs Predicted Churn
SELECT 
  COUNT(*) AS total_customers,
  SUM(Churn) AS actual_churned,
  SUM(PredictedChurn) AS predicted_churned,
  ROUND(100.0 * SUM(Churn) / COUNT(*), 2) AS actual_churn_rate,
  ROUND(100.0 * SUM(PredictedChurn) / COUNT(*), 2) AS predicted_churn_rate
FROM customer_churn_predictions;

# C9. Churn Probability Buckets
SELECT
  CASE
    WHEN ChurnProbability < 0.2 THEN 'Very Low'
    WHEN ChurnProbability BETWEEN 0.2 AND 0.5 THEN 'Low'
    WHEN ChurnProbability BETWEEN 0.5 AND 0.8 THEN 'Medium'
    ELSE 'High'
  END AS risk_level,
  COUNT(*) AS customer_count
FROM customer_churn_predictions
GROUP BY risk_level
ORDER BY FIELD(risk_level, 'Very Low', 'Low', 'Medium', 'High');


# C10: Predicted High-Risk Customers (ChurnProbability > 0.8)
SELECT 
  customerID,
  ChurnProbability,
  MonthlyCharges,
  tenure,
  Contract,
  InternetService
FROM customer_churn_predictions
WHERE ChurnProbability > 0.8
ORDER BY ChurnProbability DESC
LIMIT 20;

