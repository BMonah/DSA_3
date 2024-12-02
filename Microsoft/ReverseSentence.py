class Reverse:
    def reverseSentence(arr):
        res = []
        new = []
        for i in arr:
            new.append(i)
        while len(new) != 0:
            res.append(new.pop())
        return res

    def resverseString(arr):
        res = []
        new = []
        word = ''
        for i in arr:
            if i != ' ':
                word = word + i
            else:
                new.append(word)
                word = ''
        new.append(word)

        while len(new) != 0:
            res.append(new.pop())

        # res = ' '.join(res)
        return res
        # sentence = ''
        # for i in res:
        #    sentence = sentence + ' ' + i
        # return sentence


def reverse_string(reverse):
    stack = []
    arr = []
    for i in reverse:
        stack.append(i)
    while stack:
        arr.append(stack.pop())
    arr = ''.join(arr)
    return arr


def combine(sentence):
    arr = []
    res = []
    word = ''
    for letter in sentence:
        if letter != ' ':
            word = word + letter
        else:
            arr.append(word)
            word = ''
    arr.append(word)
    print(arr)
    for word in range(len(arr)-1, -1, -1):
        res.append(arr[word])
    return ' '.join(res)


sol = "my school is good i'm"


# print(reverse_string(sol))
# print(Reverse.reverseSentence(sol))
# print(Reverse.resverseString(sol))
print(combine(sol))


class Solution(object):
    def reverseWords(self, s):
        final = []
        res = []
        strings = ""
        for letter in range(len(s)):
            if letter == 0 and s[0] == " " or letter == len(s)-1 and s[len(s)-1] == " ":
                continue
            elif s[letter] == s[letter-1] == " ":
                continue
            elif s[letter] != " ":
                strings = strings+s[letter]
            elif s[letter] == " ":
                res.append(strings)
                strings = ""
        if strings != "":
            res.append(strings)
        print(res)
        while res:
            final.append(res.pop())

        final = " ".join(final)
        return final


print(Solution().reverseWords("a good   example"))
