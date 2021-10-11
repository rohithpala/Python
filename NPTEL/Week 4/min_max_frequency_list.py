"""
Write a Python function frequency(l) that takes as input a list of integers and returns a pair of the form
(min_freq_list,max_freq_list) where
min_freq_list is a list of numbers with minimum frequency in l, sorted in ascending order
max_freq_list is a list of numbers with maximum frequency in l, sorted in ascending order

Here are some examples of how your function should work.
frequency([13,12,11,13,14,13,7,11,13,14,12]): ([7], [13])
frequency([13,12,11,13,14,13,7,11,13,14,12,14,14]): ([7], [13, 14])
frequency([13,12,11,13,14,13,7,11,13,14,12,14,14,7]): ([7, 11, 12], [13, 14])
"""

def min_max_frequency_list(lst):
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    minimum, maximum = min(freq.values()), max(freq.values())
    min_freq_list = []
    max_freq_list = []
    for key in freq.keys():
        if freq[key] == minimum:
            min_freq_list.append(key)
        if freq[key] == maximum:
            max_freq_list.append(key)
    res = (sorted(min_freq_list), sorted(max_freq_list))
    return res

print(min_max_frequency_list([13,12,13,14,11,13,7,11,13,14,12]))
print(min_max_frequency_list([13,12,11,13,14,13,7,11,13,14,12,14,14]))
print(min_max_frequency_list([13,12,11,13,14,13,7,11,13,14,12,14,14,7]))
print(min_max_frequency_list([17322,271898,374,374,374,423432423,423432423,423432423,423432423,5325,5325,5325,5325,5325]))
