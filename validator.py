class Validation:
    def validate_question_is_string(self, question):
        if question.isdigit() is False:
            return True
        else:
            return False

    def validate_question_is_alphabetic(self, question):
        if question.isalpha() is True:
            return True
        else:
            return False

    def validate_question_is_alphanumerical(self, question):
        if question.isalnum() is True:
            return True
        else:
            return False

    def validate_all_questions_returns_list(self, questions):
        check_questions = isinstance(questions, list)
        if check_questions is True:
            return True
        else:
            return False

    def validate_one_question_returns_dictionary(self, question):
        check_question = isinstance(question, dict)
        if check_question is True:
            return True
        else:
            return False

    def validate_answer_is_string(self, answer):
        if answer.isdigit() is False:
            return True
        else:
            return False

    def validate_answer_is_alphabetic(self, answer):
        if answer.isalpha() is True:
            return True
        else:
            return False

    def validate_answer_is_alphanumerical(self, answer):
        if answer.isalnum() is True:
            return True
        else:
            return False
