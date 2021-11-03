import requests
import json
API_PATH = "https://3333-tan-goose-kjycxojb.ws-us17.gitpod.io"
pload = {
            'name':'ong_name', 
            'email':'ong_email', 
            'whatsapp':'ong_whatsapp', 
            'city':'ong_city', 
            'uf':'ong_uf'}
data = {}
data['body'] = pload
headers = {'Content-Type': "application/json", 'Accept': "application/json"}
print(json.dumps(pload))
r = requests.post(API_PATH+ '/ongs', data = json.dumps(pload),headers=headers)  
print(r.status_code)
print(r.json()['id'])