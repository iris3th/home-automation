## Synopsis

Rasperry pi + relay shield contrallable via web interface

## Code Example

Show what the library does as concisely as possible, developers should be able to figure out **how** your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.

## Motivation

I believe all IoT stuff must be more secure, and we can't trust devices serving inside our private space and communicating with third party vendor servers.
I wanted a solution which is 

    - open source
    - easy to administer
    - reachable only from inside my VPN
    - Not communicates with third party servers at all

## Installation

required packages:

    rpi-gpio
    python
    python-flask

Hardware:
    
    rpi2 =<
    keyestudio relay board

## Tests

    export FLASK_APP=relays.py
    python -m flask run --host 0.0.0.0

    http://yourserver:5000

## Contributors

All contributors are welcome. this is a pre beta software , so its a bit hendikep at the moment
Cellphone optimized webpage , and timer function ideas are welcome

## License

GPL