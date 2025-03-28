# 🌸 Iris Species Classification using Machine Learning

## 📖 Project Overview  
This project compares **K-Nearest Neighbors (KNN), Logistic Regression, Support Vector Machines (SVM), and Ensemble Methods** to classify Iris species (Setosa, Versicolor, Virginica) using the classic Iris dataset. The goal is to evaluate model performance, tune hyperparameters, and analyze the impact of distance metrics, kernels, and regularization.

---
## 📜 Table of Contents  
1. 📌 **Introduction**  
2. 📊 **Dataset & Preprocessing**  
3. 🤖 **Models and Performance**  
4. 🔍 **Hyperparameter Tuning**  
5. 🏆 **Ensemble Methods**  
6. 📝 **Evaluation Metrics**  
7. 📁 **Files**  
8. 🚀 **How to Run**  

---
## 📂 Project Details  

### 🗂 Dataset  
- **Iris Dataset** 🌺  
- 150 samples | 4 features: Sepal/Petal Length/Width | 3 classes (50 each)  
- **Preprocessing**:  
  - Standard scaling for KNN/SVM 📏  
  - Train-test split (70-30) 🔄  
  - No feature selection needed (clean, balanced data) ✅  

### 🤖 Models Tested  
1. **KNN**  
   - Metrics: Euclidean, Manhattan, Cosine 🌍📏  
   - Optimal K via 5-fold cross-validation 🎯  
2. **Logistic Regression**  
   - L1/L2 regularization for multi-class (OvR) 🔄  
3. **SVM**  
   - Kernels: Linear, Polynomial (degree=3), RBF 🌐  
4. **Ensemble Methods**  
   - **AdaBoost** (50 estimators) 📈  
   - **Random Forest** (100 estimators) 🌳  

### 🔍 Key Findings  
- **KNN**: Manhattan/Euclidean (K=3-8) achieved **100% test accuracy** 🏆  
- **Logistic Regression**: L2 regularization outperformed L1 (**100% accuracy**) 📉  
- **SVM**: RBF kernel achieved **100% accuracy** 🌐✨  
- **Ensembles**: Both AdaBoost/Random Forest scored **100%**, but RF showed better feature importance 🌳🔍  

---
## 📁 Files  
- 📄 **`ML_assignment_3.pdf`**: Assignment description.  
- 📊 **`Report.pdf`**: Detailed analysis (9 pages).  
- 🧪 **`Machine3.ipynb`**: Full code implementation.  
- 🌸 **`iris_dataset.csv`**: Dataset used.  

---
## 🚀 How to Use  
1. Clone the repository:  
   ```bash  
    git clone https://github.com/zainabja52/Machine-Learning-and-Data-Science
   cd Iris Species Classification using Machine Learning
   ```  
2. Open **`Machine3.ipynb`** in Jupyter Notebook/Google Colab.  
3. Run cells to reproduce results 🔄📊.  

---
## 📊 Results  
- **Top Performers**: SVM (RBF), Random Forest, and Logistic Regression (L2) achieved **perfect classification**.  
- **KNN**: Sensitive to distance metrics (Cosine underperformed).  
- **Ensembles**: Robust even on simple datasets, with Random Forest generalizing better.  

---
## 📜 License  
⚠️ For educational purposes only.  
