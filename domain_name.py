import requests

url = "https://api.godaddy.com/v1/domains/available"

headers = {
    "Authorization": "sso-key YOUR_API_KEY:YOUR_API_SECRET",
    "Content-Type": "application/json"
}

keywords = ["understand", "engage", "act"]
tlds = [".com", ".ai", ".net"]

for keyword in keywords:
    for tld in tlds:
        payload = {
            "domain": f"{keyword}{tld}"
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()
            if result["available]
