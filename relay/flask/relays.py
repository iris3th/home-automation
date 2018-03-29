from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# init list with pin numbers

pinList = [4, 22, 6, 26]

# loop through pins and set mode and state to 'low'

for i in pinList:
  GPIO.setup(i, GPIO.OUT)
  GPIO.output(i, GPIO.LOW)

@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Relay 1 ON') == 'Relay 1 ON':
            # pass
            GPIO.output(4, GPIO.HIGH)
	    print("r1on")
        elif  request.form.get('Relay 1 OFF') == 'Relay 1 OFF':
            # pass # do something else
            GPIO.output(4, GPIO.LOW)
            print("Decrypted")
        if request.form.get('Relay 2 ON') == 'Relay 2 ON':
            # pass
            GPIO.output(22, GPIO.HIGH)
	    print("r1on")
        elif  request.form.get('Relay 2 OFF') == 'Relay 2 OFF':
            # pass # do something else
            GPIO.output(22, GPIO.LOW)
            print("Decrypted")
        if request.form.get('Relay 3 ON') == 'Relay 3 ON':
            # pass
            GPIO.output(6, GPIO.HIGH)
	    print("r1on")
        elif  request.form.get('Relay 3 OFF') == 'Relay 3 OFF':
            # pass # do something else
            GPIO.output(6, GPIO.LOW)
            print("Decrypted")
        if request.form.get('Relay 4 ON') == 'Relay 4 ON':
            # pass
            GPIO.output(26, GPIO.HIGH)
	    print("r1on")
        elif  request.form.get('Relay 4 OFF') == 'Relay 4 OFF':
            # pass # do something else
            GPIO.output(26, GPIO.LOW)
            print("Decrypted")
        else:
            # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return render_template("index.html")

if __name__ == '__main__':
        app.run()