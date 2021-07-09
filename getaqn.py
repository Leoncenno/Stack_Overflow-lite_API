import flask
from flask import request, jsonify

Questions = [
    {'id': 0,
    'Name': 'Leo',
    'Question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn'},
    {'id': 1,
    'Name': 'Odongo',
    'Question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn'},
    {'id': 2,
    'Name': 'Okello',
    'Question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn'},
    {'id': 3,
    'Name': 'Opio',
    'Question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn'},
]

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/questions/id', methods=['GET'])
def id():
    Question = []
    if 'id' in request.args:
        id = int(request.args['id'])
    
        for question in Questions:
            if question['id'] == id:
                Question.append(question)
                return jsonify(Question)
            else:
                return"No such question"    

app.run()