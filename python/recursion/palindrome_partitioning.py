def partitioning(word):
    result = []
    _partitioning(0, word, [], result)
    return result

def _partitioning(start, word, ds, result):
    if start == len(word):
        result.append(list(ds))
        return

    for partition_end in range(start, len(word)):
        if _is_palindrome(word, start, partition_end):
            ds.append(word[start:partition_end + 1])
            _partitioning(partition_end + 1, word, ds, result)
            ds.pop()


def _is_palindrome(word, start, end):
    while start < end:
        if word[start] == word[end]:
            start +=1
            end -=1
        else:
            return False
    return True

print(partitioning('aabb'))