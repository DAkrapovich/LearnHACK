import subprocess
import macchanger

def print_mac(interface):
	print("[/] Your new MAC is -> ")
	subprocess.call("ifconfig "+interface+" | grep ether", shell=True)

macchanger.mac_change(macchanger.parse_args().interface, macchanger.parse_args().new_mac)

