import RPi.GPIO as GPIO
import serial
import glob
import MySQLdb as mdb
from time import sleep
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)
GPIO.output(5,0)
sleep(.1)
GPIO.output(5,1)
sleep(.1)
GPIO.output(5,0)
sleep(.1)
GPIO.output(5,1)

if '/dev/ttyACM1' in glob.glob('/dev/tty*'):
  ser = serial.Serial('/dev/ttyACM1',115200)
else:
	ser = serial.Serial('/dev/ttyACM0',115200)
i='y'
while i == 'y':
	s = ser.readline()
	print s
	n=s[49:66]
	#n = n.replace(".", "")
	n = n.capitalize()
	s=s[0:47]
	print s
	print n
	print " "
	con = mdb.connect('localhost','root','foosball','foosball');

	with con:
		cur = con.cursor()
		cur.execute("insert into Name_hex_data(hex,name) values('" +s+ "','"+n+"')")
		cur.execute('select hex from Name_hex_data')
		rows = cur.fetchall()
		for row in rows:
			print row[0]

	i = raw_input('read another card? [y/n] ')
	
	
