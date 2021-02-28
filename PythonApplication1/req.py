import requests

response = requests.get('https://cybershoke.net')
print(response.status_code)
print(response.text)
