print("started instagram scan")

import requests

ig_user_id = "17841401326238030"
app_id = "863397329492684"
app_secret = "929b175d28576119e7bc59c840e166f6"
user_access_token = "EAAMRQVsf2swBSZAZCJZAkqdZCIRo6oCUX48xITLjhRyiEkoZA2u1vL3Ixa38e7qMf58uiqTxY3ZBeIkuLAG57yUuVoMLAwhPcjdsHW05Yq3RT4duZCSQcsq7ez7toOYcSN0OiCXBuvVaLqSllv48WOWRuGcXUmpjngZAJyYLaD4AodQ8FeiKMaLZBvdRSzM9vfhNEH5ck4eaMAvd0Mxw8"


url = "https://graph.facebook.com/v21.0/oauth/access_token"
params = {
    "grant_type": "fb_exchange_token",
    "client_id": app_id,
    "client_secret": app_secret,
    "fb_exchange_token": user_access_token
}

response = requests.get(url, params=params)
long_access_token = response.json()["access_token"]

#iniciando pesquisa de influenciadores
username = "neymarjr"

url = f"https://graph.facebook.com/v21.0/{ig_user_id}"

params = {
    "fields": f"business_discovery.username({username}){{followers_count,media_count}}",
    "access_token": long_access_token
}

response = requests.get(url, params=params)

print("Resposta Instagram:")
print(response.text)