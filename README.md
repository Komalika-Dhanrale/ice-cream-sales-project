# Ice Cream Sales Prediction Project

## 1. Introduction

### 🎯 Objective
To build a simple machine learning model that predicts **Ice Cream Profit** based on the **Temperature**.

### ❓ Problem Statement
A business wants to understand how temperature affects ice cream sales. By analyzing the relationship between temperature and profit, the model can help forecast sales for different weather conditions.

### 📊 Dataset Description
- **Filename**: `ice_cream_sales.csv`
- **Columns**:
  - `Temperature`: Temperature in Celsius
  - `Ice Cream Profit`: Profit in dollars

---

## 2. Data Collection & Preprocessing

- ✅ Data Source: Local CSV file (`ice_cream_sales.csv`)
- ✅ Simple and clean dataset, so no missing values or outliers
- ✅ Split into input (X) and output (y)

---

## 3. Model Development

- 🔧 Algorithm Used: **Simple Linear Regression**
- 📁 Model File: `linear.pkl`
- 🧠 The model learns the linear relationship between temperature and profit

---

## 4. Model Deployment

- 🚀 Deployment Method: **Flask API**
- 📄 Main Script: `app.py`
- 🖥️ Frontend: Simple HTML form (`templates/index.html`)
- 🧠 Backend: Takes user input (temperature), loads model (`linear.pkl`), and returns predicted profit

---

## 5. Steps to Run the Project

1. Make sure you have Python installed
2. Install required libraries:

```bash
pip install flask pandas scikit-learn
