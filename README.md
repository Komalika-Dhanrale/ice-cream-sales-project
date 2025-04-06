# Ice Cream Sales Prediction Project

## 1. Introduction

### 🎯 Objective:
To build a machine learning model that predicts ice cream profits based on temperature.

### ❓ Problem Statement:
Ice cream sales are influenced by temperature. The goal is to help businesses predict expected profits based on weather forecasts.

### 📂 Dataset Description:
The dataset contains two columns:
- `Temperature`: Temperature in Celsius
- `Ice Cream Profits`: Profit in dollars

---

## 2. Data Collection & Preprocessing

### 📊 Data Source:
The dataset (`ice_cream_sales.csv`) is locally stored.

### 🔍 Preprocessing:
- Checked for missing values
- Converted data into input/output format for model training

---

## 3. Model Development

### 🧠 Algorithm Used:
- **Linear Regression** from `sklearn.linear_model`

### 🛠️ Model Training Script:
- The model was trained using `train_model.py`
- The trained model is saved as `model/linear_model.pkl`

---

## 4. Model Deployment

### 🌐 Deployment Method:
- Deployed using **Flask**
- Routes:
  - `/` → Home page (input form)
  - `/predict` → Receives input and returns prediction result

---

## 5. Steps to Run the Deployed Model

1. Clone the repository or download project files.
2. Ensure required libraries are installed:
   ```bash
   pip install flask pandas scikit-learn

