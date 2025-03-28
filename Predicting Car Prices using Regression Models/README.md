# 🚀 Predicting Car Prices using Regression Models

## 📖 Project Overview
This project focuses on **predicting car prices** using **regression models, feature selection, and regularization techniques**. By analyzing a real-world car dataset, we aim to build models that accurately estimate vehicle prices based on key attributes such as **brand, model, year, engine type, and mileage**.

---
## 📜 Table of Contents
1. 📌 **Introduction**
2. 📊 **Dataset Description and Preprocessing**
3. 🤖 **Regression Models and Performance on Validation Set**
4. 🏆 **Feature Selection Using Forward Selection**
5. 🔍 **Regularization Results**
6. 🎯 **Hyperparameter Tuning**
7. 📊 **Model Evaluation on Test Set**
8. 📝 **Reporting the Results**

---
## 📂 Project Details

### 🗂 Dataset
- **Cars Dataset** from YallaMotors 🏎️🚗
- 6,750 rows, 9 columns 📊
- Target Variable: **Car Price** 💰
- Preprocessing Steps:
  - Handling missing values ❌➡️✔️
  - Encoding categorical features 🔡➡️🔢
  - Normalization & standardization 📏📐
  - Data splitting (Train: 60%, Validation: 20%, Test: 20%)

### 🤖 Regression Models
- **Linear Models**:
  - Linear Regression 📈
  - LASSO (L1 Regularization) 🔍
  - Ridge Regression (L2 Regularization) 📉
- **Nonlinear Models**:
  - Polynomial Regression (Degree: 2 → 10) 🔄
  - Radial Basis Function (RBF) Kernel 🌐
- **Closed-Form vs. Gradient Descent**: Comparison of solutions ⚖️

### 🏆 Feature Selection
- **Forward Selection Method** 🔄➕
- Iterative feature addition to optimize model performance ✅
- Stops when additional features don’t improve results ⛔

### 🔍 Regularization Techniques
- **LASSO & Ridge Regression** to reduce overfitting ⚖️
- Grid Search to find optimal **λ** (regularization parameter) 🔍

### 🎯 Hyperparameter Tuning
- Grid Search to optimize model hyperparameters 🎛️

### 📊 Model Evaluation
- Metrics used:
  - **Mean Squared Error (MSE)** 📉
  - **Mean Absolute Error (MAE)** ⚖️
  - **R-squared (R²)** 📊
- Final model tested on unseen test data ✅

---
## 📁 Files in this Repository
- 📑 **`ML_assignment_2.pdf`**: Assignment description.
- 📝 **`Report.pdf`**: Analysis and discussion.
- 📝 **`Machine2.ipynb`**: Jupyter Notebook with full implementation.
- 📝 **`cars.csv`**: Dataset used for the project

---
## 🚀 How to Use
1️⃣ Clone this repository:
```bash
git clone https://github.com/zainabja52/Machine-Learning-and-Data-Science
cd Predicting Car Prices using Regression Models
```
2️⃣ Open **`Machine2.ipynb`** in **Jupyter Notebook** or **Google Colab**.
3️⃣ Run all cells to execute the analysis and view results.

---
## 📊 Results
This project explores multiple **regression models**, evaluates their performance using validation techniques, and applies **regularization methods** such as **Lasso and Ridge Regression** to enhance predictive accuracy. It also includes hyperparameter tuning using **Grid Search** and feature selection to optimize the final model.

---
## 📜 License
⚠️ This project is for **educational purposes only**.


