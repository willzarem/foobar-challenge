import sys
import re
def answer(s):
    salutes = 0
    for i, direction in enumerate(s):
        if direction == '>':
            his = re.findall('<', s[i:])
            salutes += len(his) * 2
    return salutes

if __name__ == "__main__":
    print(answer('>>>-<<<'))