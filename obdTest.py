import obd

connection = obd.OBD("COM9")  # auto connects to USB or RF

cmd = obd.commands.SPEED

respose = connection.query(cmd)  # send command to obd

ports = obd.scan_serial()

print(ports)

print("Tesing Hello World")

print(str(respose.value) + "\n")  # returns   unit bearing

port = connection

