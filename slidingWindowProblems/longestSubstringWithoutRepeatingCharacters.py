'''
Given a string s, find the length of the longest substring without repeating 
characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a 
substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

'''
Possible Solution: Brute Force
Time Complexity: O(n^2)
Space complexity: O(n)

If the length of s is equal to 0, then return 0. Set a max length value to 1 and
a value of i to 0. With i being in range of the length of s, set j to i + 1,
count to 1, and a temp set with the current value at index i. While j is in 
range of length of s, the value at index j is not equal to the value at index
i, and the value at index j is not in the set, add s[j] to the set, increase the
count, and increment j by 1. When this while loop ends, increment i by 1 and find
the max between ma and count.

As this algorithm repeats values but starts at a range smaller each time for the
inner for loop represented by j, the time complexity of this algorithm is 
O(n^2 / 2) and the space complexity is O(n) for using the set.
'''

def BruteForce(s: str):

    if (len(s) == 0):

        return 0
    
    ma = 1

    i = 0

    while i < len(s):

        j = i + 1

        count = 1

        se = set()

        se.add(s[i])

        while j < len(s) and s[j] != s[i] and s[j] not in se:

            se.add(s[j])

            count += 1

            j += 1

        i += 1

        ma = max(ma, count)

    return ma

'''
Possible Solution: Sliding Window
Time complexity: O(n)
Space complexity: O(n)

Create a set, a left pointer, and a max value to return after the for loop. With
r in range of the length of s, start a while loop if the value at index r is in
the set, representing that there has been indeed an identical character found.
Remove the characters at index l and increment it by 1 until the character at
index r is not in the set. After this, add the character at index r to the set
to start the process again and determine ma by the max of its current value and
the difference of r and l plus one. This is used to determine the string length
and it is possible to use the set length + 1 for this. Finally, return the value
stores in ma.

As this algorithm is only bounded by the length of s with no repeated indices in
the string, the time complexity is O(n) and the space complexity is O(n) for the
usage of the set.
'''

def SlidingWindow(s: str):

    se = set()

    l = 0

    ma = 0

    for r in range(len(s)):

        while s[r] in se:

            se.remove(s[l])

            l += 1

        se.add(s[r])

        ma = max(ma, r - l + 1)

    return ma
