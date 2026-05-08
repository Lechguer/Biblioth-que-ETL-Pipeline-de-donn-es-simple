"""
==============================================
  ÉTAPE 1 — EXTRACT
  Lire les données brutes depuis CSV et JSON
==============================================
"""

import pandas as pd
import json


def lire_livres_csv(chemin: str) -> pd.DataFrame:
    """Lit le fichier CSV des livres et affiche un aperçu."""

    print("📂 Lecture de livres.csv ...")
    df = pd.read_csv(chemin)

    print(f"   ✔ {df.shape[0]} lignes, {df.shape[1]} colonnes chargées")
    print("\n--- Aperçu des données brutes ---")
    print(df)

    print("\n--- Informations sur les colonnes ---")
    print(df.dtypes)

    print("\n--- Valeurs manquantes par colonne ---")
    print(df.isnull().sum())

    return df


def lire_auteurs_json(chemin: str) -> pd.DataFrame:
    """Lit le fichier JSON des auteurs et le convertit en DataFrame."""

    print("\n📂 Lecture de auteurs.json ...")
    with open(chemin, "r", encoding="utf-8") as f:
        auteurs = json.load(f)

    df = pd.DataFrame(auteurs)

    print(f"   ✔ {df.shape[0]} auteurs chargés")
    print("\n--- Aperçu des auteurs ---")
    print(df)

    return df
