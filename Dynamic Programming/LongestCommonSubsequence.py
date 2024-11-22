'''
Given two strings text1 and text2, return the length of their longest common 
subsequence. If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
'''


def lcs(S1, S2, m, n):
    # return 0 if the length of the strings are zero
    if n == 0 or m == 0:
        return 0

    # if the last character of S1 and S2 are same, add 1 and recursuvely call the function
    if S1[m-1] == S2[n-1]:
        return 1 + lcs(S1, S2, m-1, n-1)
    # otherwise, find the LCS by either excluding the last character of S1 or S2
    else:
        return max(lcs(S1, S2, m, n-1), lcs(S1, S2, m-1, n))


S1 = 'ABCDEFGXZ'
S2 = 'ACDEFG'
m = len(S1)
n = len(S2)

print(lcs(S1, S2, m, n))
