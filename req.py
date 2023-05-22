import requests

#GET-запрос:

status = 'available'
res1 = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers={'accept': 'application/json'})
print("Ответы запроса GET:")
print(res1.status_code)
print(res1.json())

#POST-запрос:
url2 = "https://petstore.swagger.io/v2/pet"
headers2 = {'accept': 'application/json', 'Content-Type': 'application/json'}
data2 = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res2 = requests.post(url2, headers=headers2, json=data2)

print("\nОтветы запроса POST:")
print(res2.status_code)
print(res2.json())

#DELETE-запрос:

url3 = "https://petstore.swagger.io/v2/pet/pet_id"
headers3 = {'accept': 'application/json'}

res3 = requests.delete(url3, headers=headers3)

print("\nОтветы запроса DELETE:")
print(res3.status_code)
print(res3.json())

#PUT-запрос:

res4 = requests.put(url2, json=data2)

print("\nОтветы запроса PUT:")
print(res4.status_code)
print(res4.json())