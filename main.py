import os
from api.auth import get_access_token
from api.search import search_jobs

from dotenv import load_dotenv
load_dotenv()

def main():
    # 🔑 Vérification des variables d’environnement
    if not os.getenv("ADZUNA_APP_ID") or not os.getenv("ADZUNA_APP_KEY"):
        raise EnvironmentError(
            "Variables d’environnement ADZUNA_APP_ID et ADZUNA_APP_KEY manquantes"
        )

    print("🔐 Récupération du token France Travail...")
    token = get_access_token()
    print("✅ Token obtenu")

    # 🔍 Paramètres de test
    keywords = "analyste développeur python"
    location = "75"  # Paris
    contract = "CDI"
    limit = 10

    print(f"\n🔎 Recherche d’offres : '{keywords}'")
    offers = search_jobs(
        token=token,
        keywords=keywords,
        location=location,
        contract=contract,
        limit=limit
    )

    print(f"\n📊 {len(offers)} offres trouvées\n")

    # 🖨️ Affichage simple des résultats
    for i, offer in enumerate(offers, start=1):
        print(f"--- Offre {i} ---")
        print("Titre      :", offer.get("intitule"))
        print("Entreprise :", offer.get("entreprise", {}).get("nom"))
        print("Lieu       :", offer.get("lieuTravail", {}).get("libelle"))
        print("Contrat    :", offer.get("typeContrat"))
        print("URL        :", offer.get("origineOffre", {}).get("urlOrigine"))
        print()

if __name__ == "__main__":
    main()
