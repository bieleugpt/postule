
'''

import requests
import os

TOKEN_URL = "https://entreprise.francetravail.fr/connexion/oauth2/access_token"

def get_access_token():
    payload = {
        "grant_type": "client_credentials",
        "client_id": os.getenv("FT_CLIENT_ID"),
        "client_secret": os.getenv("FT_CLIENT_SECRET"),
        "scope": "api_offresdemploiv2 o2dsoffre"
    }

    response = requests.post(TOKEN_URL, data=payload)
    response.raise_for_status()
    return response.json()["access_token"]

'''










import os
import requests

TOKEN_URL = "https://entreprise.francetravail.fr/connexion/oauth2/access_token"

def get_access_token():
    client_id = os.getenv("FT_CLIENT_ID")
    client_secret = os.getenv("FT_CLIENT_SECRET")

    if not client_id or not client_secret:
        raise EnvironmentError("FT_CLIENT_ID ou FT_CLIENT_SECRET manquant")

    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "api_offresdemploiv2"
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(TOKEN_URL, data=data, headers=headers)

    if response.status_code != 200:
        print("❌ Erreur OAuth France Travail")
        print("Status :", response.status_code)
        print("Body   :", response.text)
        response.raise_for_status()

    return response.json()["access_token"]
