def wilcard(string):
    result = []
    _wildcard(0, string, [], result)
    return result



def _wildcard(idx, string, ds, result):
    if idx >= len(string):
        result.append(''.join(ds))
        return

    if string[idx] == "?":
        ds.append('1')
        _wildcard(idx + 1, string, ds, result)
        ds.pop()
        ds.append('0')
        _wildcard(idx + 1, string, ds, result)

    else:
        ds.append(string[idx])
        _wildcard(idx + 1, string, ds, result)


print(wilcard('1?1?1'))