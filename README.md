# Modbus Data Retrieval Script

This Python script retrieves data from a Modbus server using the pyModbusTCP library. It continuously reads data based on specified Modbus addresses and handles reconnection to the server if the connection is lost.

## Requirements

- Python 3.x
- pyModbusTCP library (`pip install pyModbusTCP`)

## Usage

1. Clone the repository or download the `MOD.py` script.
2. Ensure Python 3.x is installed on your system.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Update the `addresses.json` file with your Modbus addresses and their corresponding data types.
5. Modify the script's configuration (e.g., IP address, port) according to your Modbus server settings.
6. Run the script via the command line: `python modbus_data_retrieval.py`.

## Configuration

- **addresses.json**: Contains the Modbus addresses and data types for retrieval.
- Update the `host` and `port` variables in the script to match your Modbus server's IP address and port.

## Functionality

- Establishes a connection to the Modbus server and reads data continuously from specified addresses.
- Handles reconnection attempts to the Modbus server in case of connection loss.
- If reconnection fails, the script checks the LAN connection.

## Important Notes

- Ensure that the Modbus server is accessible from the network where this script is executed.
- Customize error handling or data processing as per your specific use case.

## Troubleshooting

- If encountering connection issues, verify the Modbus server's IP address, port, and network connectivity.
- Check the `addresses.json` file for correct Modbus addresses and data types.
- Adjust script configurations based on your Modbus server's setup.

## License

This project is licensed under the [MIT License](LICENSE).
"# Catalis-HMI" 
