'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''


'''
Possible Soltion: Using sub copy of string
Time complexity: O(n)
Space complexity: O(n)

Make a copy of the inputted string with every alpha numeric character found in
the string. Then within the sub-copy, set two variables on each end of the string
and determine if they are the same value or not. If they are not then return false
and if every value is not false, then the obvious solution should be true.

As there is a need to make a copy of the inputted string, the time complexity
and the space complexity is going to be O(n).
'''
def UseExtraMemory(s: str):

    s_copy = ""

    for i in s:

        if (i.isalnum()):

            s_copy += i.lower()

    l = 0

    r = len(s_copy) - 1

    while l <= r:

        if (s_copy[l] != s_copy[r]):

            return False
        
        l += 1

        r -= 1

    return True


'''
Possible Soltuion: Iterate through non-alphanumeric
Time complexity: O(n)
Space complexity: O(1)

Instead of making a copy, simply commit to the same two pointers l and r to act
the same way as the above algorithm. In this case, simply set a while loop
to increment/decrement the variables if they are not alpha numeric and if 
l <= r.

Although it may seem like this is cutting half the steps into O(n / 2) for time
complexity, it is actually still O(n) as big O deals with worst case and the 
worst case is still an input of all alpha numeric values. So, the time
complexity is O(n), however the space complexity is cut down to O(1). 
'''

def IterateNonAL(s: str):

    l = 0

    r = len(s) - 1

    while l <= r:

        while l <= r and not s[l].isalnum():

            l += 1

        while l <= r and not s[r].isalnum():

            r -= 1

        if (s[l].lower() != s[r].lower):

            return False
        
        l += 1

        r -= 1

    return True