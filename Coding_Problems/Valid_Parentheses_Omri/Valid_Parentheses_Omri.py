def isValid(self, s):
    open_to_close = {'(': ')', '[': ']', '{': '}'}
    closers = ")]}"
    expected = []
    for l in s:
        if l in closers:
            if expected and expected[len(expected) - 1] == l:
                expected.pop()
            else:
                return False
        else:
            expected.append(open_to_close[l])
    return not expected
