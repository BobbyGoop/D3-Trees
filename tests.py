import requests

headers = {"content-type": "application/json"}

# TODO: Client requests
client_params = {'client_name': 'test',
				 'client_surname': 'testoviy',
				 'client_email': 'ivans200188@gmail.com'}

client_post = {
		"name": "slave",
		"surname": "slave",
		"email": "dasdad"
}

client_patch = {
		"id": 3,
		"name": "slave",
		"surname": "slave",
		"email": "sdfdsf"
}

# r = requests.get(" http://127.0.0.1:5000/api/clients/")
# r = requests.post(" http://127.0.0.1:5000/api/clients/", params = client_params)
# r = requests.post(" http://127.0.0.1:5000/api/clients/", json = json_post)
# r = requests.patch(" http://127.0.0.1:5000/api/clients/", headers = headers, json = json_patch)
# r = requests.patch(" http://127.0.0.1:5000/api/clients/", params = client_params)
# r = requests.delete("http://127.0.0.1:5000/api/clients/", params = {"client_id": 3})
# r = requests.post(" http://127.0.0.1:5000/api/orders/", headers = headers, params = order_params)


# TODO: Order requests

order_params = {
	"client_id": 8,
	"total": 300,
}

order_post = {
		"client_id": 8,
		"total": 200,
}

order_patch = {
		"id": 6,
		"client_id": 10,
		"total": 200,
}

# r = requests.get(" http://127.0.0.1:5000/api/orders/", params = order_params)
# r = requests.post("http://127.0.0.1:5000/api/orders/", json = order_params)
# r = requests.patch(" http://127.0.0.1:5000/api/orders/", json = order_patch )
r = requests.delete("http://127.0.0.1:5000/api/orders/", params = {"order_id": 6})

print(r.text)
print(r.status_code)
