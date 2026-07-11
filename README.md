# IPL Match Winner Predictor

A Machine Learning web app that predicts the winner of an IPL match
based on recent team form and historical head-to-head records.

## 🔗 Live Demo
[Click here to try the app]([YOUR_STREAMLIT_LINK_HERE](https://ipl-match-winner.streamlit.app/))

## 👩‍💻 Built by
**Shambhavi** — Machine Learning Project

## 📌 Problem Statement
Can we predict which IPL team will win a match using data?
This project uses 16 years of IPL match data (2008-2024)
to train a Machine Learning model that predicts match outcomes.

## 📊 Dataset
- Source: Kaggle — IPL Complete Dataset 2008-2024
- Total matches: 1090 matches across 16 seasons

## ⚙️ How It Works
1. Select two IPL teams
2. Enter their recent form (wins in last 5 matches)
3. Enter head-to-head record
4. Enter toss details
5. Get instant winner prediction with win probability!

## 🤖 ML Models Used
| Model | Accuracy |
|---|---|
| Logistic Regression | 51.38% |
| Random Forest ⭐ Best | 55.50% |
| Gradient Boosting | 51.38% |

## 🔍 Key Findings
- Head-to-head record is the strongest predictor of match outcome
- Recent form is the second most important factor
- Toss has minimal impact on the final result
- Cricket's unpredictability means even top models stay around 55-60%

## 🛠️ Technologies Used
- Python
- Pandas, Numpy
- Matplotlib, Seaborn
- Scikit-learn
- Streamlit
- Jupyter Notebook

## 🚀 Run Locally
1. Clone this repository
2. Install requirements:
   pip install pandas numpy matplotlib seaborn scikit-learn joblib streamlit
3. Run the app:
   streamlit run app.py

## 📁 Project Structure
IPL-Match-Winner-Prediction/
├── app.py                          ← Streamlit web app
├── IPL_MatchWinnerPredictor.ipynb  ← ML notebook
├── ipl_winner_model.pkl            ← trained model
├── matches.csv                     ← dataset
└── README.md                       ← you are here
