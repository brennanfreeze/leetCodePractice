'''
Encode and Decode Strings (medium)

Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back 
to the original list of strings.

Please implement encode and decode

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
'''


'''
Possible Soltuion

Time Complexity: O(n)
Space Complexity: O(n)

For encoding, for each index value in strs, append it to res with ':;'at the end.
Make sure to commit to a substring res value. For decode, for through res with 
an index iterator and a curr_split to indicate when you last split the string.
everytime a ':' is found and the next value in the string is ';', append the 
substring to res array.

As both of these need strings and arrays to convert one to the other and they
both use a iterator through the entire data structure that holds the data, the
space and time complexity are both O(n).
'''

def encode(strs):
    res = ""

    for s in strs:
        res += s + ':;'

    return res[:len(res) - 2]

def decode(str):

    res = []

    i = 0

    curr_split = 0

    while i < len(str):

        if (i + 1 < len(str) and str[i] == ':' and str[i + 1] == ';'):

            res.append(str[curr_split:i])

            curr_split = i + 2

        i += 1


    res.append(str[curr_split:])

    return res
