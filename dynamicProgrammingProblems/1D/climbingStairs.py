"""
Climbing Stairs (Easy)

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""



"""
Possible solution: Two variables

Create two variables, o and t and set them both to 1. This will be are constraint
and handle the base case of 1 as t is set to 1, the for loop does not occur and
you return 1. set te as the summation of o and t, the next iteration of the 
fibonacci sequence this problem follows. Set o to t to keep track of the previous
iteration of the algorithm and then set t to te to continue the loop. Do this 
until the loop ends at n - 1, which handles the technically second base case
of n = 2. Finally return 2. 

As there is no need to use an extra data structure and the for loop is bounded 
by n, the runtime complexity is O(n) and the space complexity is O(1).
"""


def TwoVariables(n: int) -> int:
  o = 1
  t = 1
  for _ in range(n - 1):
    te = o + t
    o = t
    t = te
  return t