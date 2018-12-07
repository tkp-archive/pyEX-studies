import talib as t
import pyEX as p
import pandas as pd


def bollinger(symbol, timeframe='6m', col='close'):
    df = p.chartDF(symbol, timeframe)
    bb = t.BBANDS(df[col].values)
    return pd.DataFrame({'upper': bb[0], 'middle': bb[1], 'lower': bb[2]})
