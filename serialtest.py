import serial   
import os, time

# Enable Serial Communication
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)

# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key
while(1):
     port.write(b'AT'+'\r\n')
     rcv = port.read(10)
     print rcv
     time.sleep(1)