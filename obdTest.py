import time
import obd

connection = obd.OBD("COM9")  # auto connects to USB or RF
cmd = obd.commands.SPEED

#TODO add logging of infomation

def obd_response(obd_command: any) -> list:
    """Store the OBDResponse objects properties in a list.

    value:	The decoded value from the car
    command:	The OBDCommand object that triggered this response
    message:	The internal Message object containing the raw response from the car
    time:	Timestamp of response (as given by time.time()).
    """
    obd_query_response = connection.query(obd_command)
    obd_port_name = connection.port_name()
    obd_response_output = []  # Todo chnage to dictionary

    if not obd_query_response.is_null():
        print(obd_query_response)
        obd_response_output.append(obd_port_name)
        obd_response_output.append(obd_query_response.value)
        obd_response_output.append(obd_query_response.command)
        obd_response_output.append(obd_query_response.messages)
        obd_response_output.append(str(time.time()))

    else:
        print("OBD has no response")

    return obd_response_output


def obd_status() -> tuple:
    """Return tuple of obd status.

    Information about the Malfunction Indicator Light (check-engine light), the number
    of trouble codes being thrown, and the type of engine.
    """
    obd_command = obd.commands.STATUS
    obd_query_response = connection.query(obd_command)
    # dtc_count = obd_query_response.value.DTC_count
    check_engine_lit = obd_query_response.value.MIL
    ignition_type = obd_query_response.value.ignition_type

    return (obd_query_response, check_engine_lit, ignition_type)


def obd_status_test(obd_status: tuple) -> None:
    # TODO cycle true mutliple test and do some checks
    """Test names that python-OBD reports.

    These are exposed as StatusTest objects, loaded into named properties.
    Each test object has boolean flags for its availability and completion.
    """
    tests = [
        "MISFIRE_MONITORING",
        "FUEL_SYSTEM_MONITORING",
        "COMPONENT_MONITORING",
        "CATALYST_MONITORING",
        "HEATED_CATALYST_MONITORING",
        "EVAPORATIVE_SYSTEM_MONITORING",
        "SECONDARY_AIR_SYSTEM_MONITORING",
        "OXYGEN_SENSOR_MONITORING",
        "OXYGEN_SENSOR_HEATER_MONITORING",
        "EGR_VVT_SYSTEM_MONITORING",
        "NMHC_CATALYST_MONITORING",
        "NOX_SCR_AFTERTREATMENT_MONITORING",
        "BOOST_PRESSURE_MONITORING",
        "EXHAUST_GAS_SENSOR_MONITORING",
        "PM_FILTER_MONITORING",
    ]
    obd_query_response = obd_status[0]
    print("Obd test!:")
    time.sleep(5)
    print(obd_query_response.value.ignition_type)
    print(obd_query_response.value.FUEL_SYSTEM_MONITORING)
    print(
        "FUEL_SYSTEM_MONITORING -> completed",
        obd_query_response.value.FUEL_SYSTEM_MONITORING.complete,
    )
    print(
        "FUEL_SYSTEM_MONITORING -> available",
        obd_query_response.value.FUEL_SYSTEM_MONITORING.available,
    )


while True:
    vechile_speed = obd_response(cmd)
    status = obd_status()
    print("vechile status: ", status)
    time.sleep(3)
    print(vechile_speed[1])

    obd_status_test(status)
