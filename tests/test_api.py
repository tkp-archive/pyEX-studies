# for Coverage
from mock import patch, MagicMock

C = 'AAPL'


class TestAPI:
    def setup(self):
        pass
        # setup() before each test method

    def teardown(self):
        pass
        # teardown() after each test method

    @classmethod
    def setup_class(cls):
        pass
        # setup_class() before any methods in this class

    @classmethod
    def teardown_class(cls):
        pass
        # teardown_class() after any methods in this class

    def test_peercorrelation(self):
        from pyEXstudies import peerCorrelation
        peerCorrelation(C, '6m')
