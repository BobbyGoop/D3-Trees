import requests
client_json = {
		"email": "asdasd@123",
		"password": "123"
}

r = requests.post("http://127.0.0.1:5000/api/auth/", json = client_json)
print(r.text, r.status_code)
access_token = r.json()['access_token']
print("Token: ", access_token)

headers = {
	'Authorization': f'Bearer {access_token}'
}
r2 = requests.get("http://127.0.0.1:5000/api/clients/", headers = headers)
print(r2.text, r2.status_code)
