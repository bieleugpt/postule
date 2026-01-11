import os
from dotenv import load_dotenv

from api.auth import get_access_token
from api.search import search_jobs

load_dotenv()

def main():
    # 🔑 Vérification variables France Travail
    if not os.getenv("FT_CLIENT_ID") or not os.getenv("FT_CLIENT_SECRET"):
        raise EnvironmentError(
            "Variables d’environnement FT_CLIENT_ID et FT_CLIENT_SECRET manquantes"
        )

    print("🔐 Récupération du token France Travail...")
    token = get_access_token()
    print("✅ Token obtenu")

    keywords = "analyste développeur python"
    location = "75"
    contract = "CDI"
    limit = 10

    print(f"\n🔎 Recherche d’offres France Travail : '{keywords}'")
    offers = search_jobs(
        token=token,
        keywords=keywords,
        location=location,
        contract=contract,
        limit=limit
    )

    print(f"\n📊 {len(offers)} offres trouvées\n")

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
