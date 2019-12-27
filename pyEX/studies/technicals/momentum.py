# -*- coding: utf-8 -*-
import talib as t
import pandas as pd


def rsi(client, symbol, timeframe='6m', col='close', period=14):
    '''This will return a dataframe of rsi for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    rs = t.RSI(df[col].values, period)
    return pd.DataFrame({col: df[col].values, 'rsi': rs})
