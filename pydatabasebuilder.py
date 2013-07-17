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

con = mdb.connect('localhost','root','foosball','foosball');

with con:
	cur = con.cursor()
	##cur.execute('drop table if exists name_hex_data')
	##cur.execute('create table name_hex_data (Id int primary key auto_increment, name varchar(16), hex varchar(47))')
		

i='y'
while i == 'y':
        GPIO.output(5,0)
        sleep(.1)
        GPIO.output(5,1)
	s = ser.readline()
	print s
	n=s[49:66]
	n = n.capitalize().replace(".","").rstrip()
	s=s[0:47]
	print s
	print n
	print " "
	con = mdb.connect('localhost','root','foosball','foosball');

	with con:
		cur = con.cursor()
		#cur.execute('drop table if exists name_hex_data')
		#cur.execute('create table name_hex_data (Id int primary key auto_increment, name varchar(16), hex varchar(47))')
		cur.execute("insert into name_hex_data(hex,name) values('" +s+ "','"+n+"')")
		cur.execute('select hex from name_hex_data')
		rows = cur.fetchall()
		for row in rows:
			print row[0]

	i = raw_input('read another card? [y/n] ')
	
	
