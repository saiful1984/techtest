import requests

print("Testing PUT method")
data = [{
    'firstName': "Syed",
    'middleName': "Saiful",
    'lastName': "Arefin",
    'age': 37
},
{
    'firstName': "Syed",
    'middleName': "NURUL",
    'lastName': "Arefin",
    'age': 43
}]

for index in range(len(data)):
    BASE = "http://localhost:8000/api/v1.0/apiTasks/{}".format(int(index) + 1)
    response = requests.put(BASE, data[index])
    print(response.json())


print("Database after PUT method")
for index in range(len(data)):
    BASE = "http://localhost:8000/api/v1.0/apiTasks/{}".format(int(index) + 1)
    response = requests.get(BASE)
    print(response.json())

print("Testing PATCH method")
new_data = {
    'firstName': "sample",
    'lastName': "sample",
    'age': 370
}
BASE = "http://localhost:8000/api/v1.0/apiTasks/1"
response = requests.patch(BASE, new_data)
print(response.json())
print("Database after PATCH method")
response = requests.get(BASE)
print(response.json())

print("Testing DELETE method")
for index in range(len(data)):
    BASE = "http://localhost:8000/api/v1.0/apiTasks/{}".format(int(index) + 1)
    response = requests.delete(BASE)
    print(response)
print("Database after DELETE method")
for index in range(len(data)):
    BASE = "http://localhost:8000/api/v1.0/apiTasks/{}".format(int(index) + 1)
    response = requests.get(BASE)
    print(response)
