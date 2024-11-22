# check if the last character of the two strings are same
# if same return 1 plust call the function recursively where you remove the last character
# if they are not same return the maximum LCS function without the last character of either
# string 1 or string2

# if item exists in memo return memoized item
# check if last item is same and return 1 + recursive of the next last item
# recursively return maximum between S1 without the last item or S2 without the last item


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m = len(text1)
        n = len(text2)
        memo = [[None for i in range(max((n+1), (m+1)))]
                for i in range(max((n+1), (m+1)))]

        def lcs(text1, text2, m, n):
            if n == 0 or m == 0:
                return 0

            if memo[m][n] != None:
                return memo[m][n]

            if text1[m-1] == text2[n-1]:
                memo[m][n] = 1 + lcs(text1, text2, m-1, n-1)
                return memo[m][n]

            else:
                memo[m][n] = max(lcs(text1, text2, m-1, n),
                                 lcs(text1, text2, m, n-1))
            return memo[m][n]
        return lcs(text1, text2, m, n)


def lcs(S1, S2, m, n, memo):
    # return 0 if the length of the strings are zero
    if n == 0 or m == 0:
        return 0

    # Already exists in the memo table
    # items in the memo table are initialized as None
    if memo[m][n] != None:
        return memo[m][n]

    # if the last character of S1 and S2 are same, add 1 and recursuvely call the function
    if S1[m-1] == S2[n-1]:
        memo[m][n] = 1 + lcs(S1, S2, m-1, n-1, memo)
        return memo[m][n]
    else:
        memo[m][n] = max(lcs(S1, S2, m, n-1, memo), lcs(S1, S2, m-1, n, memo))
        return memo[m][n]


S1 = 'ABGJJJ'
S2 = 'ABTTTGJ'
m = len(S1)
n = len(S2)
memo = [[None for _ in range(max((n+1), (m+1)))]
        for _ in range(max((n+1), (m+1)))]

print(lcs(S1, S2, m, n, memo))

[[-1, -1, -1, -1],
 [-1, -1, -1, -1],
 [-1, -1, -1, -1]]


l = 'ABCDE'
print(len(l))

print([[None for i in range(5)] for i in range(4)])
