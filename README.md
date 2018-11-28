# internet-thing
Build an internet 'thing' with the Raspberry Pi using Python flask web application to control GPIO pulse width modulation


## Reference
Resources to use for development

### Adafruit

* Uploader: Adafruit Industries
* Raspberry Pi & Python Internet "Thing" pt 1 with Tony D! @adafruit LIVE!

https://www.youtube.com/watch?v=L55QYFnnrgo

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
 
 
