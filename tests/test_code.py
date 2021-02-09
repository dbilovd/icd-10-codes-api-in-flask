import unittest
from app.models.code import Code


class CodeUnitTest(unittest.TestCase):

    def test_a_code_with_a_parent_returns_an_joined_code(self):
        parent_code = Code(code="A123", title="Parent Title")
        code = Code(code="456", title="Child Title", parent_code=parent_code)

        self.assertEqual(code.full_code(), "A123456")

    def test_a_code_with_a_parent_returns_an_joined_title(self):
        parent_code = Code(code="A123", title="Parent Title")
        code = Code(code="456", title="Child Title", parent_code=parent_code)

        self.assertEqual(code.full_title(), "Parent Title, Child Title")
