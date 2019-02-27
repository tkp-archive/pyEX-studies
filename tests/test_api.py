# for Coverage
import time
from mock import patch, MagicMock

C = 'AAPL'


class TestAPI:
    def setup(self):
        time.sleep(1)

    def teardown(self):
        pass

    def test_peercorrelation(self):
        from pyEXstudies import peerCorrelation
        peerCorrelation(C, '6m')

    def test_bollinger(self):
        from pyEXstudies import bollinger
        bollinger(C, '6m')

    def test_emasma(self):
        from pyEXstudies import ema, sma, dema
        ema(C)
        ema(C, periods=30)
        ema(C, periods=[30, 45])
        dema(C)
        dema(C, periods=30)
        dema(C, periods=[30, 45])
        sma(C)
        sma(C, periods=30)
        sma(C, periods=[30, 45])

    def test_sar(self):
        from pyEXstudies import sar
        sar(C)

    def test_rsi(self):
        from pyEXstudies import rsi
        rsi(C)
