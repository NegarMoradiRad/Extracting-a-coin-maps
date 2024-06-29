import requests
import json
import xmltodict


url = "https://sahmeto.com/crypto-sitemap.xml"


response = requests.get(url)


if response.status_code == 200:
   
    xml_data = response.content.decode('utf-8')

    
    data_dict = xmltodict.parse(xml_data)

for url in data_dict['urlset']['url']:
    coin_name = url['loc'].split('/')[-1]  
    url['name'] = coin_name
    
    json_data = json.dumps(data_dict, indent=4)

    
    print(json_data)
else:
    print("Error loading xml data:", response.status_code)