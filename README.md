💊 AI-Driven Drug Side Effect Prediction & Smart Substitution Recommender

This project presents a Clinical Decision Support System (CDSS) designed to predict adverse drug reactions (ADRs) and recommend safer therapeutic alternatives using machine learning. Built as part of my Master’s thesis at Pondicherry University, it aims to improve drug safety and reduce harmful side effects in clinical settings.

Key Features
- Predicts drug risk scores using an FDA-weighted side effect severity system.
- Recommends safer substitutes within the same therapeutic class.
- Streamlit web app for interactive use — drug input, risk output, and substitute recommendations.
- Explainable AI: Feature importance is derived using interpretable ML techniques.

Tech Stack
- Python, Scikit-learn, Pandas, NumPy
- Matplotlib & Seaborn for visualization
- Streamlit for deployment
- Random Forest Regressor (best performing model with R² ≈ 0.81)

Model Performance
- R² Score: 0.81
- RMSE: 3.2
- MAE: 2.4
- Feature Importance:  
  - SideEffectScore = 0.58  
  - Chemical Class = 0.18  
  - Action Class = 0.15

Dataset
- Sourced from Kaggle: Includes drug names, classes, side effects, and substitutes.
- Features: Action Class, Therapeutic Class, Habit Forming, Side Effect Severity.
- Weighted scores based on FDA classifications (e.g., heart attack = 10, rash = 4).

How It Works
1. Drug name is input via Streamlit UI.
2. Model outputs a risk score using learned pharmacological patterns.
3. The system retrieves and recommends lower-risk substitutes from the same category.

Streamlit App Preview
Not live-hosted yet. Run locally using:
```VSCode
streamlit run app.py
