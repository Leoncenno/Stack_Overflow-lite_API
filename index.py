import flask
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

questions = [
    {'id': 0,
     'Name': 'Leo',
     'Question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn',
     'Answer': ''},
    {'id': 1,
     'Name': 'Odongo',
     'Question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn',
     'Answer': ''},
    {'id': 2,
     'Name': 'Okello',
     'Question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn',
     'Answer': ''},
    {'id': 3,
     'Name': 'Opio',
     'Question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn',
     'Answer': ''},
]


class Interactions():
    @app.route('/api/v1/questions', methods=['GET'])
    def all_questions():
        return jsonify(questions)

    @app.route('/api/v1/questions/id', methods=['GET'])
    def one_question():
        if 'id' in request.args:
            id = int(request.args['id'])
        else:
            return"Sorry, no match"

        search = []

        for question in questions:
            if question['id'] == id:
                search.append(question)
        return jsonify(search)

    @app.route('/api/v1/questions', methods=['POST'])
    def add_question():
        added_question = questions.append(request.get_json())
        return jsonify(added_question)

    @app.route('/api/v1/questions/id/answers', methods=['POST'])
    def add_answer():
        if 'id' in request.args:
            id = int(request.args['id'])

        answers = []

        for question in questions:
            if question['id'] == id:
                added_answer = answers.append(request.get_json())
                return jsonify(answers)
            else:
                return "No such question"


app.run(debug=True)
