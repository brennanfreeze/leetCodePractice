"""
139. Word Break (medium)


Given a string s and a dictionary of strings wordDict, return true if s can be 
segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the 
segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as 
"apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""

"""
Possible Solution: Bottom Up Dynamic Programming

Create a bottom up memoization array that is 1 longer than the inputted string
s. This will confirm that all characters have been seen and the values in 
wordDict can be inputted in every value if this is true. Going backwards in the
array, this will allow the memorization of all values and is similar in nature
to the coin change problem, just using the subtraction of values with substrings.
within range of the word dictionary given, determine if i + the length of the
current word being looked at is a possible substring of s and if this range
is equal to the current word. If so, then it is known that this is a substring 
of s and can be inputted in the array d that this has been seen at length i
from length i + length of w. if this value is true, then we know that there is
no need to continue the loop, as it will add extra average runtime so break the
inner for loop. Finally, return the first index of the d array. 

As this relies on a correlated array to keep track of substring placements found
in the array and there is a inner independent for loop of the main for loop in
bounds of the length of s, the runtime complexity is going to be O(n * m) and
the space complexity is going to be O(n). It must be noted that extra additions
to runtime time and space complexity could be added to this due to heavy usage 
of the functionalities in python, so optimization of those can improve this.
"""

def DynamicProgramming(s: str, wordDict) -> bool:
  
  d = [False] * (len(s) + 1)
  
  d[len(s)] = True
  
  for i in range(len(s) - 1, -1, -1):
    
    for w in wordDict:
      
      if i + len(w) <= len(s) and s[i:i + len(w)] == w:
        
        d[i] = d[i + len(w)]
        
      if d[i]:
        
        break
      
  return d[0]
  