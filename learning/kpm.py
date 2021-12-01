# -*- coding: utf-8 -*


p = 'ababaabaabac'
def get_next(x):
    for i in range(x, 0, -1):
        if p[0:i] == p[x-i+1:x+1]:
            return i
    return 0

next = [get_next(x) for x in range(len(p))]

print(p)
print(next)