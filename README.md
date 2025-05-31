# Réduction de CO₂ par l’adoption des véhicules électriques (VE)

Ce projet vise à prédire la réduction des émissions de CO₂ induite par l'adoption croissante des véhicules électriques (VE) en France.  
Il s’appuie sur des jeux de données publics et l’utilisation de modèles d’intelligence artificielle pour simuler différents scénarios d’évolution du parc automobile.

---

## Objectifs

- Quantifier l’impact environnemental du remplacement progressif des véhicules thermiques par des véhicules électriques.
- Prédire la réduction potentielle de CO₂ en fonction de la croissance de l’adoption des VE.
- Utiliser des modèles IA de séries temporelles (LSTM, Prophet) pour simuler des scénarios futurs.
- Exploiter des données ouvertes (ADEME, Our World in Data, IEA...) pour une approche réaliste.

---

## Structure du projet

- \`data/\` : Données sources brutes (émissions, immatriculations, mix énergétique, etc.)
- \`scripts/\` : Scripts Python pour prétraitement, modélisation et visualisation
- \`notebooks/\` : Jupyter Notebooks pour exploration et modélisation
- \`results/\` : Graphiques, modèles IA entraînés et exports
- \`docs/\` : Documentation, sources et annexes

---

## 🔧 Environnement

Installer les dépendances nécessaires via :

\`\`\`bash
pip install -r requirements.txt
\`\`\`

---

## Approche IA

Les modèles ont été choisis pour leur capacité à capturer des tendances temporelles (Prophet), à représenter des dépendances complexes (LSTM), tout en restant accessibles et pédagogiques pour une montée en compétence progressive.

Nous utiliserons des modèles comme **Prophet** ou des réseaux de neurones **LSTM** pour :

- Prévoir l’évolution de la part de marché des VE
- Estimer les tonnes de CO₂ évitées selon différents scénarios d’adoption
- Simuler l’effet de plusieurs paramètres (intensité carbone, croissance annuelle, réglementation)

---

## Sources de données

- ADEME (émissions CO₂ des véhicules)
- Our World in Data (intensité carbone de l’électricité)
- IEA (données globales sur les VE)
- Data.gouv.fr (immatriculations, empreintes carbone comparées)
- Ministère de la Transition Écologique

---

## Auteur·e
Rosette-Michèle, étudiante en M1 IA-datasciences
**IA-school - Groupe-Gema**

