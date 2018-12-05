import pyEX as p


def peerCorrelation(symbol, timeframe='6m'):
    peers = p.peers(symbol)
    rets = p.batchDF(peers + [symbol], 'chart', timeframe)['chart']
    ret = rets.pivot(columns='KEY', values='changePercent').corr()
    ret.index.name = 'symbol'
    ret.columns = ret.columns.tolist()
    return ret
