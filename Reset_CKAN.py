```Python
import requests
import json

def DataStore_Delete(id):
    url = "http://<YOUR_CKAN_URL>/api/3/action/datastore_delete"
    payload = "{\"resource_id\":\"" + id + "\"}"
    headers = {
      'Authorization': '<YOUR_API_KEY>',
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    print("\t\tDataStore Excluido!!")

def Resource_Delete(id):
    url = "http://<YOUR_CKAN_URL>/api/action/resource_delete"
    payload = "{\"id\":\"" + id + "\"}"
    headers = {
      'Authorization': '<YOUR_API_KEY>',
      'Content-Type': 'application/json',
      'Cookie': 'BIGipServerVS078_HTTP.app~VS078_HTTP_pool=2567836844.56611.0000'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    print("\t\tResource Excluido!!")

url = "http://<YOUR_CKAN_URL>/api/3/action/package_list"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)
JsonListPackage = json.loads(response.text.encode('utf8'))

packages = JsonListPackage["result"]

for package in packages:
    print("Pacote: ",package)

    PackageShowURL = "http://<YOUR_CKAN_URL>/api/3/action/package_show?id=" + package
    PackageShowPAYLOAD = {}
    PackageShowHEADERS = {
        'Cookie': 'BIGipServerVS078_HTTP.app~VS078_HTTP_pool=2567836844.56611.0000' 
    }


    response = requests.request("GET", PackageShowURL, headers=PackageShowHEADERS, data = PackageShowPAYLOAD)
    jsonListResource = json.loads(response.text.encode('utf8'))
    num_resources = jsonListResource['result']['num_resources']

    tam = int(num_resources)
    i = 0
    while i < tam:
        Name = jsonListResource['result']['resources'][i]['name']
        ID = jsonListResource['result']['resources'][i]['id']
        url_type = jsonListResource['result']['resources'][i]['url_type']
        print("\tName: ",Name)
        print("\tID: ",ID)
        print("\turl_type: ", url_type,"\n")

        if(url_type == <URL_TYPE>):
            DataStore_Delete(ID)
            Resource_Delete(ID)

        i = i+1
```
