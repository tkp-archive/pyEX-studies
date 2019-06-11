import talib as t
import pandas as pd


def rsi(client, symbol, timeframe='6m', col='close', period=14):
    df = client.chartDF(symbol, timeframe)
    rs = t.RSI(df[col].values, period)
    return pd.DataFrame({col: df[col].values, 'rsi': rs})
