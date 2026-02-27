# 🎓 EduAnalytica – Student Dropout Risk Prediction System

EduAnalytica is a machine learning-powered web application that predicts student dropout risk using academic performance, engagement, attendance, and financial indicators.

The system is designed as an **early-warning analytical tool** to help identify at-risk students based on probabilistic modeling.

---

## 🎯 Business Use Case

This system can help:
- Universities detect early dropout risk
- Academic advisors intervene earlier
- Improve student retention rates

## 🔐 Disclaimer

* This system is trained using a Portuguese higher education dataset.

* The prediction output is a probabilistic estimate intended for:

* Research purposes

* Early-warning analysis

* Academic exploration

* It should not be used as a final decision-making system.

---

## ⬇️Installation

Python Version: 3.10.0

Setup Instructions:

1. Clone the repository

2. Create virtual environment: ``` python -m venv venv ```

3. Activate virtual environment:``` venv\Scripts\activate ```

4. Install dependencies:``` pip install -r requirements.txt ```

5. Run the application:``` python app.py ```
## 🚀 Features

- 📊 Real-time dropout risk prediction
- 🧠 Machine Learning model (XGBoost)
- 🎯 5-feature optimized model for web deployment
- 🔐 Terms & Disclaimer popup system
- 📈 Risk visualization with dynamic circular progress UI
- ⚠ Intelligent validation & warning system
- 💡 Explanation bullets for risk factors
- 🌐 Flask backend API
- 🎨 Modern TailwindCSS UI

---

## 🧠 Machine Learning Models Tested

The following models were evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- LightGBM

After evaluation, **XGBoost** was selected for deployment due to superior recall and ROC-AUC performance.

---

## 📊 Final Web Model (5 Features)

The deployed model uses engineered features:

-------------------------------------------------------------------------
| Feature          |         Description                                |
|------------------|----------------------------------------------------|
| `attendance`     | Attendance percentage                              |
| `submission_gap` | Assignment delay proxy                             |
| `avg_score`      | Average academic score (0–20 scale)                |
| `fees_status`    | Tuition status (1 = Up to date, 0 = Pending)       |
| `engagement`     | Encoded engagement level (High=2, Medium=1, Low=0) |

---

## 🔧 Feature Engineering Process

From the original Portuguese student dataset:

```python
# Attendance proxy
df["attendance_pct"] = (
    (df["Curricular units 1st sem (enrolled)"] +
     df["Curricular units 2nd sem (enrolled)"]) /
    (df["Curricular units 1st sem (enrolled)"].max() +
     df["Curricular units 2nd sem (enrolled)"].max())
) * 100

# Average score
df["avg_score"] = (
    df["Curricular units 1st sem (grade)"] +
    df["Curricular units 2nd sem (grade)"]
) / 2

# Engagement index
df["engagement_index"] = (
    (df["Curricular units 1st sem (approved)"] +
     df["Curricular units 2nd sem (approved)"]) /
    (df["Curricular units 1st sem (enrolled)"] +
     df["Curricular units 2nd sem (enrolled)"] + 1)
)

# Submission gap proxy
df["submission_gap"] = (
    df["Curricular units 1st sem (without evaluations)"] +
    df["Curricular units 2nd sem (without evaluations)"]
)
# Fees status
df["fees_status"] = df["Tuition fees up to date"]

```

## 🖥️ Tech Stack

### Backend

* Flask

* Scikit-learn

* XGBoost

* Pandas

* NumPy

### Frontend

* HTML

* TailwindCSS

* JavaScript (Vanilla)

## 📁 Project Structure

```
EduAnalytica/
│
├── model/
│   └── xgboost_web_model.pkl
│
├── templates/
│   ├── index.html
│   └── about.html
├── app.py
├── README.md
└── requirements.txt
```
## 📐System Architecture Diagram
```
User Input → Frontend (HTML/JS) → Flask API → XGBoost Model → JSON Response → UI Update

