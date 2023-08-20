"""
5. Longest Palindromic Substring (medium)
Given a string s, return the longest palindromic substring in s.


Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

"""
Possible Solution: inside out  
"""

def InsideOut(s: str) -> str:
  
  if len(s) == 1:
    
    return s[0]
  
  ma_l = 0
  
  ma_r = 0
  
  for i in range(len(s)):
    
    l,r = i, i
    
    while l >= 0 and r < len(s) and s[l] == s[r]:
      
      if (r - l + 1) > (ma_r - ma_l + 1):
        
        ma_r = r
        
        ma_l = l
        
      l -= 1
      
      r += 1
      
    l,r = i, i + 1
    
    while l >= 0 and r < len(s) and s[l] == s[r]:
      
      if (r - l + 1) > (ma_r - ma_l + 1):
        
        ma_r = r
        
        ma_l = l
        
      l -= 1
      
      r += 1
      
    return s[ma_l: ma_r + 1]