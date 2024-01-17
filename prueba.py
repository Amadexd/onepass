nombre_var = ['ideq', 'modelo', 'url', 'ip', 'sw_id']
datos_v = [3, 'Shelly Pro1PM', '/rpc/Switch.GetStatus?id=', '192.168.100.33', 0]

#rint(nombre_var)
#print(datos_v)
nombre_datos_eq = dict(zip(nombre_var,datos_v))
print(nombre_datos_eq)
print(nombre_datos_eq['ideq'])