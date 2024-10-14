from gpiozero import Device

Device.ensure_pin_factory()

board_info = Device.pin_factory.board_info
#print(Device.pin_factory.board_info)

def print_all_info():
    print("               Device info:")
    print(f"Revision: {board_info.revision}, model: Raspberry Pi {board_info.model}")
    print(f"Pcb Revision: {board_info.pcb_revision}, Released: {board_info.released}")
    print(f"Soc: {board_info.soc}, Manufacturer: {board_info.manufacturer}, Memory: {board_info.memory}")
    print(f"Total usb ports: {board_info.usb}, Total usb 3 ports: {board_info.usb3}")
    print(f"Ethernet ports {board_info.ethernet}, Ethernet speed: {board_info.eth_speed}")
    print(f"wifi: {board_info.wifi}, bluetooth: {board_info.bluetooth}")
    
    print(f"CSI connector: {board_info.csi}, DSI connector: {board_info.dsi}")


print_all_info()
