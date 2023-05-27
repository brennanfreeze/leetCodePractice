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
