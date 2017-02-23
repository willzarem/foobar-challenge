import sys

def test(s):
    count = 0
    if len(s) == 1:
        return 1
    ss = ""
    while len(ss) <= len(s)//2:
        ss = s[0:len(ss) + 1]
        m = s.count(ss)
        if m * len(ss) == len(s):
            return m
    return 1
print(test(sys.argv[1]))