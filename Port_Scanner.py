#!bin/python3
import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid number of arguments!")

print("-" * 60)
print(f"Scanning Target: {target}")
print(f"Time started: {datetime.now()}")
print("-" * 60)

try:
    lower = int(input("Lower Bound of Port Range: "))
    upper = int(input("Upper Bound of Port Range: "))
    print("-" * 60)
    print("PLEASE WAIT!")
    print("SCANNING...")
    for port in range(lower, upper):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is Open!")
        s.close()

except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit()

except socket.gaierror:
    print("Host name could not be resolved!")
    sys.exit()

except socket.error:
    print("Could not connect to the server!")
    sys.exit()
