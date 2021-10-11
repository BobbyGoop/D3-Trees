import requests
import time
client_json = {
		"email": "ivans200188@gmail.com",
		"password": "12345"
}

r = requests.post("http://127.0.0.1:5000/api/login/", json=client_json)
print(r.text, r.status_code)
access_token = r.json()['access_token']
print("Token: ", access_token)

time.sleep(5)

headers = {
	'Authorization': f'Bearer {access_token}'
}
r2 = requests.get("http://127.0.0.1:5000/api/clients/", headers=headers)
print(r2.text, r2.status_code)

r3 = requests.delete("http://127.0.0.1:5000/api/logout/", headers = headers)
print(r2.text, r2.status_code)

r2 = requests.get("http://127.0.0.1:5000/api/clients/", headers=headers)
print(r2.text, r2.status_code)