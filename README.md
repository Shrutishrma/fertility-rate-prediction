# 🌍 Fertility Rate Prediction Web App

This is a Machine Learning web application built with the **Django** framework that predicts the fertility rate of a region based on various demographic and geographic characteristics.

---

## 🚀 Project Overview

The application provides a clean web interface where users can input specific demographic metrics. These inputs are processed by a pre-trained **Machine Learning model** (`prediction.pkl`) to generate an estimated Fertility Rate.

### **Key Features:**
* **Django Integration**: Utilizes a robust backend to handle data routing and model execution.
* **Automated Predictions**: Seamlessly loads a serialized model via `pickle` to provide real-time results.
* **Data Validation**: Implements error handling in the `views.py` to ensure all numeric inputs are valid before processing.
* **Interactive Results**: Displays the predicted rate on a dedicated results page for better user experience.

---

## 🛠️ Tech Stack

* **Framework**: Python, Django
* **Data Handling**: Pandas, NumPy
* **Machine Learning**: Scikit-Learn (via Pickle)
* **Frontend**: HTML5, CSS3

---

## 📂 Repository Structure

Based on the `papp` application configuration:

```text
fertility-rate-prediction/
│
├── manage.py                         # Django management script
├── requirements.txt                  # Python dependencies
├── README.md                         # Project documentation
│
├── core_project/                     # Main project configuration folder
│   ├── settings.py                   
│   ├── urls.py                       
│   └── ...
│
└── papp/                             # Main application folder
    ├── views.py                      # ML prediction logic and rendering
    ├── admin.py                      # Django admin boilerplate
    ├── apps.py                       # App configuration (PappConfig)
    ├── models.py                     # Database models
    │
    ├── models/                       
    │   └── prediction.pkl            # Serialized ML model
    │
    └── templates/                    
        ├── predict_fertility_rate.html  # Input form template
        └── prediction_result.html       # Result display template
```

---

## 📊 Model Input Features

To obtain a prediction, the model requires the following demographic data:

1.  **Population (2023)**: The total population count.
2.  **Yearly Change**: Percentage of annual population change.
3.  **Net Change**: The absolute change in population size.
4.  **Density (P/Km²)**: Population per square kilometer.
5.  **Land Area (Km²)**: Total geographic area.
6.  **Migrants (net)**: Total number of incoming/outgoing migrants.
7.  **Median Age**: The average age of the population.
8.  **Urban Pop (%)**: Percentage of the population living in urban centers.

---
4.  Paste the content above into the editor.
5.  Click **Commit changes**.
