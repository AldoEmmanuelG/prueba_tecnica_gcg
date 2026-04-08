import requests
from flask import Flask, request, jsonify
url="https://pokeapi.co/api/v2/pokemon"
prueba=requests.get(url)
if prueba.status_code==200:
    print("Se logro")
else:
    print("No funciono")
pokemon=prueba.json()
while (pokemon["next"]!=None):
    for usuario in pokemon["results"]:
        print(usuario["name"])
        url_temp=usuario["url"]
        sacar=requests.get(url_temp)
        print(sacar)
        temporal=sacar.json()
        print(temporal["weight"])
        print(temporal["height"])
new_url=pokemon["next"]
respo=requests.get(new_url)
pokemon=respo.json()