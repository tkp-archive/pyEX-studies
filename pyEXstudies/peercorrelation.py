import pyEX as p
# from temporalcache import expire


# @expire(hour=16)
def peerCorrelation(symbol, timeframe='6m'):
    peers = p.peers(symbol)
    rets = p.batchDF(peers + [symbol], 'chart', timeframe)['chart']
    ret = rets.pivot(columns='symbol', values='changePercent').corr()
    ret.index.name = 'symbol'
    ret.columns = ret.columns.tolist()
    return ret
