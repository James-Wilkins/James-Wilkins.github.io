import requests

url = "https://aerodatabox.p.rapidapi.com/flights/airports/icao/EGGD/2021-10-04T20:00/2021-10-05T08:00"

querystring = {"withLeg":"true","withCancelled":"true","withCodeshared":"true","withCargo":"true","withPrivate":"true","withLocation":"false"}

headers = {
    'x-rapidapi-host': "aerodatabox.p.rapidapi.com",
    'x-rapidapi-key': "514813b33bmsh1a3ab90de5db55ep11f05bjsnfa3bff251bb6"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
