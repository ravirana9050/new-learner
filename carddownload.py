import requests
import json

def getPokemonData(pokemon_name):
    url = "https://api.pokemontcg.io/v1/cards?name={}" .format(pokemon_name)
    response = requests.get(url)
    return  response.json()


pokemon_name = input("enter the pokemon's name: ")
x = getPokemonData(pokemon_name)
#print(x)
#print(x['cards'])
imgUrl = x['cards'][0]['imageUrl']

img = requests.get(imgUrl)

imageName = pokemon_name+'-photo.png'

with open(imageName,'wb') as file:
    for i in img.iter_content(1024):
        file.write(i)

