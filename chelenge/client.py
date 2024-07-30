import requests

request = requests.get("http://127.0.0.1:5000/")
print(request.text)

request = requests.post("http://127.0.0.1:5000/add_post", json={})
print(request.text)

request = requests.get("http://127.0.0.1:5000/profile")
print(request.text)

request = requests.post("http://127.0.0.1:5000/add_cat", json ={})
print(request.text)