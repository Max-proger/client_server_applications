import os
import sys
import unittest

sys.path.append(os.path.join(os.getcwd(), ".."))
from client import create_presence, process_ans
from common.variables import (
    ACCOUNT_NAME,
    ACTION,
    ERROR,
    PRESENCE,
    RESPONSE,
    TIME,
    USER,
)


class TestClass(unittest.TestCase):
    def test_def_presense(self):
        """Тест коректного запроса"""
        test = create_presence()
        test[TIME] = 1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1, USER: {ACCOUNT_NAME: "Guest"}})

    def test_200_ans(self):
        """Тест корректтного разбора ответа 200"""
        self.assertEqual(process_ans({RESPONSE: 200}), "200 : OK")

    def test_400_ans(self):
        """Тест корректного разбора 400"""
        self.assertEqual(
            process_ans({RESPONSE: 400, ERROR: "Bad Request"}),
            "400 : Bad Request",
        )

    def test_no_response(self):
        """Тест исключения без поля RESPONSE"""
        self.assertRaises(ValueError, process_ans, {ERROR: "Bad Request"})


if __name__ == "__main__":
    unittest.main()
