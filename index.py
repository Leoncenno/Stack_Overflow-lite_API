from getallqns import Questions
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

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

@app.route('api/v1/questions', methods=['GET'])
def All_Questions():
    return jsonify(Questions)


app.run(debug=True)    































