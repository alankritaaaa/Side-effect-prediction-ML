import pandas as pd
import streamlit as st

df = pd.read_csv("FINAL_DrugRiskDataset.csv")

st.set_page_config(page_title="Drug Safety Checker", layout="centered")

st.markdown("""
    <style>
        html, body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #ffffff;
            color: #222;
        }
        .main-title {
            font-size: 2.5rem;
            font-weight: 700;
            text-align: center;
            margin-bottom: 0.25rem;
        }
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 2rem;
            font-size: 1.1rem;
        }
        .card {
            background-color: #fff;
            padding: 1.25rem;
            border-radius: 1rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.06);
            margin-bottom: 2rem;
        }
        .risk-label {
            font-size: 1rem;
            font-weight: 600;
            color: #666;
            margin-bottom: 0.25rem;
        }
        .risk-score {
            font-size: 2rem;
            font-weight: bold;
            color: #D72638;
        }
        .sub-heading {
            font-size: 1.25rem;
            margin-top: 1rem;
            margin-bottom: 0.5rem;
            font-weight: 600;
        }
        .pill {
            display: inline-block;
            background-color: #f1f3f5;
            padding: 0.5rem 0.9rem;
            border-radius: 999px;
            margin: 0.25rem 0.5rem 0.25rem 0;
            font-size: 0.95rem;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>💊 Drug Safety Checker</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Understand the risk score of a drug and explore safer alternatives</div>", unsafe_allow_html=True)

drug_name = st.text_input("🔍 Enter the drug name")

if st.button("Check Drug Risk") and drug_name:
    row = df[df['name'].str.strip().str.lower() == drug_name.strip().lower()]

    if row.empty:
        st.error("❌ Drug not found in the database.")
    else:
        risk = row['FinalRiskScore'].values[0]
        st.markdown(f"""
            <div class='card'>
                <div class='risk-label'>Risk Score</div>
                <div class='risk-score'>{risk:.2f}</div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='sub-heading'>🧪 Substitute Medicines</div>", unsafe_allow_html=True)
        substitute_found = False
        subs_html = ""
        for i in range(5):
            col = f"substitute{i}"
            if col in row.columns:
                val = row.iloc[0][col]
                if pd.notna(val) and val.strip().lower() != "unknown":
                    subs_html += f"<span class='pill'>{val.strip()}</span>"
                    substitute_found = True
        if substitute_found:
            st.markdown(subs_html, unsafe_allow_html=True)
        else:
            st.info("No valid substitutes found.")