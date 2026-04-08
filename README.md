# 🌍 Global Fertility Rate: From Web Scraping to Deployment

This repository features an end-to-end Machine Learning project that predicts a country's fertility rate based on demographic metrics. It includes the complete data science lifecycle: automated web scraping, exploratory data analysis, unsupervised clustering, and a functional **Django** web application for real-time predictions.

---

## 🚀 Project Components

### 1. 🧪 Research & Model Training (`.ipynb`)
The core engine of this project is the **`country_demographics_clustering.ipynb`** notebook. 
* **Data Collection:** Uses `Selenium` to scrape live demographic data from Worldometer.
* **Unsupervised Learning:** Implements **K-Means Clustering** and **PCA** to identify natural groupings among 234 countries based on socioeconomic factors.
* **Supervised Learning:** Trains a classification model (saved as `prediction.pkl`) to predict demographic categories with high precision.

### 2. 💻 Web Application (Django)
A production-ready web interface that allows users to interact with the trained model.
* **Backend:** Django handles the routing and integration of the serialized model.
* **Real-time Prediction:** Users input current demographic stats, and the app instantly returns the predicted fertility category.
* **Validation:** Built-in Python logic ensures all inputs are numeric and complete before processing.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Web Framework:** Django
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Automation:** Selenium WebDriver
* **Serialization:** Pickle
* **Frontend:** HTML5, CSS3

---

## 📂 Repository Structure

```text
fertility-rate-prediction/
│
├── country_demographics_clustering.ipynb  # Core ML research & model training
├── manage.py                             # Django management script
├── requirements.txt                      # Project dependencies
│
├── papp/                                 # Django Application Folder
│   ├── views.py                          # Prediction logic & ML integration
│   ├── models/
│   │   └── prediction.pkl                # The trained ML model
│   ├── templates/                        # HTML User Interfaces
│   │   ├── predict_fertility_rate.html
│   │   └── prediction_result.html
│   └── ...                               # Django boilerplate (admin, apps, etc.)
│
└── core_project/                         # Project Configuration
    ├── settings.py
    └── urls.py
```

---

## 📊 Model Input Features

The model analyzes the following features to generate a prediction:
* **Population (2023)**
* **Yearly & Net Change**
* **Density (P/Km²)** & **Land Area**
* **Net Migrants**
* **Median Age**
* **Urban Population (%)**

---
