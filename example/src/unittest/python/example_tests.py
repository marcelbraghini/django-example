from mockito import mock, verify
import unittest

from example import example

class exampleTest(unittest.TestCase):
    def test_should_issue_example_message(self):
        out = mock()

        example(out)

        verify(out).write("Python")