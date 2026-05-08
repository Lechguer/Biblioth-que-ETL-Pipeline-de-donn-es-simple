"""
================================================
  PIPELINE ETL — BIBLIOTHÈQUE PERSONNELLE
  Point d'entrée principal : lance tout le pipeline
  
  Usage :
      python pipeline.py
================================================
"""

from src.extract   import lire_livres_csv, lire_auteurs_json
from src.transform import nettoyer_livres, enrichir_livres
from src.load      import sauvegarder_csv, afficher_resume


def main():

    print("=" * 50)
    print("   🚀 DÉMARRAGE DU PIPELINE ETL")
    print("=" * 50)

    # ---------------------------
    # ÉTAPE 1 — EXTRACT
    # ---------------------------
    print("\n📥 [ÉTAPE 1 / 3]  EXTRACT\n" + "-" * 30)
    df_livres  = lire_livres_csv("data/livres.csv")
    df_auteurs = lire_auteurs_json("data/auteurs.json")

    # ---------------------------
    # ÉTAPE 2 — TRANSFORM
    # ---------------------------
    print("\n⚙️  [ÉTAPE 2 / 3]  TRANSFORM\n" + "-" * 30)
    df_propre = nettoyer_livres(df_livres)
    df_final  = enrichir_livres(df_propre, df_auteurs)

    # ---------------------------
    # ÉTAPE 3 — LOAD
    # ---------------------------
    print("\n📤 [ÉTAPE 3 / 3]  LOAD\n" + "-" * 30)
    sauvegarder_csv(df_final, "output/rapport_final.csv")
    afficher_resume(df_final)

    print("\n✅ Pipeline terminé avec succès !\n")


if __name__ == "__main__":
    main()
