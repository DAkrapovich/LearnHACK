import subprocess
import optparse

def mac_change(interface, new_mac):
	print("[+] Starting MacChanger...")

	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw","ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])

def parse_args():
	parser = optparse.OptionParser()

	parser.add_option("-i","--interface", dest="interface", help="Inteface for changing MAC")
	parser.add_option("-m","--macaddres", dest="new_mac", help="Setter for new MAC Address")

	(options, arguments) = parser.parse_args()

	return options