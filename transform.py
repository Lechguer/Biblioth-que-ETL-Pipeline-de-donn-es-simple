"""
===========================================================
  ÉTAPE 2 — TRANSFORM
  Nettoyer, enrichir et fusionner les données
===========================================================
"""

import pandas as pd


def nettoyer_livres(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoie le DataFrame des livres."""

    print("\n🧹 Nettoyage des livres ...")
    nb_avant = df.shape[0]

    # 1. Supprimer les lignes avec un titre manquant
    df = df.dropna(subset=["titre"])
    print(f"   ✔ Lignes sans titre supprimées : {nb_avant - df.shape[0]}")

    # 2. Supprimer les doublons exacts
    nb_avant = df.shape[0]
    df = df.drop_duplicates()
    print(f"   ✔ Doublons supprimés : {nb_avant - df.shape[0]}")

    # 3. Remplir les notes manquantes par la moyenne
    moyenne = round(df["note"].mean(), 1)
    nb_manquants = df["note"].isnull().sum()
    df["note"] = df["note"].fillna(moyenne)
    print(f"   ✔ Notes manquantes ({nb_manquants}) remplacées par la moyenne : {moyenne}")

    # 4. Nettoyer les espaces dans les textes
    df["titre"]  = df["titre"].str.strip()
    df["auteur"] = df["auteur"].str.strip()
    df["genre"]  = df["genre"].str.strip()

    print(f"\n   ✅ Données propres : {df.shape[0]} livres")
    return df


def enrichir_livres(df_livres: pd.DataFrame, df_auteurs: pd.DataFrame) -> pd.DataFrame:
    """Fusionne les livres avec les auteurs et ajoute des colonnes calculées."""

    print("\n🔗 Fusion livres + auteurs ...")

    # 1. Fusionner les deux DataFrames sur le nom de l'auteur
    df = pd.merge(
        df_livres,
        df_auteurs,
        left_on="auteur",
        right_on="nom",
        how="left"          # on garde tous les livres, même sans auteur trouvé
    )
    df = df.drop(columns=["nom"])  # colonne redondante après le merge
    print(f"   ✔ Fusion terminée : {df.shape[0]} lignes")

    # 2. Calculer l'âge du livre (en années)
    df["age_livre"] = 2025 - df["annee"]

    # 3. Catégoriser la note
    def categoriser_note(note):
        if note >= 9.0:
            return "⭐ Excellent"
        elif note >= 8.0:
            return "👍 Bon"
        elif note >= 7.0:
            return "😐 Moyen"
        else:
            return "👎 Mauvais"

    df["categorie_note"] = df["note"].apply(categoriser_note)

    # 4. Statut de l'auteur
    df["auteur_vivant"] = df["deces"].isnull().map({True: "Vivant", False: "Décédé"})

    print("\n--- Résultat après transformation ---")
    print(df[["titre", "auteur", "annee", "note", "genre",
              "age_livre", "categorie_note", "auteur_vivant"]])

    return df
