import os
import requests
from dotenv import load_dotenv

load_dotenv()

def main():
    if not os.getenv("ADZUNA_APP_ID") or not os.getenv("ADZUNA_APP_KEY"):
        raise EnvironmentError(
            "Variables d’environnement ADZUNA_APP_ID et ADZUNA_APP_KEY manquantes"
        )

    url = "https://api.adzuna.com/v1/api/jobs/fr/search/1"
    params = {
        "app_id": os.getenv("ADZUNA_APP_ID"),
        "app_key": os.getenv("ADZUNA_APP_KEY"),
        "what": "java",
        "results_per_page": 25
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    print(f"{len(data['results'])} offres trouvées\n")

    for job in data["results"]:
        print(job["title"], "|", job["company"]["display_name"])

if __name__ == "__main__":
    main()
