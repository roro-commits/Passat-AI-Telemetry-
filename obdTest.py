import time
import obd

connection = obd.OBD("COM9")  # auto connects to USB or RF
cmd = obd.commands.SPEED

def obd_response(connection,cmd) -> list[str,float,bool,str,float]:
    obd_response = connection.query(cmd)
    obd_port_name = connection.port_name()
    obd_response_output = []
    
    if not obd_response.is_null():
        obd_response_output =  list(obd_port_name)
        obd_response_output =  list(obd_response.value)
        obd_response_output =  list(obd_response.command)
        obd_response_output =  list(obd_response.message)
        obd_response_output =  list(time.time())
    
    return obd_response_output
        
                    
while True:

    vechile_speed = obd_response(connection=connection, cmd= cmd)
    print("vechile speed",vechile_speed)
    print("vechile speed",vechile_speed[1].rstrip)
    
    
