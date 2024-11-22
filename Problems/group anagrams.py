
def group_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagram_groups:
            anagram_groups[sorted_string].append(string)
        else:
            anagram_groups[sorted_string] = [string]
    return list(anagram_groups.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


def anagrams(strings):
    my_dic = {}
    for word in strings:
        sorted_word = ''.join(sorted(word))
        if sorted_word in my_dic:
            my_dic[sorted_word].append(word)
        else:
            my_dic[sorted_word] = [word]
    return list(my_dic.values())


print(anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


def anagram2(value):
    my_dic = {}
    for i in value:
        sorted_i = ''.join(sorted(i))
        if sorted_i in my_dic:
            my_dic[sorted_i].append(i)
        else:
            my_dic[sorted_i] = [i]
    return list(my_dic.values())


word = 'twosum'
print(sorted(word))

print(anagram2(["eat", "tea", "tan", "ate", "nat", "bat"]))


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dic = {}
        my_dict = {}
        arr = []
        if len(s) != len(t):
            return False
        for i in s:
            if i not in my_dic:
                my_dic[i] = (1)
            else:
                d = my_dic[i]
                d += 1
                my_dic[i] = (d)
        for j in t:
            if j in my_dict:
                c = my_dict[j]
                c += 1
                my_dict[j] = (c)
            else:
                my_dict[j] = (1)
        print(my_dic, my_dict)
        for i in my_dict:
            if i not in my_dic:
                return False
            else:
                if my_dict[i] != my_dic[i]:
                    arr.append(i)
        if arr:
            return False
        else:
            return True


class SortedSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False


s = "racecar"
t = "carrace"
print(Solution().isAnagram(s, t))
