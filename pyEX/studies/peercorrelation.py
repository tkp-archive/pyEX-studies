# -*- coding: utf-8 -*-
# from temporalcache import expire


# @expire(hour=16)
def peerCorrelation(client, symbol, timeframe='6m'):
    peers = client.peers(symbol)
    rets = client.batchDF(peers + [symbol], 'chart', timeframe)['chart']
    ret = rets.pivot(columns='symbol', values='changePercent').corr()
    ret.index.name = 'symbol'
    ret.columns = ret.columns.tolist()
    return ret
