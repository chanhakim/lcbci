import serial
import time
import re
from data_list import *

DUE = serial.Serial('/dev/cu.usbmodem142401')

while True:
	try:
		line = str(DUE.readline())
		value = int(re.sub(r'\D', "", line))
		print(value)
		data.add(value)
			time.sleep(0.1)
	except KeyboardInterrupt:
		print("KeyboardInterrupt")
		print(data.__list__())
		break
