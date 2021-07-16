from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

questions = [
    {'pk': 0,
     'question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn',
     'answers': [{'answer': 'none yet'}]},
    {'pk': 1,
     'question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn',
     'answers': [{'answer': ''}]},
    {'pk': 2,
     'question': 'I leon the one making this ahppen at the firsty place?',
     'answers': [{'answer': ''}]},
    {'pk': 3,
     'question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn',
     'answers': [{'answer': ''}]},
]


@app.route('/api/v1/questions')
def all_questions():
    return jsonify(questions)


@app.route('/api/v1/question/<pk>')
def one_question(pk):
    for question in questions:
        if question['pk'] == int(pk):
            return jsonify(question)
        else:
            return jsonify({'warning': 'Invalid question ID'}), 404


app.run(debug=True)
