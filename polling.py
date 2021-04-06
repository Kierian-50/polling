"""Polling module containing all exceptions and helpers used for the polling function"""

__version__ = '0.3.1'

try:
    from Queue import Queue
except ImportError:
    from queue import Queue


class Polling:
    """Class that allows to have a class attribute to stop the poll method"""

    def __init__(self):
        """Constructor that initializes the attribute which will be used to stop the polling"""
        self.stop = False

    def poll(self, target, args=(), kwargs=None, ignore_exceptions=(), poll_forever=True, *a, **k):
        """Poll by calling a target function until a certain condition is met. You must specify at least a target
        function to be called and the step -- base wait time between each function call.

        :param args: Arguments to be passed to the target function
        :type kwargs: dict
        :param kwargs: Keyword arguments to be passed to the target function
        :type ignore_exceptions: tuple
        :param ignore_exceptions: You can specify a tuple of exceptions that should be caught and ignored on every
        iteration. If the target function raises one of these exceptions, it will be caught and the exception
        instance will be pushed to the queue of values collected during polling. Any other exceptions raised will be
        raised as normal.
        :param poll_forever: If set to true, this function will retry until an exception is raised or the target's
        return value satisfies the check_success function. If this is not set, then a timeout or a max_tries must be set.

        I rewrite this function to be simple as possible and to befully connected to my need of reading the ttys0 file
        and it will be able to stop the polling when I want and not with a timeout.
        """

        kwargs = kwargs or dict()

        while not self.stop:
            try:
                target(*args, **kwargs)
            except ignore_exceptions as e:
                pass
