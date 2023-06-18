'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

'''
Possible Solution: Brute Force

'''


def BruteForce(s):
    s_valid = [False] * len(s)
    i = 0
    while i < len(s):
        for j in range(len(s) - 1, i, -1):
            if (s[i] == '(' and s[j] == ')' and not s_valid[i] and not s_valid[j]):
                s_valid[i] = True
                s_valid[j] = True
                break
                
        i += 1

    for i in s_valid:

        if not i:

            return False
        
    return True

BruteForce("(]")
