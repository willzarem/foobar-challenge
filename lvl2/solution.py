import re
def answer(l):
    # Used this answer as a reference http://stackoverflow.com/a/13980081 but replaced the numerical comparison with a version comparison (minro_v)
    # sorry for  the weird statements, i'm still learning Python
    def swap(i, j):
        sqc[i], sqc[j] = sqc[j], sqc[i]

    def heapify(end,i):
        l = 2 * i + 1
        r = 2 * (i + 1)
        max = i
        if l < end and minor_v(sqc[i], sqc[l]):
            max = l
        if r < end and minor_v(sqc[max], sqc[r]):
            max = r
        if max != i:
            swap(i, max)
            heapify(end, max)


    def heap_sort():
        end = len(sqc)
        start = end // 2 - 1
        for i in range(start, -1, -1):
            heapify(end, i)
        for i in range(end-1, 0, -1):
            swap(i, 0)
            heapify(i, 0)

    def minor_v(e1, e2):
        # e1 = a.b.c
        # e2 = x.y.z
        e1_l = re.split('\.', e1)
        e2_l = re.split('\.', e2)
        if (not len(e1_l) or not len(e2_l)):
            print('empty string found')
            return None
        if e1_l[0] != e2_l[0]:
            # a != x
            return int(e1_l[0]) < int(e2_l[0])
        else:
            # a == x
            if len(e1_l) >= 2 and len(e2_l) >= 2:
                if e1_l[1] != e2_l[1]:
                    # b != y
                    return int(e1_l[1]) < int(e2_l[1])
                else:
                    # b == y
                    if len(e1_l) == 3 and len(e2_l) == 3:
                        return int(e1_l[2]) < int(e2_l[2])
                    else: 
                        return len(e1_l) < len(e2_l)
            else:
                return len(e1_l) < len(e2_l)
    sqc = l
    heap_sort()
    return sqc

print(answer(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))