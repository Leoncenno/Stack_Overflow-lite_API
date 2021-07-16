from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

questions = [
    {'id': 0,
     'question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn',
     'answers': [{'answer': 'none yet'}]},
    {'id': 1,
     'question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn',
     'answers': [{'answer': ''}]},
    {'id': 2,
     'question': 'I leon the one making this ahppen at the firsty place?',
     'answers': [{'answer': ''}]},
    {'id': 3,
     'question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn',
     'answers': [{'answer': ''}]},
]


@app.route('/api/v1/questions')
def all_questions():
    return jsonify(questions)


@app.route('/api/v1/questions/<id>')
def one_question(id):
    if 'id' in request.args:
        id = int(request.args['id'])
    for question in questions:
        if question['id'] == int(id):
            return jsonify(question)
    else:
        return jsonify({'warning': 'Invalid question ID'}), 404


app.run(debug=True)
