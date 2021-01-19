from unittest import TestCase

from gender_test import gender_test1

class Test(TestCase):
    def test_gender_test_when_male(self):
        actual = gender_test1("M")
        expected = "MALE"
        self.assertEqual(actual, expected)

    def test_gender_test_when_female(self):
        actual = gender_test1("F")
        expected = "FEMALE"
        self.assertEqual(actual, expected)

    def test_gender_test_when_unknown(self):
        actual = gender_test1("Hello")
        expected = "UNKNOWN_GENDER"
        self.assertEqual(actual, expected)