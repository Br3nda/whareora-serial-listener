from mysensors import mysensors, openhab
from enum import IntEnum

class Station(IntEnum):
  MASTER_BEDROOM = 1
  LIVING_ROOM = 2

def cb(type, nid):
  print("CALLBACK for sensor: ", nid)
  sensor = gw.sensors[nid]
  print(sensor.sketch_name, sensor.sketch_version)
  station_name = Station(nid).name
  print(station_name)

  for i, child in sensor.children.items():    
    for type_id, value in child.values.items():
      v_type = gw.const.SetReq(type_id).name
      print("\t\t", v_type, value)
      try:
        openhab.send(key=v_type, station=station_name, value=value)
      except Exception as e:
        print(e)

gw = mysensors.SerialGateway('/dev/ttyUSB0', cb, persistence=True, protocol_version='1.5')
gw.start()