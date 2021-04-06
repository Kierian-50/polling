import unittest

from polling import Polling


class TestPoll(unittest.TestCase):

    def test_import(self):
        """Test that you can import via correct usage"""
        import polling
        from polling import Polling

        assert Polling
        assert polling

    def test_arg_validation(self):
        """Tests various permutations of calling with invalid args"""

        # No function
        try:
            Polling.poll()
        except TypeError:
            pass
        else:
            assert False, 'No error raised with no args'

        try:
            Polling.poll(lambda: True)
        except TypeError:
            pass
        else:
            assert False, 'No error raised with no step'

        try:
            Polling.poll(lambda: True)
        except AssertionError:
            pass
        else:
            assert False, 'No error raised without specifying poll_forever or a timeout/max_tries'

        try:
            Polling.poll(lambda: True, poll_forever=True)
        except AssertionError:
            pass
        else:
            assert False, 'No error raised when specifying poll_forever with timeout/max_tries'
