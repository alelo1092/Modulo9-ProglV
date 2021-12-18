# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 17:11:30 2021

"""

import requests

URL = "https://www.swapi.tech/api/films/"

data = requests.get(URL)
data = data.json()
Resultados_Planetas = []
Numero_Peliculas = []
for i in range(1,6):
    URL=URL + str(i)
    data = requests.get(URL)
    data = data.json()
    Planets = (data['result']['properties']['planets'])
    for element in Planets:
        data_Planet = requests.get(element)
        data_Planet = data_Planet.json()
        if ('arid' in data_Planet['result']['properties']['climate']) == True:
            if (data['result']['properties']['title'] not in Numero_Peliculas) == True:
                Numero_Peliculas.append(data['result']['properties']['title'])
    URL = "https://www.swapi.tech/api/films/"
print('Las peliculas donde aparecen planetas áridos son : ',Numero_Peliculas)


## Wookies

URL = "https://www.swapi.tech/api/films/6/"
data = requests.get(URL)
data = data.json()
Species = (data['result']['properties']['species'])
Wookies = []
for element in Species:
    data_species = requests.get(element)
    data_species = data_species.json()
    if data_species['result']['properties']['name'] == 'Wookie':
        Peoples_Species = data_species['result']['properties']['people']
        for people in Peoples_Species:
            if (people in (data['result']['properties']['characters'])) == True:
                Wookie = requests.get(people)
                Wookie = Wookie.json()
                Wookies.append(Wookie['result']['properties']['name'])

print('Los wookies que aparecen en la pelicula 6 son : ',Wookies)
                
    


## Aeronave

URL ="https://www.swapi.tech/api/vehicles/"
data = requests.get(URL)
data = data.json()
Aeronaves = []
for i in range(1,58):
    try:
        URL = "https://www.swapi.tech/api/vehicles/"
        URL=URL + str(i)+'/'
        dataV = requests.get(URL)
        dataV = dataV.json()
        Info = (dataV['result']['properties']['length'],dataV['result']['properties']['name'])
        Aeronaves.append(Info)
    except:
        print('No se han encontrado')


for i in range(1,39):
    try:
        URL = "https://www.swapi.tech/api/starships/"
        URL=URL + str(i)+'/'
        dataV = requests.get(URL)
        dataV = dataV.json()
        Info = (dataV['result']['properties']['length'],dataV['result']['properties']['name'])
        Aeronaves.append(Info)
    except:
        pass

Mas_Grande = float(Aeronaves[0][0])
Nombre_Mas_Grande = Aeronaves[0][1]
for element in Aeronaves:
    try:
        if float(element[0])>Mas_Grande:
            Mas_Grande = float(element[0])
            Nombre_Mas_Grande = (element[1])
    except:
        print('Dato no Valido')

print('La Aeronave Mas grande de la saga es : ',Nombre_Mas_Grande,'Tiene un tamaño de :',Mas_Grande)





