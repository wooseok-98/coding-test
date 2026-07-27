def solution(s, n):
    result = []

    for c in s:
        if c == ' ':
            result.append(c)
        elif c.islower():
            result.append(chr((ord(c) - ord('a') + n) % 26 + ord('a')))
        else:
            result.append(chr((ord(c) - ord('A') + n) % 26 + ord('A')))

    return ''.join(result)