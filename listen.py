from mysensors import mysensors, openhab
from enum import IntEnum

class Station(IntEnum):
  MASTER_BEDROOM = 6
  KITCHEN = 2
  LIVING_ROOM = 3
  CASEY_ROOM = 4
  STUDY = 5



def cb(type, nid):
  print("CALLBACK for sensor: ", nid)
  sensor = gw.sensors[nid]
  print(sensor.sketch_name, sensor.sketch_version)
  try:
    station_name = Station(nid).name
  except ValueError:
    station_name = "UNKNOWN_STATION_{nid}".format(nid=nid)

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