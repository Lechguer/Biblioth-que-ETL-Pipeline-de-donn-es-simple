"""
=============================================
  ÉTAPE 3 — LOAD
  Sauvegarder les données transformées
=============================================
"""

import pandas as pd
import os


def sauvegarder_csv(df: pd.DataFrame, chemin: str) -> None:
    """Exporte le DataFrame final en fichier CSV."""

    print(f"\n💾 Export vers {chemin} ...")

    # Créer le dossier output s'il n'existe pas
    os.makedirs(os.path.dirname(chemin), exist_ok=True)

    df.to_csv(chemin, index=False, encoding="utf-8-sig")  # utf-8-sig pour Excel

    print(f"   ✅ Fichier sauvegardé avec succès ! ({df.shape[0]} lignes)")


def afficher_resume(df: pd.DataFrame) -> None:
    """Affiche un résumé final des données chargées."""

    print("\n" + "=" * 50)
    print("         📊 RÉSUMÉ FINAL DU PIPELINE")
    print("=" * 50)

    print(f"\n📚 Nombre total de livres     : {df.shape[0]}")
    print(f"✍️  Nombre d'auteurs uniques   : {df['auteur'].nunique()}")
    print(f"🎭 Genres présents            : {', '.join(df['genre'].unique())}")
    print(f"⭐ Note moyenne               : {df['note'].mean():.2f} / 10")
    print(f"📅 Livre le plus ancien       : {df.loc[df['annee'].idxmin(), 'titre']} ({df['annee'].min()})")
    print(f"📅 Livre le plus récent       : {df.loc[df['annee'].idxmax(), 'titre']} ({df['annee'].max()})")

    print("\n--- Répartition par catégorie de note ---")
    print(df["categorie_note"].value_counts().to_string())

    print("\n--- Meilleure note par genre ---")
    print(df.groupby("genre")["note"].max().sort_values(ascending=False).to_string())
