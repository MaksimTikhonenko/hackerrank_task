

def solve(s):
    if not isinstance(s, str):
        return None

    result = ''
    for word in s.split(' '):
        for idx in range(0, len(word)):

            if idx == 0:
                result += word[idx].upper()
            else:
                result += word[idx]
        result += ' '
    return result[:-1]
