import talib as t
import pyEX as p
import pandas as pd


def rsi(symbol, timeframe='6m', col='close', period=14):
    df = p.chartDF(symbol, timeframe)
    rs = t.RSI(df[col].values, period)
    return pd.DataFrame({col: df[col].values, 'rsi': rs})
