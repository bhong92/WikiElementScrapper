# WikiElementScrapper
Scrapes the introductory paragraph on Wikipedia for Elements

Example Request:
  run the main python file as server
    uvicorn main:app --reload

  In main application make a POST request to url as so
    url = 'http://127.0.0.1:8000/api/chem-wiki/'
    test = {'name': 'Helium'}
    x = requests.post(url, json=test)
    print(x)
    
    prints out
    {"Helium": "Helium (from Greek: ἥλιος, romanized: helios, lit. 'sun') is a....}
