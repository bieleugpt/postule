import requests

API_URL = "https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search"

def search_jobs(token, keywords, location=None, contract=None, limit=20):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    params = {
        "motsCles": keywords,
        "range": f"0-{limit}"
    }

    if location:
        params["codeDepartement"] = location
    if contract:
        params["typeContrat"] = contract

    response = requests.get(API_URL, headers=headers, params=params)
    response.raise_for_status()
    return response.json().get("resultats", [])
