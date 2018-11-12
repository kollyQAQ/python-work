# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if L == []:
        return (None, None)
    min = max = L[0]
    for x in L:
        if min > x:
            min = x
        if max < x:
            max = x
    return (min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
