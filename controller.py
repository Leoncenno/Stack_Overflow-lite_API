from index import app
from views import questions
from flask import request, jsonify, json
from validator import Validation


validation = Validation()


@app.route('/api/v1/questions')
def all_questions():
    return_questions = validation.validate_all_questions_returns_list(
        questions)
    if return_questions:
        return jsonify(questions), 200
    else:
        return ('Wrong questions format'), 404


@app.route('/api/v1/question/<id>')
def one_question(id):
    if 'id' in request.args:
        id = int(request.args['id'])
    for question in questions:
        check_question = validation.validate_one_question_returns_dictionary(
            question)
        if check_question and (question['id'] == int(id)):
            return jsonify(question), 200
    else:
        return jsonify({'warning': 'Invalid question ID, bad request'}), 404


@app.route('/api/v1/questions', methods=['POST'])
def post_question():
    question = request.json
    qn = question['question']
    post_in = validation.validate_question_is_string(qn)
    alphabet = validation.validate_question_is_alphabetic(qn)
    alphanum = validation.validate_question_is_alphanumerical(qn)
    number_of_questions = len(questions)
    id = int(number_of_questions)
    if post_in or (alphabet and alphanum):
        questions.append({'id': id, 'question': qn.strip(),
                         'answers': [{'answer': ''}]})
        return jsonify(questions), 201
    else:
        return ('Wrong question formart, enter string'), 400


@app.route('/api/v1/questions/<id>/answers', methods=['POST'])
def post_answer(id):
    if 'id' in request.args:
        id = int(request.args['id'])
    for question in questions:
        if question['id'] == int(id):
            question = question['question']
            new_answer = request.json
            ans = new_answer['answer']
    answer_string = validation.validate_answer_is_string(ans)
    answer_alphabetic = validation.validate_answer_is_alphabetic(ans)
    answer_alphanum = validation.validate_answer_is_alphanumerical(ans)
    if answer_string or (answer_alphabetic and answer_alphanum):
        questions.append(
            {'id': id, 'question': question, 'answers': [{'answer': ans.strip()}]})
        return jsonify(questions), 201
    else:
        return ('Wrong answer formart, enter string'), 400
