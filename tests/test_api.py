# for Coverage
import time
from mock import patch, MagicMock

C = MagicMock()
S = 'AAPL'


class TestAPI:
    def setup(self):
        time.sleep(1)

    def teardown(self):
        pass

    def test_peercorrelation(self):
        from pyEXstudies import peerCorrelation
        peerCorrelation(C, S, '6m')

    def test_bollinger(self):
        from pyEXstudies import bollinger
        bollinger(C, S, '6m')

    def test_emasma(self):
        from pyEXstudies import ema, sma, dema
        ema(C, S)
        ema(C, S, periods=30)
        ema(C, S, periods=[30, 45])
        dema(C, S)
        dema(C, S, periods=30)
        dema(C, S, periods=[30, 45])
        sma(C, S)
        sma(C, S, periods=30)
        sma(C, S, periods=[30, 45])

    def test_sar(self):
        from pyEXstudies import sar
        sar(C, S)

    def test_rsi(self):
        from pyEXstudies import rsi
        rsi(C, S)
