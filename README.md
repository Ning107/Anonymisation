# Projet-anonymisation
Ce programme a pour but d'anonymiser des données personelles (nom, adresse, etc). Il a été conçu à partir d'annonces immobilières postées sur le site Leboncoin.

## Scripts
**scraper.py** permet d'extraire le résumé ainsi que la description de chaque annonce.<br>
**anonymisation.py** contient l'algorithme qui permet l'anonymisation des informations à l'aide des outils suivants de SpaCy :
* Rule-based matching
  * numéro de téléphone
  * adresse mail
  * adresse postale
* Reconnaissance d'entités nommées (NER)
  * ville, région
  * nom, prénom
  * nom d'entreprises

## Données
* **Corpus** : contient les annonces extraites
* **Corpus_anony** : contient les annonces anonymisées automatiquement
* **Corpus_manuel** : contient une dizaine d'annonces anonymisées manuellement
