'''
Group Anagrams (medium)

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of 
a different word or phrase,  typically using all the original letters 
exactly once.
'''

'''
Possible Solution: Brute Force

Time Complexity: O(m * nlogn)
Space Complexity: O(n + k)

Create an empty array and an empty set. First, go through the array and sort 
every value and add each sorted value to the set so it takes every unique
variation in the strs input. in another for loop, append empty arrays to the res
based on the length of the set, and convert the compare_res set to a list
Finally, in a final for loop take the index of where the sorted string is in the
converted set array and add it to the res array in a 2d array system. 

This is a highly inefficient method as given the length of each string in the 
input array can be any length, call this length m and the need to sort each 
string, call this nlogn (assuming quick sort with random pivot enabled). This 
means the algorithm runtime will be m * nlogn. The space complexity with the 
extra set is n and the length of each string can be at any length, call this k.
The space complexity will therefore be: O(n + k) (it is n + k instead of n * k
as these two variables are independent of each other and do not determine one
another technically.)
'''

def BruteForce(strs):

    res = [] # n

    compare_res = set() # n

    for i in range(len(strs)): # n

        temp_sorted = sorted(strs[i]) #nlogn

        compare_res.add("".join(temp_sorted)) # n

    for _ in range(len(compare_res)):

        res.append([])

    compare_res = list(compare_res)

    for i in range(len(strs)): # n
        # nlogn n 
        res[compare_res.index("".join(sorted(strs[i])))].append(strs[i])

    return res

'''
Possible Solition: Hash Map and encoding chars

Time Complexity: O(m * n)
Space Complexity: O(n)

Set a default dictionary to have the keys be lists. In each value in strs,
create a count array with a constant size of 26 for each character in the 
alphabet. For each character in a looked at ASCII value of the character minus
the ASCII value for 'a' (80) to get a index value within 0 - 26 (b - a = 1, 
c - a = 2, etc.). Take the count list and set it as a tuple to be added to the 
res hash map with the current word being looked to be appended to the value
array. Finally as we only need the values in the dictionary for the return, 
simple return those values inside of a list.

Given the amount of words within strs, call this n and the length of each word,
call this m will be O(n * m) as they are dependent within the loop itself.
Space complexity wise is technically the same as O(n * m), however it is 
technically O(n * m * 26) for the length of count array, however it is a 
constant so it is not accounted for.
'''

from collections import defaultdict

def HashMapEncode(strs):

    res = defaultdict(list)
    
    for i in range(len(strs)):

        count = [0] * 26

        for c in strs[i]:

            count[ord(c) - ord('a')] += 1

        res[tuple(count)].append(strs[i])

    return list(res.values())

