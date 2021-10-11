"""
An airline has assigned each city that it serves a unique numeric code. It has collected information about all the direct
flights it operates, represented as a list of pairs of the form (i,j), where i is the code of the starting city and j is
the code of the destination. It now wants to compute all pairs of cities connected by one intermediate hope — city i is
connected to city j by one intermediate hop if there are direct flights of the form (i,k) and (k,j) for some other
city k. The airline is only interested in one hop flights between different cities — pairs of the form (i,i) are not useful.
Write a Python function one_hop(l) that takes as input a list of pairs representing direct flights, as described above,
and returns a list of all pairs (i,j), where i != j, such that i and j are connected by one hop. Note that it may already
be the case that there is a direct flight from i to j. So long as there is an intermediate k with a flight from i to k
and from k to j, the list returned by the function should include (i,j). The input list may be in any order. The pairs
in the output list should be in lexicographic (dictionary) order. Each pair should be listed exactly once.

Here are some examples of how your function should work.
one_hop([(2,3),(1,2)]): [(1, 3)]
one_hop([(2,3),(1,2),(3,1),(1,3),(3,2),(2,4),(4,1)]): [(1, 2), (1, 3), (1, 4), (2, 1), (3, 2), (3, 4), (4, 2), (4, 3)]
one_hop([(1,2),(3,4),(5,6)]): []
"""

def one_hop(lst):
    res = []
    for tup in lst:
        for tup1 in lst:
            if tup != tup1 and tup[1] == tup1[0] and tup[0] != tup1[1]:
                t = tuple((tup[0], tup1[1]))
                if t not in res:
                    res.append(t)
    return sorted(res)

print(one_hop([(2,3),(1,2)]))
print(one_hop([(2,3),(1,2),(3,1),(1,3),(3,2),(2,4),(4,1)]))
print(one_hop([(1,2),(3,4),(5,6)]))
