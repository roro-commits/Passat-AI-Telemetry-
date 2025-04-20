import time
import obd

connection = obd.OBD("COM9")  # auto connects to USB or RF
cmd = obd.commands.SPEED


while True:
    respose = connection.query(cmd)  # send command to obd
    port_names  = connection.port_name()
    print("!!!!!- sending the request to OBD2- %s !!!!! ",port_names)
    print("!!!!!- sending the request to OBD2- %f!!!!!! ",respose.value,time.time())
    print("!!!!!- sending the request to OBD2- %s !!!!!!",respose.is_null())
    print("!!!!!- sending the request to OBD2- %s !!!!!!",respose.messages)
    print("!!!!!- sending the request to OBD2- %s !!!!!!",respose.command)


    respose = connection.query(cmd)
    time.sleep(2)
    print(str(respose.value) + "\n")  # returns   unit bearing
    port = connection    

