# internet-thing
Build an internet 'thing' with the Raspberry Pi using Python flask web application to control GPIO pulse width modulation


## Reference
Resources to use for development

### Adafruit

* Uploader: Adafruit Industries
* Raspberry Pi & Python Internet "Thing" pt 1 with Tony D! @adafruit LIVE!

https://www.youtube.com/watch?v=L55QYFnnrgo

### Sparkfun
Time of Flight distance sensor
https://www.digikey.com/product-detail/en/adafruit-industries-llc/3316/1528-1815-ND/6569763?WT.srch=1&gclid=EAIaIQobChMI37udy56C3wIVHx-tBh2nGAGtEAQYASABEgJCZ_D_BwE

Data Sheet:
https://www.st.com/resource/en/datasheet/vl6180x.pdf

i2c tutorial using module smbus
https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all


```python
# i2ctest.py
# A brief demonstration of the Raspberry Pi I2C interface, using the Sparkfun
# Pi Wedge breakout board and a SparkFun MCP4725 breakout board:
# https://www.sparkfun.com/products/8736

import smbus

# I2C channel 1 is connected to the GPIO pins
channel = 1

#  MCP4725 defaults to address 0x60
address = 0x60

# Register addresses (with "normal mode" power-down bits)
reg_write_dac = 0x40

# Initialize I2C (SMBus)
bus = smbus.SMBus(channel)

# Create a sawtooth wave 16 times
for i in range(0x10000):

    # Create our 12-bit number representing relative voltage
    voltage = i & 0xfff

    # Shift everything left by 4 bits and separate bytes
    msg = (voltage & 0xff0) >> 4
    msg = [msg, (msg & 0xf) << 4]

    # Write out I2C command: address, reg_write_dac, msg[0], msg[1]
    bus.write_i2c_block_data(address, reg_write_dac, msg)
```


### Tut Point

Next up:
https://www.tutorialspoint.com/flask/flask_sessions.htm

## Python and Flask
Set up the app with a default route and define hellow world function

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```

Run the app

```python
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
```

#### Easy to Setup
Run this on the command line

```bash
$ pip install Flask
$ FLASK_APP=hello.py flask run
 * Running on http://localhost:5000/
 ```
 
 
