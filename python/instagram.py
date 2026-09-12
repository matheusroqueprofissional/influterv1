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
print(response.content)
long_access_token = response.json()["access_token"]
long_access_token

print("\n\n")
#url pra buscar informacoes de influenciador digital do instagram
user = "bluebottle"
url = "https://graph.facebook.com/v21.0/"+ig_user_id+"?fields=business_discovery.username("+user+"){followers_count,media_count}&access_token="+user_access_token
print("\n\nurl = "+url+"\n\n")
response = requests.get(url)
print(response.content)