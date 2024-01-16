#import ShellyPy
import json
import requests
from funciones import *

# evice = ShellyPy.Shelly("192.168.100.30")
ip = "192.168.100.33"
switch = "0"
method_url = 'http://' + ip + '/rpc/Switch.GetStatus?id=' + switch
print(method_url)

data = requests.get(method_url).json()
print(data)
print(data['id'])
print(data['output'])
print(data['apower'])
print(data['voltage'])
print(data['current'])
print(data['pf'])
print(data['aenergy']['total']/1000)
print(data['aenergy']['by_minute'])
print(data['aenergy']['by_minute'][0])
print(data['aenergy']['by_minute'][1])
print(data['aenergy']['by_minute'][2])
print(data['aenergy']['minute_ts'])
print(data['temperature']['tC'])
'''python_dict=json.loads(data)
print(data)
print(python_dict['apower'])
print(python_dict['voltage'])
#datos = get_data_http(ip,switch)
'''
#deviceMeter = device.status()   #request meter information
#print(deviceMeter[0])     #print power information
#print(deviceMeter['total'])     #print total informatio
#print(deviceMeter)

#print(device)