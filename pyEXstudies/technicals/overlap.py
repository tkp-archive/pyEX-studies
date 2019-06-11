import talib as t
import pandas as pd
from ..utils import tolist


def bollinger(client, symbol, timeframe='6m', col='close', period=2):
    df = client.chartDF(symbol, timeframe)
    bb = t.BBANDS(df[col].values, period)
    return pd.DataFrame({col: df[col].values, 'upper': bb[0], 'middle': bb[1], 'lower': bb[2]})


def dema(client, symbol, timeframe='6m', col='close', periods=None):
    if periods is None:
        periods = [30]
    periods = tolist(periods)

    df = client.chartDF(symbol, timeframe)

    build = {col: df[col].values}
    for per in periods:
        build['ema-{}'.format(per)] = t.DEMA(df[col].values, per)
    return pd.DataFrame(build)


def ema(client, symbol, timeframe='6m', col='close', periods=None):
    if periods is None:
        periods = [30]
    periods = tolist(periods)

    df = client.chartDF(symbol, timeframe)

    build = {col: df[col].values}
    for per in periods:
        build['ema-{}'.format(per)] = t.EMA(df[col].values, per)
    return pd.DataFrame(build)


def sar(client, symbol, timeframe='6m', highcol='high', lowcol='low'):
    df = client.chartDF(symbol, timeframe)
    sar = t.SAR(df[highcol].values, df[lowcol].values)
    return pd.DataFrame({highcol: df[highcol].values, lowcol: df[lowcol].values, 'sar': sar})


def sma(client, symbol, timeframe='6m', col='close', periods=None):
    if periods is None:
        periods = [30]
    periods = tolist(periods)

    df = client.chartDF(symbol, timeframe)

    build = {col: df[col].values}
    for per in periods:
        build['sma-{}'.format(per)] = t.EMA(df[col].values, per)
    return pd.DataFrame(build)
