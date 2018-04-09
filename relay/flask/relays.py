#!/usr/bin/env python
from flask import Flask, render_template, request
from flask_mobility import Mobility
from flask_mobility.decorators import mobile_template

import RPi.GPIO as GPIO
import time

app = Flask(__name__)
Mobility(app)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# init list with pin numbers

pinList = [4, 22, 6, 26]

# loop through pins and set mode and state to 'low'

#for i in pinList:
#  GPIO.setup(i, GPIO.OUT)
#  GPIO.output(i, GPIO.LOW)

def rstatus():
    n = 1
    pinList = [4, 22, 6, 26]
    f= open("static/status.txt","w+")
    for k in pinList:
        GPIO.setup(k, GPIO.IN)
	f.write ("Relay %d is in state %d" % (n, GPIO.input(k)) + '\n')
	GPIO.setup(k, GPIO.OUT)
	n = n + 1
    f.close()
#    print(open("static/status.txt").read())

@app.route("/", methods=['GET', 'POST'])
@mobile_template('/{mobile/}index.html')
def index(template):
#    print(request.method)
    rstatus()
    if request.method == 'POST':
        if request.form.get('Relay 1 ON') == 'Relay 1 ON':
            GPIO.output(4, GPIO.HIGH)
	    rstatus()
	elif  request.form.get('Relay 1 OFF') == 'Relay 1 OFF':
            GPIO.output(4, GPIO.LOW)
	    rstatus()
        if request.form.get('Relay 2 ON') == 'Relay 2 ON':
            GPIO.output(22, GPIO.HIGH)
	    rstatus()
        elif  request.form.get('Relay 2 OFF') == 'Relay 2 OFF':
            GPIO.output(22, GPIO.LOW)
	    rstatus()
        if request.form.get('Relay 3 ON') == 'Relay 3 ON':
            GPIO.output(6, GPIO.HIGH)
	    rstatus()
        elif  request.form.get('Relay 3 OFF') == 'Relay 3 OFF':
            GPIO.output(6, GPIO.LOW)
	    rstatus()
        if request.form.get('Relay 4 ON') == 'Relay 4 ON':
            GPIO.output(26, GPIO.HIGH)
	    rstatus()
        elif  request.form.get('Relay 4 OFF') == 'Relay 4 OFF':
            GPIO.output(26, GPIO.LOW)
	    rstatus()
        else:
            return render_template(template)
    elif request.method == 'GET':
        print("No Post Back Call")
    return render_template(template)


if __name__ == '__main__':
#        app.run(host='0.0.0.0', port=80)
        app.run(host='0.0.0.0', port=5000, use_reloader=True)
#	rstatus()
