import datetime
import requests

# openhab_host = '127.0.0.1'
# openhab_host = 'openhab.service.consul'
# openhab_port = '80'
openhab_host = '10.1.1.85'
openhab_port = '8080'

def send(station, key, value):
  url = 'http://{host}:{port}/rest/items/MySensors_{station}{key}/state'.format(host=openhab_host, port=openhab_port, station=station, key=key)

  response = requests.put(url, headers={'Content-Type': 'text/plain'}, data=str(value))
  print(response.text)

  if response.status_code != requests.codes.ok:
    response.raise_for_status()   
