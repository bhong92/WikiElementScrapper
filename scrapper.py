import requests
from bs4 import BeautifulSoup
import json

def findElement(element):
    url = "https://en.wikipedia.org/wiki/" + element
    response = requests.get(
        url=url
    )
    soup = BeautifulSoup(response.content, 'html.parser')

    allTxt = soup.get_text()
    cTxt = allTxt.find('Contents') - 1
    rTxt = allTxt.find('reference') + 11

    if cTxt != -2 & rTxt != -1:
        return allTxt[rTxt:cTxt]

def getJSON(e):
    info = findElement(e)
    element = {e: info}

    jsonFile = json.dumps(element, ensure_ascii=False)
    print(jsonFile)

    with open('example.json', 'w', encoding="utf-8") as outfile:
        outfile.write(jsonFile)

