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
