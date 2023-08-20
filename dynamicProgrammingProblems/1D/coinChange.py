"""
322. Coin Change (medium)
You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, 
return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

"""


"""
Possible Solution: Memoization

set up a dictionary called d, and set every value that is in coins as a key in d,
with 1 as the starting value. This is to indicate how many base coins there are 
starting with for each segment. create a dfs helper function called dfs. If 
amount is 0, then we know no coin can go to that amount, so return 0. If amount 
is already in d, Then we know we have a final answer of how many coins are needed
to get to the amount. set a high number (float('inf') is a valid option) and
go through every coin in coins. if c <= amount, Then we know that is a possible 
coin that can sum up to the amount, however it may not be the final solution. So
set up k to be equal to itself, or 1 + the recursive call of dfs with amount - c
to determine if that is the case. After this recursive call, set the current k
value to be at d[amount] to make sure any recursive call on the stack can continue
to find the valid answer and finally, return k for both recursive and final 
return value. Return the value from dfs if and only if it is not equal to the 
max value from k, if it does, then return -1.
"""

def Memoization(coins, amount: int) -> int:
  
  d = {}
  
  for i in coins:
    
    d[i] = 1
    
  def dfs(amount):
    
    if amount == 0:
      
      return 0
    
    if amount in d:
      return d[amount]
    
    k = 100000
    
    for c in coins:
      
      if c <= amount:
        
        k = min(k,1 + dfs(amount - c))

    d[amount] = k
    
    return d[amount]
  
  res = dfs(amount)
  
  return res if res != 100000 else -1


"""
Possible Solution: Dynamic Programming

Set an array called d of amount + 1 with a length of amount + 1. This will act
as the base case value for each iteration as we know that is the max value the
amount of coins needed (ex: amount = 1000 coins = [1] wouldn't take 1001 coins).
Set dp[0] to 0, as we know this is impossible to add up to within range of given
coins on the question parameters. Within range of the amount given plus 1 and
starting at 1 (no need to add extra steps at d[0], again there is no way to add
any value of coins to 0). For c in range of coins, if i - c is above 0 (used
to make sure that the index is not out of bounds, and if this coin is within
range of the amount being asked for, ex: amount = 5 coins=[10] is never going
to have this if statement be true). The value at index i in d is then set to the
smaller value at either d[i], or 1 + d[i - c] (1 + ... is needed as the current
coin accumulates to the current index). Finally, if the value at index amount
is not amount + 1, then it is known that the value has been found to accumulate
to that amount and it can be returned, if not return -1 as it is not possible. 

"""

def DynamicProgramming(coins, amount: int) -> int:
  
  d = [amount + 1] * (amount + 1)
  
  d[0] = 0
  
  for i in range(1, amount + 1):
    
    for c in coins:
      
      if i - c >= 0:
        
        d[i] = min(d[i], 1 + d[i - c])
        
  return d[amount] if d[amount] != amount + 1 else -1
  
      
    
  