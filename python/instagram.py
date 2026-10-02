print("started instagram scan")
from flask import request
import requests
import json
#informacoes do aplicativo do instagram
ig_user_id = '17841401326238030' #id do
app_id  = '863397329492684'#id do app
app_secret = '929b175d28576119e7bc59c840e166f6'#app secret do app
#token do usuario achado na ferramenta do meta
user_access_token = 'EAAMRQVsf2swBSSVdDpAZAeGnUOkpT3l5H4UZCXT5Qn7vYdGklj90vc0Mcr8ZCVjJcK1JtcL29vKD0AFgnBnK569GlA75v8FSVxcvETFdxZBRLjmbGJn2pbv0K18zOxjTq1gxvpfoDnGgqOvoEw9PELLGAZBQu3vAIZCa9fS1TA4MaPytJX0CTd1fsmgJIcBtL3AjIYlx39sGSKQTEWhwZDZD'

#https://graph.facebook.com/v17.0/oauth/access_token?grant_type=fb_exchange_token&client_id={app_id}&client_secret={app_secret}&fb_exchange_token={user_access_token}
#url pra buscar token de acesso longo
url = f"https://graph.facebook.com/v17.0/oauth/access_token?grant_type=fb_exchange_token&client_id={app_id}&client_secret={app_secret}&fb_exchange_token={user_access_token}"
response = requests.get(url)

long_access_token = response.json()["access_token"]
long_access_token

#url pra buscar informacoes de influenciador digital do instagram
user = "shibulana"
url = "https://graph.facebook.com/v21.0/"+ig_user_id+"?fields=business_discovery.username("+user+"){id,username,name,biography,website,profile_picture_url,followers_count,follows_count,media_count,media}&access_token="+user_access_token
response = requests.get(url)
data = response.json()

class influencer:
    id = data["business_discovery"]["id"]
    username = data["business_discovery"]["username"]
    name = data["business_discovery"]["name"]
    biography = data["business_discovery"]["biography"]
    try:
        website = data["business_discovery"]["website"]
    except:
        website = "none"
    profile_picture_url = data["business_discovery"]["profile_picture_url"]
    followers_count = data["business_discovery"]["followers_count"]
    follows_count = data["business_discovery"]["follows_count"]
    media_count = data["business_discovery"]["media_count"]
    media = data["business_discovery"]["media"]["data"][0]

print("\n\n",response.content,"\n\n")
print("DADOS DO INFLUENCIADOR\n")
print(f"id:\n{influencer.id}"),
print(f"username:\n{influencer.username}"),
print(f"name:\n{influencer.name}"),
print(f"biography:\n{influencer.biography}"),
print(f"website:\n{influencer.website}"),
print(f"profile_picture_url:\n{influencer.profile_picture_url}"),
print(f"followers_count:\n{influencer.followers_count}"),
print(f"follows_count:\n{influencer.follows_count}"),
print(f"media_count:\n{influencer.media_count}"),
print(f"Comentários: {influencer.media.get('comments_count')}")