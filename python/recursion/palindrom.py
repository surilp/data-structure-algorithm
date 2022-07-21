def palindrome(string: str, idx=0) -> bool:
    if idx < len(string) // 2:
        if string[idx] == string[len(string) - 1 - idx]:
            return palindrome(string, idx + 1)
        else:
            return False
    return True


print(palindrome('madams'))
