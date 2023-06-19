'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

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
Time Complexity: O(n^2)
Space Complexity: O(n)

Set a dictionary of values for easier logic set up and a array of boolean values
to see which brackets have been encountered. In range of the length of s, 
determine if the current index is an open parentheses. If so, set a count of 1
and start an inner for loop in range of curr index + 1 to end of string. If it
is an open bracket, count += 1, else count -= 1. The Final step in the main part
is to determine if the close bracket is in values, if the key of that value is
the current found open bracket (open index), both of these two brackets have not
been encountered, and finally if the current count is equal to 0. If all of these
pass then it is a valid formation and set these two indices to be true in s_valid.
Do this for all open bracket. Finally, go through s_valid to determine if there
are any False values in the array, if not return True.

As this algorithm relies on an inner for loop to determine the if there is a 
proper closing in which it can repeat the same iteration multiple times, the 
runtime complexity is O(n^2) and the space complexity is O(n) for the use of
s_valid.
'''


def BruteForce(s):

    values = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    s_valid = [False] * len(s)

    for open in range(len(s)):

        if s[open] not in values:

            count = 1

            for close in range(open + 1, len(s)):

                if s[close] in values: 

                    count -= 1

                if s[close] in values.values():

                    count += 1

                if (s[close] in values and values[s[close]] == s[open] and not s_valid[open] and not s_valid[close] and count == 0):

                    s_valid[open] = True

                    s_valid[close] = True

                    break

    for i in range(len(s_valid)):

        if (not s_valid[i]):

            return False
        
    return True

'''
Possible Solution: Stack
Time Complexity: O(n)
Space Complexity: O(n)

Create an array to act with rules of a stack and set a dictionary of possible 
brackets in the string. within range of the string, determine if the current
index is an open bracket, if so push it to the end (front) of the stack. If not,
Determine if the stack is empty or not and determine if the front of the stack 
is a proper opener for the current closing index which is a closing bracket. If
the stack is empty or if theyare not proper closed brackets, return False. Else
pop the front of the stack. Finally, return True if the stack is empty and False
if it is not.

As There is no repeated index and it is bound by the length of the string which 
length is n, the time complexity of this algorithm is O(n) and the space 
complexity is O(n) for using the stack.
'''

def Stack(s: str):

    stack = []
    
    values = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    for c in range(len(s)):

        if s[c] not in values:

            stack.append(s[c])

        elif (not stack or stack[-1] != values[s[c]]):

            return False
        
        else:

            stack.pop()

    return True if len(stack) == 0 else False

    

