import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text) #r.text es un str, hay que pasarlo a continuación a formato lista
    categories = r.json()
    for category in categories:
        print(category['name'])
