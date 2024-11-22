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
