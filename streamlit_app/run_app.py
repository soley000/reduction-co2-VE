import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- CONFIGURATION ---
st.set_page_config(page_title="Conseiller CO₂ personnalisé", layout="centered")
st.title("💡 Conseiller CO₂ personnalisé – Thermique vs Véhicule Électrique")

# --- SECTION 1 : INPUT UTILISATEUR ---
st.header("1. Votre véhicule actuel")

with st.form(key="formulaire_utilisateur"):
    carburant = st.selectbox("Type de carburant", ["Essence", "Diesel", "Autre"])
    conso = st.number_input("Consommation moyenne (en L/100 km)", min_value=1.0, max_value=20.0, value=6.0)
    km_parcourus = st.number_input("Kilomètres parcourus par an", min_value=1000, max_value=100000, value=15000)
    annee_ve = st.selectbox("Année de passage au véhicule électrique", list(range(2024, 2036)))
    valider = st.form_submit_button("Valider les informations")

if valider:
    # --- CALCUL DES ÉMISSIONS CO2 ---
    if carburant == "Essence":
        FACTEUR_CONV = 2.31
    elif carburant == "Diesel":
        FACTEUR_CONV = 2.68
    else:
        FACTEUR_CONV = 2.50

    emission_thermique = conso * km_parcourus / 100 * FACTEUR_CONV / 1000
    CO2_VE = 49.33
    emission_ve = CO2_VE * km_parcourus / 1000
    gain_annuel = emission_thermique - emission_ve
    arbres = gain_annuel / 25

    # --- AFFICHAGE DES RÉSULTATS ---
    st.subheader("📊 Résultats individuels")
    st.write(f"🚘 Votre véhicule **{carburant.lower()}** émet environ **{emission_thermique:.0f} kg de CO₂/an**.")
    st.write(f"🔌 Un **véhicule électrique** équivalent émettrait environ **{emission_ve:.0f} kg de CO₂/an**.")
    st.success(f"💚 Gain : **{gain_annuel:.0f} kg de CO₂/an**, soit **{arbres:.0f} arbres plantés**.")

    # --- SECTION 2 : GRAPHIQUES PROJECTIONS ---
    try:
        df_forecast = pd.read_csv("forecast_prophet.csv")
        df_forecast = df_forecast.rename(columns={"yhat": "part_ve_predite"})

        nb_voitures = 38_000_000
        df_forecast = df_forecast[df_forecast["annee"] <= 2035]

        df_forecast["co2_collectif_thermique"] = emission_thermique * nb_voitures / 1_000_000
        df_forecast["co2_collectif_ve"] = emission_ve * nb_voitures / 1_000_000 * df_forecast["part_ve_predite"]
        df_forecast["co2_melange"] = (
            df_forecast["part_ve_predite"] * emission_ve +
            (1 - df_forecast["part_ve_predite"]) * emission_thermique
        ) * nb_voitures / 1_000_000
        df_forecast["gain_collectif"] = df_forecast["co2_collectif_thermique"] - df_forecast["co2_collectif_ve"]

        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=df_forecast["annee"], y=df_forecast["co2_collectif_thermique"],
                                  mode='lines+markers', name="Sans adoption VE (tout thermique)", line=dict(color='red')))
        fig1.add_trace(go.Scatter(x=df_forecast["annee"], y=df_forecast["co2_melange"],
                                  mode='lines+markers', name="Mix prévisionnel VE/thermique", line=dict(color='green')))
        fig1.update_layout(title="📉 Projection nationale des émissions de CO₂",
                           xaxis_title="Année", yaxis_title="Millions de kg de CO₂")
        st.plotly_chart(fig1, use_container_width=True)

        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=df_forecast["annee"], y=df_forecast["gain_collectif"],
                                  mode='lines+markers', name="CO₂ évité (France entière)",
                                  line=dict(color='blue')))
        fig2.update_layout(title="🌍 CO₂ évité si toute la France faisait comme vous",
                           xaxis_title="Année", yaxis_title="Millions de kg de CO₂ évité")
        st.plotly_chart(fig2, use_container_width=True)

    except FileNotFoundError:
        st.error("⚠️ Le fichier `forecast_prophet.csv` est manquant.")

# --- PIED DE PAGE ---
st.markdown("---")
st.caption("Application IA – Projet de Rosette-Michèle (M1 IA School)")
