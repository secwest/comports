import serial.tools.list_ports

def list_com_ports_detailed():
    """
    Lists all available COM ports with detailed information including VID, PID, Serial Number, and Manufacturer.
    """
    ports = serial.tools.list_ports.comports()
    if not ports:
        print("No COM ports found.")
        return

    header = f"{'COM Port':<10} {'Description':<40} {'VID':<6} {'PID':<6} {'Serial Number':<20} {'Manufacturer':<20}"
    print(header)
    print("-" * len(header))

    for port in ports:
        com_port = port.device
        description = port.description
        vid = f"{port.vid:04X}" if port.vid else "N/A"
        pid = f"{port.pid:04X}" if port.pid else "N/A"
        serial_number = port.serial_number if port.serial_number else "N/A"
        manufacturer = port.manufacturer if port.manufacturer else "N/A"
        print(f"{com_port:<10} {description:<40} {vid:<6} {pid:<6} {serial_number:<20} {manufacturer:<20}")

if __name__ == "__main__":
    list_com_ports_detailed()
