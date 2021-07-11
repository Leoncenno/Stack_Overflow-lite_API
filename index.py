from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

questions = [
    {'id': 0,
     'name': 'Leo',
     'question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn',
     'answer': ''},
    {'id': 1,
     'name': 'Odongo',
     'question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn',
     'answer': ''},
    {'id': 2,
     'name': 'Okello',
     'question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn',
     'answer': ''},
    {'id': 3,
     'name': 'Opio',
     'question': 'mahsfhduujhws anshdshdhj akjsjdiinasksk nmjsbhhjjskknms  sbbhbhsjhjdsn',
     'answer': ''},
]


@app.route('/api/v1/questions')
def all_questions():
    return jsonify(questions)


@app.route('/api/v1/questions/<id>')
def one_question(id):
    for question in questions:
        if question['id'] == int(id):
            return jsonify(question)
    
    return jsonify({'message': f'No question with id {id}'}), 404


@app.route('/api/v1/questions', methods=['POST'])
def add_question():
    number_of_questions = len(questions)
    question_to_add = request.get_json()
    question_to_add['id'] = number_of_questions
    questions.append(request.get_json())
    return jsonify(question_to_add), 201


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
