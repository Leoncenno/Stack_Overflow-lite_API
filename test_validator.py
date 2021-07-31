import unittest
from validator import Validation


class TestValidation(unittest.TestCase):
    def setUp(self):
        self.val = Validation()

    def test_validate_question_is_string(self):
        self.assertTrue(
            'This is me', self.val.validate_question_is_string('This me'))

    def test_validate_question_is_alphabetic(self):
        self.assertTrue(
            'werty', self.val.validate_question_is_alphabetic(';lkjhgfd'))

    def test_validate_question_is_alphanumerical(self):
        self.assertTrue(
            'werty234', self.val.validate_question_is_alphanumerical(';876lkjh'))

    def test_validate_all_questions_returns_list(self):
        self.assertTrue(
            [2, 3, 4], self.val.validate_all_questions_returns_list(['peter', 'tom']))

    def test_validate_one_question_returns_dictionary(self):
        self.assertTrue(
            {'man': 'Down'}, self.val.validate_one_question_returns_dictionary({'key': 'true'}))

    def test_validate_answer_is_string(self):
        self.assertTrue(
            'This is me', self.val.validate_answer_is_string('This one me'))

    def test_validate_answer_is_alphabetic(self):
        self.assertTrue(
            'This', self.val.validate_answer_is_alphabetic('Thisoneme'))

    def test_validate_answer_is_alphanumerical(self):
        self.assertTrue(
            'This98765', self.val.validate_answer_is_alphanumerical('23456Thisoneme'))


if __name__ == '__main__':
    unittest.main()
