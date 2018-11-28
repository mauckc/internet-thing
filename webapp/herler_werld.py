from flask import Flask
app = Flask(__name__)

# setup the base route
@app.route("/")
def hello(): # Define the hello world function to be run on webpage
    return "Hello World!"

if __name__ == "__main__":
    # Default host is localhost
    # Therefore we must pass '0.0.0.0' as host
    # in order to make the app accessible over the network
    app.run(host='0.0.0.0') 
