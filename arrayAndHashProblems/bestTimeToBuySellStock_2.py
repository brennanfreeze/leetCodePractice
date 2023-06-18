'''
Best Time to Buy and Sell Stock II (medium)

You are given an integer array prices where prices[i] is the price of a 
given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. However, you can 
buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), 
profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
'''

'''
Possible Solution: Greedy Algorithm
Time Complexity: O(n)
Space Complexity: O(1)

Start with a base max value called ma which is set to within range of 1 to the 
length of the array of prices, if prices at i is greater
than the prices at i - 1, we can determine there was an increase in price from
the day before and we should sell the stock we bought it at. The variable ma adds
up the difference between value at index i and i - 1 and continues through the 
array and finally returns ma as the return value.

As there is no needed extra memory for this solution, the space complexity is 
going to be O(1) and the time complexity being bound by the input array length, 
is going to be O(n).
'''

def Greedy(prices):

    ma = 0

    for i in range(1, len(prices)):

        if prices[i] > prices[i - 1]:

            ma += prices[i] - prices[i - 1]

    return ma
