import RPi.GPIO as GPIO
from Adafruit_IO import Client
import time

ADAFRUIT_IO_USERNAME = "ecs1002"
ADAFRUIT_IO_KEY = "xjnkvfbjfabnuhnfe38u48bh"

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

def switch_on_motor():
    GPIO.output(18, False)

def switch_off_motor():
    GPIO.output(18, True)

def switch_on_bulb():
    GPIO.output(23, False)

def switch_off_bulb():
    GPIO.output(23, True)

def switch_on_light():
    GPIO.output(24, False)

def switch_off_light():
    GPIO.output(24, True)

def switch_on_socket():
    GPIO.output(20, False)

def switch_off_socket():
    GPIO.output(20, True)

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

while True:
    data = aio.receive('relay-1')
    data2 = aio.receive('relay-2')
    data3 = aio.receive('relay-3')
    data4 = aio.receive('relay-4')
    
    if data.value == '1':
        switch_on_motor()
    elif data.value == '0':
        switch_off_motor()
    
    if data2.value == 'ON':
        switch_on_bulb()
    elif data2.value == 'OFF':
        switch_off_bulb()
    
    if data3.value == 'Lon':
        switch_on_light()
    elif data3.value == 'Lof':
        switch_off_light()
    
    if data4.value == 'Son':
        switch_on_socket()
    elif data4.value == 'Sof':
        switch_off_socket()
    
    time.sleep(1)
