from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

questions = [
    {'id': 0,
     'question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn',
     'answers': [{'answer': ''}]},
    {'id': 1,
     'question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn',
     'answers': [{'answer': ''}]},
    {'id': 2,
     'question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn',
     'answers': [{'answer': ''}]},
    {'id': 3,
     'question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn',
     'answers': [{'answer': ''}]},
]


@app.route('/api/v1/questions')
def all_questions():
    return jsonify(questions)


app.run(debug=True)
