import streamlit as st
import pandas as pd
import joblib
import os

# --- Page Config ---
st.set_page_config(
    page_title="IPL Match Winner Predictor",
    page_icon="🏏",
    layout="centered"
)

# --- Header ---
st.title("🏏 IPL Match Winner Predictor")
st.markdown("### Predict which team will win an IPL match based on current form and head-to-head record")
st.markdown("---")
st.markdown("**Built by Shambhavi** | Machine Learning Project")
st.markdown("---")

# --- Load Model ---
model = joblib.load("ipl_winner_model.pkl")

# --- Team List ---
ipl_teams = sorted([
    'Mumbai Indians',
    'Chennai Super Kings',
    'Royal Challengers Bengaluru',
    'Kolkata Knight Riders',
    'Delhi Capitals',
    'Punjab Kings',
    'Rajasthan Royals',
    'Sunrisers Hyderabad',
    'Gujarat Titans',
    'Lucknow Super Giants'
])

# --- Team Selection ---
st.subheader("Select Teams")
col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox("Team 1", ipl_teams, index=0)

with col2:
    team2 = st.selectbox("Team 2", ipl_teams, index=1)

st.markdown("---")

# --- Recent Form ---
st.subheader("Recent Form (Last 5 Matches)")
col3, col4 = st.columns(2)

with col3:
    team1_wins = st.slider(f"{team1} — wins in last 5", 0, 5, 3)
    team1_winrate = team1_wins / 5

with col4:
    team2_wins = st.slider(f"{team2} — wins in last 5", 0, 5, 3)
    team2_winrate = team2_wins / 5

st.markdown("---")

# --- Head to Head ---
st.subheader("Head to Head Record")
col5, col6 = st.columns(2)

with col5:
    h2h_team1_wins = st.number_input(f"{team1} wins vs {team2} (all time)", min_value=0, value=10)

with col6:
    h2h_total = st.number_input(f"Total matches between them", min_value=1, value=20)

h2h_winrate = h2h_team1_wins / h2h_total if h2h_total > 0 else 0.5

st.markdown("---")

# --- Toss ---
st.subheader("Toss Details")
col7, col8 = st.columns(2)

with col7:
    toss_winner = st.selectbox("Toss Winner", [team1, team2])

with col8:
    toss_decision = st.radio("Toss Decision", ["Bat", "Field"])

team1_won_toss = 1 if toss_winner == team1 else 0
toss_dec_enc = 1 if toss_decision == "Bat" else 0

st.markdown("---")

# --- Predict Button ---
if st.button("🔮 Predict Winner", use_container_width=True):

    if team1 == team2:
        st.error("Please select two different teams!")
    else:
        form_diff = team1_winrate - team2_winrate
        h2h_adv = h2h_winrate - 0.5

        input_data = pd.DataFrame([{
            'form_difference': form_diff,
            'h2h_advantage': h2h_adv,
            'team1_won_toss': team1_won_toss,
            'toss_decision_encoded': toss_dec_enc
        }])

        prediction = model.predict(input_data)[0]
        proba = model.predict_proba(input_data)[0]
        team1_prob = round(proba[1] * 100, 1)
        team2_prob = round(proba[0] * 100, 1)
        winner = team1 if prediction == 1 else team2

        # --- Result ---
        st.markdown("## 🏆 Prediction Result")
        st.success(f"**Predicted Winner: {winner}**")

        st.markdown("### Win Probabilities")
        col9, col10 = st.columns(2)

        with col9:
            st.metric(label=team1, value=f"{team1_prob}%")

        with col10:
            st.metric(label=team2, value=f"{team2_prob}%")

        st.progress(int(team1_prob))
        st.caption(f"{team1} ← probability → {team2}")

# --- Footer ---
st.markdown("---")
st.caption("Built by Shambhavi | IPL Match Winner Predictor ")