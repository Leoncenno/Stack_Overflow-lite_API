from flask import Flask, request, jsonify, json

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


@app.route('/api/v1/question/<id>')
def one_question(id):
    if 'id' in request.args:
        id = int(request.args['id'])
    for question in questions:
        if question['id'] == int(id):
            return jsonify(question)
    else:
        return jsonify({'warning': 'Invalid question ID'}), 404


@app.route('/api/v1/questions', methods=['POST'])
def post_question():
    new_question = request.json
    qn = new_question['question']
    number_of_questions = len(questions)
    id = int(number_of_questions)
    print(qn)
    questions.append({'id': id, 'question': qn, 'answers': [{'answer': ''}]})
    return jsonify(questions), 201


@app.route('/api/v1/questions/<id>/answers', methods=['POST'])
def post_answer(id):
    if 'id' in request.args:
        id = int(request.args['id'])
    for question in questions:
        if question['id'] == int(id):
            question = question['question']
            new_answer = request.json
            ans = new_answer
            questions.append(
                {'id': id, 'question': question, 'answers': [{'answer': ans['answer']}]})
    return jsonify(questions)


app.run(debug=True)
