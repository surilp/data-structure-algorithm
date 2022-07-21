def valid_discount(discounts):
    result = []
    for discount in discounts:
        if _valid_discount(discount, 0, len(discount) - 1):
            result.append(1)
        else:
            result.append(0)
    return result


def _valid_discount(discount, start, end):
    if end == start:
        return False
    if start > end:
        return True
    if discount[start] == discount[end]:
        return _valid_discount(discount, start + 1, end - 1)
    else:
        mid = (start + end) // 2
        if _valid_discount(discount, start, mid) and _valid_discount(discount, mid + 1, end):
            return True
        else:
            return False


def _same(discount, start1, end1, start2, end2):
    if end1 - start1 != end2 - start2:
        return False
    while start1 < end1 + 1:
        if discount[start1] == discount[start2]:
            start1 += 1
            start2 += 1
        else:
            return False
    return True


discounts = ['abba','abca', 'daabbd', 'dacbad']
print(valid_discount(discounts))