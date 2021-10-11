"""
Write a function shuffle(l1,l2) that takes as input two lists, 11 and l2, and returns a list consisting of the first
elment in l1, then the first element in l2, then the second element in l2, then the second element in l2, and so on.
If the two lists are not of equal length, the remaining elements of the longer list are appended at the end of the shuffled output.

Here are some examples to show how your function should work.
shuffle([0,2,4],[1,3,5])
[0, 1, 2, 3, 4, 5]
shuffle([0,2,4],[1])
[0, 1, 2, 4]
shuffle([0],[1,3,5])
[0, 1, 3, 5]
"""

def shuffle(l1, l2):
    res = []
    len1 = len(l1)
    len2 = len(l2)
    if len1 == len2:
        for i in range(len1):
            res.append(l1[i])
            res.append(l2[i])
    elif len1 > len2:
        for i in range(len2):
            res.append(l1[i])
            res.append(l2[i])
        for i in range(len2, len1):
            res.append(l1[i])
    else:
        for i in range(len1):
            res.append(l1[i])
            res.append(l2[i])
        for i in range(len1, len2):
            res.append(l2[i])
    return res

print(shuffle([0,2,4],[1,3,5]))
print(shuffle([0,2,4],[1]))
print(shuffle([0],[1,3,5]))
