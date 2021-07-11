import flask
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

Questions = [
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
        return jsonify(Questions)

    @app.route('/questions/id', methods=['GET'])
    def one_question():
        if 'id' in request.args:
            id = int(request.args['id'])
        else:
            return"Sorry, no match"

        search = []

        for Question in Questions:
            if Question['id'] == id:
                search.append(Question)
        return jsonify(search)
            

    @app.route('/api/v1/questions', methods=['POST'])
    def add_question():
        AddedQuestion = Questions.append(request.get_json())
        return jsonify(AddedQuestion)

    @app.route('/questions/id/answers', methods=['POST'])
    def add_answer():
        if 'id' in request.args:
            id = int(request.args['id'])

        Answers = []

        for Question in Questions:
            if Question['id'] == id:
                AddedAnswer = Answers.append(request.get_json())
                return jsonify(Answers)
            else:
                return"No such question"


app.run(debug=True)    































