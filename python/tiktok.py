import requests
import os
import requests


#client_Key = "awk7flwj0qs0bfa2"
#client_Secret = "kt5h8vCPISJ0QJPo7sbb2ZPcIysAma56"
client_key_sandbox = "sbawh7e5w89csinhzs"
client_secret_sandbox = "gLKjAK6Gvm4w9UCz5xHgJrYeu8xTqzFO"
r = requests.get('https://open.tiktokapis.com/v2/research/video/query/?fields=id%2Clike_count')
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

CLIENT_KEY = os.getenv("sbawh7e5w89csinhzs")
CLIENT_SECRET = os.getenv("gLKjAK6Gvm4w9UCz5xHgJrYeu8xTqzFO")

TOKEN_URL = "https://open.tiktokapis.com/v2/oauth/token/"
