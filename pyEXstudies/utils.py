
def tolist(val):
    try:
        iter(val)
        return val
    except TypeError:
        return [val]
