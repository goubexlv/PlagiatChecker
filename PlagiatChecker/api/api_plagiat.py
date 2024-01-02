import requests

url = "https://plagiarism-checker-and-auto-citation-generator-multi-lingual.p.rapidapi.com/plagiarism"
headers = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": "0fcccf228bmshab8f84877ac8a36p14fb9ejsn5befbc823f88",
    "X-RapidAPI-Host": "plagiarism-checker-and-auto-citation-generator-multi-lingual.p.rapidapi.com"
}

text = "However, please note that availability of hazard map may vary depending on the location Municipal, Provincial or Regional). If there is no map showing in the municipal level, try selecting only up to provincial or regional level. If there is no hazard map available in your selected province, it\'s either there is no hazard specific to the area or mapping is still ongoing. PHIVOLCS takes the necessary steps to continuously improve the accuracy of hazards information reflected on each map generated. These maps may be revised as new information becomes available."

data = {
    "text": text,
    "language": "en",
    "includeCitations": False,
    "scrapeSources": False
}

try:
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()  # Lève une exception pour les codes d'erreur HTTP
    result = response.json()
    print(result)
except requests.exceptions.RequestException as e:
    print(e)
