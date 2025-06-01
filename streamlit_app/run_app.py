# app.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- CONFIGURATION ---
st.set_page_config(page_title="Mon Impact CO₂", layout="centered")
st.title("🚗 Mon Impact CO₂ – Comparaison entre véhicule thermique et VE")

# --- SECTION 1 : INPUT UTILISATEUR ---
st.header("1. Votre véhicule actuel")

carburant = st.selectbox("Type de carburant", ["Essence", "Diesel", "Autre"])
conso = st.number_input("Consommation moyenne (en L/100 km)", min_value=1.0, max_value=20.0, value=6.0)
km_parcourus = st.number_input("Kilomètres parcourus par an", min_value=1000, max_value=100000, value=15000)

# --- CALCUL DES ÉMISSIONS CO2 ---
FACTEUR_CONV = 2.31 if carburant == "Essence" else 2.68  # gCO2/L
depense_thermique = conso * km_parcourus / 100
emission_thermique = depense_thermique * FACTEUR_CONV / 1000  # en kg

CO2_VE = 49.33  # g/km (analyse préalable)
emission_ve = CO2_VE * km_parcourus / 1000  # en kg
gain = emission_thermique - emission_ve
arbres = gain / 25  # équivalent arbres plantés

# --- AFFICHAGE DES RÉSULTATS ---
st.subheader("📊 Comparaison avec un véhicule électrique")
st.write(f"🚘 Votre véhicule **{carburant.lower()}** actuel émet environ **{emission_thermique:.0f} kg de CO₂/an**.")
st.write(f"🔌 Un **véhicule électrique** équivalent émettrait environ **{emission_ve:.0f} kg de CO₂/an**.")
st.success(f"💚 Vous réduiriez vos émissions annuelles de **{gain:.0f} kg de CO₂**, soit l'équivalent de **{arbres:.0f} arbres plantés**.")

# --- SECTION 2 : PROJECTION NATIONALE ---
st.header("2. Projection nationale")

# Chargement des prévisions Prophet
try:
    df_forecast = pd.read_csv("data/forecast_prophet.csv")

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_forecast['annee'], 
        y=df_forecast['co2_evite_cumule_tonnes'],
        mode='lines+markers', 
        name='CO₂ évité (cumul)', 
        line=dict(color='green')
    ))
    fig.update_layout(
        title="Évolution du CO₂ évité en France (prévision Prophet)",
        xaxis_title="Année",
        yaxis_title="Tonnes de CO₂ évitées"
    )
    st.plotly_chart(fig, use_container_width=True)

except FileNotFoundError:
    st.error("Le fichier `forecast_prophet.csv` est introuvable. Merci de l'ajouter dans le dossier `data/`.")

# --- PIED DE PAGE ---
st.markdown("---")
st.caption("Application conçue dans le cadre d'un projet IA - Développement Durable (M1 IA School)")
