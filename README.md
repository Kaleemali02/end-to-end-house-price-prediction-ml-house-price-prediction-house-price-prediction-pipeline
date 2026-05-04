# 🏠 House Price Prediction App

## 📌 Project Overview

This project predicts house prices using Machine Learning.
It includes complete data preprocessing, visualization, model training, and deployment using Streamlit.

---

## 🚀 Features

* 📊 Data visualization and EDA (histograms, boxplots, correlation heatmap)
* 🔄 End-to-end pipeline (preprocessing + model)
* 🤖 Multiple model comparison
* ⚙️ Hyperparameter tuning using GridSearchCV
* 🌐 Interactive web app using Streamlit

---

## 🧠 Machine Learning Workflow

### 1️⃣ Data Analysis & Visualization

* Distribution plots (histogram, KDE)
* Boxplots for outlier detection
* Correlation heatmap
* Feature-target relationship analysis

### 2️⃣ Data Preprocessing (Pipeline)

* Handling missing values (SimpleImputer)
* Scaling numerical features (StandardScaler)
* Encoding categorical variables (OneHotEncoder)
* Combined using ColumnTransformer & Pipeline

### 3️⃣ Model Training

* Linear Regression
* Ridge & Lasso
* Random Forest
* HistGradientBoosting
* XGBoost & LightGBM

### 4️⃣ Model Evaluation

* Cross-validation (KFold)
* Metrics: RMSE, MAE, R²
* Residual analysis

### 5️⃣ Hyperparameter Tuning

* GridSearchCV for optimal parameters
* Selected best model automatically

### 6️⃣ Deployment

* Saved model using joblib
* Built web app using Streamlit

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Matplotlib, Seaborn (Visualization)
* Scikit-learn (Pipeline & Models)
* LightGBM / XGBoost
* Streamlit (Deployment)

---

## ▶️ How to Run Locally

### 1. Clone repository

git clone https://github.com/your-username/house-price-prediction.git

### 2. Navigate to folder

cd house-price-prediction

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run app

streamlit run app.py

---

## 📊 Example Output

* Input: Income = 4.5, Rooms = 1500
* Output: Predicted Price ≈ $250,000+

---

## 📈 Key Highlights

* Used **Pipeline** to ensure consistent preprocessing
* Applied **cross-validation** for reliable evaluation
* Compared multiple models to select best performer
* Built **interactive UI** using Streamlit

---

## 👨‍💻 Author

Kaleem Ali
