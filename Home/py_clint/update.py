import requests

ENDPOINT = 'http://127.0.0.1:8000/products/1/update/'

data ={
    
    'title':'updated data',
    'price':56.5
}


resp = requests.put(ENDPOINT,json=data)

print(resp.json())