import time
import json
from pyModbusTCP.client import ModbusClient

# Establishing Modbus client and loading addresses from a JSON file
client = ModbusClient(host="192.168.1.3", port=502)
f = open('./main/addresses.json')
addresses = json.load(f)["addresses"]

# Function to read data based on the address and data type
def read_data(address, data_type):
    if data_type == 1:  # For double registers
        data = client.read_holding_registers(address, 2)
        if data:
            counter, overflow = data
            double = (overflow * 65536) + counter
            return double
    elif data_type == 0:  # For single registers
        data = client.read_holding_registers(address, 1)
        if data:
            return data[0]
    return None

# Check if client is connected to the Modbus server
connected = client.open()

# Continuously fetch and print data
while True:    
    if not connected:  # Reconnect if not connected
        print("CHECK LAN")
        connected = client.open()
        time.sleep(2)
        continue

    output_data = []
    # Go through addresses and read data
    for addr, data_type in addresses:
        result = read_data(addr, data_type)
        if result is not None:
            output_data.append({
                "address": addr,
                "timestamp": int(time.time()),
                "data": result
            })

    if output_data:
        for data in output_data:
            print(f"{data['address']} {data['timestamp']}  {data['data']}")
    else:
        print("No data retrieved Check Lan")  # Indicate when no data is retrieved
        
    print()

    time.sleep(5)  # Wait for 5 seconds before fetching data again
