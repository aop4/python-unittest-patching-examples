import unittest
from unittest.mock import Mock, patch

class Foo:
    def say_introduction(self):
        return 'Hello, I am ' + self.get_name()

    def get_name(self):
        return 'Spam'

class WrapsTest(unittest.TestCase):
    def test_wraps_argument_for_patch(self):
        foo = Foo()
        with patch.object(Foo, 'get_name', wraps=foo.get_name) as get_name:
            result = foo.say_introduction()
            self.assertEqual('Hello, I am Spam', result)
            get_name.assert_called_once()

    def test_wraps_argument_for_mock(self):
        # you might think that the below approach works the same way, but it doesn't
        mock_foo = Mock(wraps=Foo())
        # the mock will record a direct call to get_name()
        mock_foo.get_name()
        # but it doesn't record it when method is called indirectly
        mock_foo.say_introduction()
        # so the internal method call in say_introduction isn't recorded
        # and there is one call registered instead of 2
        self.assertEqual(1, mock_foo.get_name.call_count)
