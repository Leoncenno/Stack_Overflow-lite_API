import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
    return"<h1>Stack Overflow Lite</h1><p>Where all developers meet and discuss</p>"

app.run()    































