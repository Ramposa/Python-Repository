import sys
import subprocess
import os
from decouple import config

IP_NETWORK = config('IP_NETWORK')
IP_DEVICE = config('IP_DEVICE')


proc = subprocesss.Popen(['ping', IP_NETWORK], stdout=subprocess.PIPE)

while True:
    line = proc.stdout.readline()
    if not line:
        break
    connect_ip = line.decode('utf-8').split()[3]

    if connected_ip == IP_DEVICE:
        subprocess.Popen(['say', 'Person just connected to the network.'])

    # Import time and call the
    # time.sleep() method to have the script run.
    #