import time
import obd

connection = obd.OBD("COM9")  # auto connects to USB or RF

cmd = obd.commands.SPEED

response = connection.query(cmd)  # send command to obd

ports = obd.scan_serial()

print(ports)

print("Tesing Hello World")

while True:
    respose = connection.query(cmd)
    time.sleep(200)
    print(str(respose.value) + "\n")  # returns   unit bearing

port = connection

