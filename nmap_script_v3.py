#!/usr/bin/python3

# *** NOTE: THIS SCRIPT MUST BE RUN AS ROOT ***

# python module imports
import os
import shutil
import nmap
import sys
import subprocess
from datetime import datetime

cwd = os.getcwd()

# variable containing the filepath of the nmap scan results file
mac_list = os.path.join(cwd, "maclist.txt")

# If a file from previous nmap scans exists, create a backup of the file
if os.path.exists(mac_list):
    backup_file = os.path.join(cwd, "maclist_" + datetime.now().strftime("%Y_%m_%H:%M") + ".log.bk")
    shutil.copyfile(mac_list, backup_file)

# Open a new file for the new nmap scan results
f = open(mac_list, "w+")

# Print to console this warning
print("Don't forget to update your network in the nmap scan of this script")

# This block of code will scan the network and extract the IP and MAC address
# Create port scanner object, nm
nm = nmap.PortScanner()
# Perform: nmap -oX - -n -sn 192.168.0.1/24
# *** NOTE: -sP has changed to -sn for newer versions of nmap! ***
# Change this to your network IP range
nm.scan(hosts='10.41.30.1/24', arguments='-n -sn')
# Retrieve results for all hosts found
nm.all_hosts()
# For every host result, write their mac address and ip to the $mac_list file
for host in nm.all_hosts():
    # If 'mac' expression is found in results write results to file
    if 'mac' in nm[host]['addresses']:
        f.write(str(nm[host]['addresses']) + "\n")
    # If 'mac' expression isn't found in results print warning
    elif nm[host]['status']['reason'] != "localhost-response":
        print("MAC addresses not found in results, make sure you run this script as root!")

# Close file for editing
f.close()
# Open file for reading
f = open(mac_list, "r")
# Read each line of file and store it in a list
mac_addresses = f.read().splitlines()
# Close file for reading
f.close()

# Create a list of approved MAC addresses
approved_macs = [
    "00:24:9B:77:A5:27",
    "04:D5:90:05:D7:B3",
    "C8:D3:FF:A2:FA:44",
    "00:15:5D:1E:5D:06",
    "58:20:B1:7C:CA:26",
    "0C:37:96:3F:90:25",
    "00:15:5D:1E:5D:07",
    "B4:B6:86:CB:F2:41",
    "FC:45:96:69:05:7C",
    "0C:37:96:21:BE:14",
    "00:15:5D:1E:5D:08",
    "00:11:32:98:0A:F5",
    "08:F1:EA:EF:09:6E",
    "00:15:5D:1E:5D:01",
    "00:15:5D:1E:5D:0A",
    "00:15:5D:1E:5D:0F",
    "84:25:3F:30:8A:3F",
    "00:04:A5:3F:2D:10",
    "8C:85:C1:04:3D:C0",
    "E0:63:DA:A0:13:E2",
    "74:AC:B9:60:1C:63",
    "EC:B1:D7:0A:19:40",
    "58:38:79:60:FD:66",
    "2C:27:D7:12:D5:A8",
    "2C:27:D7:12:D5:A4",
    "2C:27:D7:12:D5:4C",
    "A0:D3:C1:EB:53:DE",
    "30:8D:99:AF:76:6E",
    "D4:C9:EF:20:FE:C0",
    "08:F1:EA:EF:09:6C",
    "94:57:A5:33:7E:40",
    "F0:9F:C2:79:26:9F",
    "70:BC:10:82:53:CF",
    ]

# Create empty list of new devices found on network
new_devices = []

# For every list entry in the mac_addresses list
for i in mac_addresses:
    # Convert the list index from a string to a dictionary so we can parse out mac address for comparison
    dic = eval(i)
    # Compare mac address portion of dictionary to mac addresses in the master_mac_addresses file
    # If the scanned mac address is not in the master_mac_addresses file
    if dic['mac'] not in approved_macs:
        # Add scanned mac address to new devices list
        new_devices.append(dic)

# If the new_devices list isn't empty
if len(new_devices) != 0:
    # output a warning to the console
    warning = "\nWARNING!! NEW DEVICE(S) ON THE LAN!! - UNKNOWN MAC ADDRESS(ES): " + str(new_devices) + "\n"
    print(warning)

    # Create email notification of the warning
    try:
        # subject of email
        subject = "WARNUNG, neues Geraet im Netzwerk!"
        # content of email
        content = "Neues unbekanntes Geraet im Netzwerk:\n"
        for device in new_devices:
            content += f"IP address: {device['ipv4']}\nMAC address: {device['mac']}\n\n"
        # shell process of sending email with mutt
        m1 = subprocess.Popen('echo "{content}" | mail -s "{subject}" ictsupport@suicorr.com'.format(
            content=content, subject=subject), shell=True)
        # output whether email was successful in sending or not
        print(m1.communicate())

    # if sending of the email fails, this will output why
    except OSError as e:
        print("Error sending email: {0}".format(e))
    except subprocess.SubprocessError as se:
        print("Error sending email: {0}".format(se))
