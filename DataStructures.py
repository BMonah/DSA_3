from collections import deque
# List
List = [0, 7, 5]

for i in range(1, len(List)):
    print(List[i])
    if List[i] <= List[i-1]:
        print(False)
    else:
        print(True)

print(List[1])
print(len(List))

print(range(len(List)))
# root = List.pop()
# while root:
root = []
for i in range(1, len(List)):
    print(List[i])
    # root.append(List.pop(0))
    # print(root)
print(root)
List.append(4)
print(List)
List = ['1', '2', '3', "GFG", '2.3']
List.extend([19])
# print(List[0])
# x = List.pop()
# print(x)
# print(List)
# List2 = List.pop(0)
# print(List + ["Mumbai"])
# print(List)
# List.pop()
print(List)
List.append('i')

print(List)
# print(List.index("GFG"))
print(List[0:5])
# List.pop()

# print(List)

# print(new)
# print(List[0]) #first element
# print(List[-1])  # last element
# print(List.index(2.3))

# Tuple
Tuple = ('Geeks', 'For', 'Nerds')
# print(Tuple)
# print(Tuple[0])  # First elemet
# print(Tuple[-2])  # second last element

# Set
# mutable collection of data that does not allow any duplication
Set = set([1, 1, 2, 3, 'Geeks', 'for', 'Geeks'])
# print(Set)
# for i in Set:
#    print(i, end=" ")
# print()

# String
String = "Welcome Home"
arr = []
for i in String:
    arr.append(i)
# print(arr)

# print(String)
# print(String[0])
num = [String[0]]
# print(num)
# print(int((String.index('W')))+1)
# num = str(-1234)
# print(num[0])
# print(len(num))

# Dictionary
Dict = {'Name': 'Bonny', 'Age': 31, 'Group': [1, 2, 4]}
# for x in Dict['Group']:
# print(x)
# print(Dict['Group'])
# print(Dict)
# print(Dict['Name'])
print(Dict.get('Age'))
print(Dict['Age'])
# print(Dict['Name'])
y = [1, 2, 3, 4, 5]
myDict = {x: x**2 for x in y}
i = "Bonny"
if i in Dict:
    print(True)
else:
    print(False)
# print(myDict)

Dict[2] = 3
Dict[21] = [31]
# Dict.update({"new": ["old"]})
# Dict[2].append(4)
print(Dict)
print(Dict['Group'])
print(len(Dict))
# print(Dict[2])
# print(myDict)

# Queue
# Queues are linear data structures that store items in a First in First Out manner
# Queue implementation using a list
# Enqueue - Adds an item to the queue. if the queue is full, then it is said to be an overflow condition
# Dequeue - Removes an item from the queue. if the queue is empty, it is said to be an Underflow condition
# Front - get the front item from the queue
# Rear - get the last item from queue

queue = []
queue.append('A')
queue.append('b')
queue.append('c')  # adding an item to a queue
# print(queue)
# new = queue.pop(0)
print(queue)
print(queue.pop())
print(queue)
# print(queue.pop())
# print(new)
# print(queue.pop(0))  # removing an item from a queue
# print(queue)


# x = 0
# while x < 5:
# x += 1
# print(x)

x = 3
arr = [1, 4, 93, 21]
arr2 = []
# for i in range(len(arr)-1, 0, -1):
# print(arr[i])
# for j in range(i):
# print(arr[j])

# arr2.append(arr[i])
# print(arr2)
new = "bon"
my_hash = 0
# for letter in new:
# my_hash = my_hash + (ord(letter)+2)
# print(letter)
# print(my_hash)
# print(my_hash)
# test = (0 + ord('S') * 23) % 7
# print(test)
# print(107*23 % 7)
test2 = [2]
test3 = test2*7
# print(test3)
test4 = [None] * 7
test4[2] = 3
# print(test4)

# for index, item in enumerate(test3):
# print(index, item)
par = {')': '(', ']': '[', '}': '{'}
# print(par[')'])
# for i in range(len(par)-1, 0, -1):
# print(i)
# s = "})[]"
# for i in s:
# print(i)

word = 'bade'
print(''.join(sorted(word)))
newList = [1, 2, 3, 4, 5, 6, 7]
print(newList)
print(range(len(newList)))
newList.append('D')
print(newList)
print(len(newList))
print(range(len(newList)))
for i in range(len(newList)):
    print(i)

for i in range(len(newList)):
    print(newList[i])


charSet = set()
# print(sorted(charSet))
l = 0
string = "abccddefg"
charSet.add('s')
charSet.add('d')
charSet.remove('d')
print(charSet)
'''
for i in range(len(string)):
    while string[i] in charSet:
        charSet.remove(string[l])
        l += 1
    charSet.add(string[i])
print(charSet)
'''

test = [1, 2, 3]
test.pop(0)
print(test)

listt = [1, 2, 2, 3, 4, 4]
q = deque()
q.append(2)
q.append(4)
q.append(7)
q.pop()
print(q)
listt.pop(0)
listt.append((8, 9))
print(listt)

grid = [
    ["0", "1", "1", "1", "0"],
    ["0", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(grid[1][0])

nums = [1, 2, 3, 4, 5, 5]
nums_res = [[] for i in range(len(nums))]
print(nums_res)
count = {}

for n in nums:
    count[n] = 1 + count.get(n, 0)
    print(count)

print(5//2)
