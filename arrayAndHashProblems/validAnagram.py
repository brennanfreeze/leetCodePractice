'''
Valid Anagram (easy)
Given two strings s and t, return true if t is an anagram of s, and false 
otherwise. An Anagram is a word or phrase 
formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.


'''

'''
Possible Solution: Brute Force
Time Complexity: O(n^2)
Space Complexity: O(1)

Brute Force method, count up all the occurances of the same occurance of the 
letter in s, then do so for string t. If the two counts are not the same return
false.
'''

def BruteForce(s: str, t: str):

    if (len(s) != len(t)):

        return False
    
    for i in range(len(s)):

        count_i = 0

        for j in range(len(s)):

            if (s[j] == s[i]):

                count_i += 1

        count_j = 0

        for j in range(len(t)):

            if (t[j] == s[i]):

                count_j += 1

        if (count_j != count_i):

            return False
        
    return True

'''
Possible Solution: Brute Force and hash map

Time Complexity: O(n^2)
Space Complexity: O(n)

Set a hash map to only one of the strings and store all the values. Then,
use two for loops to iterate each iteration found in each of the hash map keys
and two then count the number of times it is encountered in string t. If the 
count in the hash table and the count for the string t encounters are not the 
same, return false. If the loop ends, return true.
'''

def BruteForceHashMap(s: str, t: str):

    if len(s) != len(t):

        return False
    
    d = {}

    for i in range(len(s)):

        d[s[i]] = 1 + d.get(s[i], 0)

    for c in d:

        count = 0

        for j in range(len(t)):

            if (c == t[j]):

                count += 1

        if d[c] != count:
            return False
        
    return True


'''
Possible Solution: Hash map for both strings

Time Complexity: O(n)
Space Complexity: O(n)

Take two hash empty hash tables and fill them with the characters it encounters
and the value of those to be incremented on each occurance of the key found
within the strings, if they do not have the same values, then you can return
false, else return true.
'''

def TwoHashTables(s: str, t: str):

    if (len(s) != len(t)):

        return False
    
    hashs = {}

    hasht = {}

    for i in range(len(s)):

        hashs[s[i]] = 1 + hashs.get(s[i], 0)

        hasht[t[i]] = 1 + hasht.get(t[i], 0)

    for c in hashs:

        if hashs[c] != hasht[c]:

            return False
        
    return True