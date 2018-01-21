import sys
import time
import serial

BAUD_RATE = 9600

if len(sys.argv) != 2:
    print("Please provide the serial port name")
    sys.exit(1)

serial_port = sys.argv[1]

arduino = serial.Serial(
    serial_port,
    BAUD_RATE,
    serial.EIGHTBITS,
    serial.PARITY_NONE,
    serial.STOPBITS_ONE)

time.sleep(2)

while True:
    command = input()
    arduino.write(command.encode('utf-8'))
    line = arduino.readline().rstrip()
    print(line.decode('utf-8'))

