class Solution:
    def encode(self, List):
        res = ""
        for item in List:
            res += str(len(item))+'#'+item
        return res

    def decode(self, string):
        res, i = [], 0
        while i < len(string):
            j = i
            # Find the position of the next '#' character
            while string[j] != '#':
                j += 1
            # Get the length of the next string
            length = int(string[i:j])
            # Extract the string based on the length
            res.append(string[j + 1:j + 1 + length])
            # Move to the next encoded segment
            i = j + 1 + length
        return res


List = ["neet", "code", "love", "you"]
string = "4#neet4#code4#love3#you"
# print(Solution().encode(List))
print(Solution().decode(string))
