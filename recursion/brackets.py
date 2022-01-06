def brackets(n):
    result = []
    _brackets(n, 0, 0, [], result)
    return result

def _brackets(n, open, close, ds, result):
    print(open, close, ds, result)
    if len(ds) == n * 2:
        result.append(''.join(ds))
        return

    if open < n:
        ds.append('<')
        _brackets(n, open + 1, close, ds, result)
        ds.pop()

    if close < open:
        ds.append('>')
        _brackets(n, open, close + 1, ds, result)
        ds.pop()

print(brackets(2))