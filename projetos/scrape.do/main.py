import requests
import urllib.parse

token = "YOUR_TOKEN"
targetUrl = "https://httpbin.co/ip"

encoded_url = urllib.parse.quote(targetUrl)
url = "http://api.scrape.do?token={}&url={}".format(token, encoded_url)
response = requests.request("GET", url)

print(response.text)