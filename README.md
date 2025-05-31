# reduction-co2-VE
Prédiction de la réduction des émissions de CO₂ grâce à l’adoption des véhicules électriques

---

## ��� Approche IA

Ce projet repose sur une approche progressive, combinant des modèles simples et puissants avec des techniques plus avancées, afin de modéliser et prédire l’impact de l’adoption des véhicules électriques sur la réduction des émissions de CO₂.

### ��� Prophet (Meta/Facebook)  
> Modèle principal utilisé

- **Pourquoi ce choix ?**  
  Prophet est un modèle de séries temporelles conçu pour être à la fois puissant et facile à utiliser. Il permet de prédire l’évolution d’indicateurs (comme la part des véhicules électriques ou les tonnes de CO₂ évitées) en tenant compte des tendances et de la saisonnalité.
- **Avantages :** rapide à mettre en œuvre, interprétable, parfait pour les données chronologiques (année par année).

### ��� Régression linéaire ou arbres de décision (Random Forest)
> Modèles explicatifs alternatifs

- **Pourquoi ?**  
  Pour expliquer quelles variables influencent le plus la réduction de CO₂ (part des VE, intensité carbone, subventions...).
- **Avantages :** faciles à comprendre, utiles pour la communication des résultats.

### ��� LSTM (Long Short-Term Memory)
> Modèle challenge (bonus avancé)

- **Pourquoi ?**  
  Pour aller plus loin avec un modèle de deep learning, capable d’apprendre des dynamiques plus complexes dans les données temporelles.
- **Avantages :** très performant sur des séries longues, bonne introduction au deep learning.

---

## ��� Objectif pédagogique

Ce projet a aussi pour ambition de me faire progresser dans l'utilisation de modèles d'intelligence artificielle actuels.  
Je veux apprendre en appliquant des outils concrets, accessibles à mon niveau, tout en me challengeant avec des approches plus avancées comme LSTM.

## Approche IA

Ce projet repose sur une approche progressive, combinant des modèles accessibles et performants pour prédire l’impact de l’adoption des véhicules électriques sur la réduction des émissions de CO2.

1. Prophet (développé par Meta/Facebook)
   - Modèle de séries temporelles principal du projet.
   - Simple à utiliser, il permet de prédire l’évolution d’indicateurs comme la part des véhicules électriques ou les émissions de CO2 évitées.
   - Avantages : rapide à mettre en œuvre, interprétable, adapté aux données chronologiques (année par année).

2. Régression linéaire et Random Forest
   - Modèles alternatifs pour expliquer les relations entre variables (part de marché des VE, intensité carbone, subventions, etc.).
   - Avantages : faciles à comprendre, utiles pour identifier les facteurs influents.

3. LSTM (Long Short-Term Memory)
   - Modèle avancé de deep learning pour les séries temporelles.
   - Il sera utilisé comme un bonus pour aller plus loin et apprendre à construire un modèle p




















cat >> README.md <<'EOF'

## Approche IA

Ce projet repose sur une approche progressive, combinant des modèles accessibles et performants pour prédire l’impact de l’adoption des véhicules électriques sur la réduction des émissions de CO2.

1. Prophet (développé par Meta/Facebook)
   - Modèle de séries temporelles principal du projet.
   - Simple à utiliser, il permet de prédire l’évolution d’indicateurs comme la part des véhicules électriques ou les émissions de CO2 évitées.
   - Avantages : rapide à mettre en œuvre, interprétable, adapté aux données chronologiques (année par année).

2. Régression linéaire et Random Forest
   - Modèles alternatifs pour expliquer les relations entre variables (part de marché des VE, intensité carbone, subventions, etc.).
   - Avantages : faciles à comprendre, utiles pour identifier les facteurs influents.

3. LSTM (Long Short-Term Memory)
   - Modèle avancé de deep learning pour les séries temporelles.
   - Il sera utilisé comme un bonus pour aller plus loin et apprendre à construire un modèle plus complexe.
   - Avantages : performant sur des données temporelles avec dépendances longues, bonne initiation au deep learning.

Objectif pédagogique : utiliser des modèles d’intelligence artificielle modernes, compréhensibles à mon niveau d’étudiante, tout en me challengeant progressivement avec des outils plus puissants.
