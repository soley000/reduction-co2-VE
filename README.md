```
# 🌱 Réduction de CO₂ par l’adoption des véhicules électriques (VE) – Application IA personnalisée

Ce projet a pour but de **quantifier et prédire la réduction des émissions de CO₂** générée par l’adoption progressive des véhicules électriques (VE) en France.  
Il s’appuie sur des **données publiques** et l’intégration d’un **modèle d’intelligence artificielle Prophet** afin de personnaliser les résultats selon les habitudes de l’utilisateur.

> 📌 Projet réalisé dans le cadre du Master 1 IA - Data Science (IA School - Groupe GEMA), par Rosette-Michèle.

---

## 🎯 Objectifs pédagogiques et techniques

- Proposer une **application interactive Streamlit** intégrant une logique métier environnementale.
- **Personnaliser** les estimations CO₂ en fonction du type de véhicule, de la consommation, et du kilométrage annuel de l’utilisateur.
- **Projeter les émissions futures** à l’échelle nationale grâce à **l’IA (Prophet)**.
- Simuler les **gains individuels et collectifs** en CO₂ si tous les conducteurs adoptaient le VE.

---

## 🧠 Intelligence Artificielle utilisée

Le projet intègre **le modèle Prophet** (Meta/Facebook), utilisé ici pour :

- Prédire la **part de marché future des VE en France** jusqu’en 2035.
- **Personnaliser les projections d’émissions** en fonction du profil utilisateur.
- Générer des **graphes interactifs** montrant l’évolution des émissions selon différents scénarios.

---

## 🖥️ Fonctionnalités de l’application

L’utilisateur renseigne :
- Le **type de carburant** utilisé actuellement.
- Sa **consommation moyenne** (L/100 km).
- Le **nombre de kilomètres parcourus par an**.
- L’**année de passage** au véhicule électrique.

L’application calcule :
- Les **émissions annuelles actuelles** en CO₂.
- Les émissions estimées avec un **véhicule électrique**.
- Le **gain total** en kg de CO₂/an.
- L’**équivalent en arbres plantés 🌳**.
- Deux **graphiques dynamiques** :
  - Émissions nationales projetées : thermique seul vs mix prédit VE/thermique.
  - CO₂ évité si toute la France roulait comme vous.

---

## 📁 Structure du projet

```

├── data/                   # Données sources ouvertes
├── notebooks/              # Exploration des dpnnées & Modélisations 
├── streamlit\_app/          # Application principale
│   └── run\_app.py          # Code principal de l'application
├── forecast\_prophet.csv    # Fichier issu du modèle Prophet
├── requirements.txt        # Dépendances Python
└── README.md

````
---

## 📦 Installation

1. Installe les dépendances :

```bash
pip install -r requirements.txt
````

2. Lance l’application Streamlit :

```bash
streamlit run streamlit_app/run_app.py
```

---

## 🔍 Sources de données utilisées

* [ADEME](https://www.ademe.fr) – Émissions CO₂ des véhicules
* [Our World in Data](https://ourworldindata.org) – Intensité carbone de l’électricité
* [IEA](https://www.iea.org) – Données globales sur les VE
* [data.gouv.fr](https://data.gouv.fr) – Immatriculations, comparaisons thermiques/VE
* [Ministère de la Transition Écologique](https://www.ecologie.gouv.fr)

---

## 🧑🏾‍💻 Auteure

**Rosette-Michèle**
Master 1 Intelligence Artificielle & Management – IA School (Groupe GEMA)
Projet IA 2025 – Application pratique d’IA appliquée à la transition écologique

---

## 🚀 Déploiement (facultatif)

L’application peut être rendue accessible :

* En **local** via Streamlit comme démontré ci-dessus.
* Ou déployée sur **Streamlit Cloud** ([https://streamlit.io/cloud](https://streamlit.io/cloud)) avec un simple `git push`.

---

## ✨ Conclusion

Ce projet démontre **comment l’IA peut rendre compréhensible et mesurable l’impact écologique individuel**, et comment un simple changement de véhicule pourrait réduire significativement les émissions de CO₂ en France.

```
