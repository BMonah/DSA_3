class Marching:
    def isMarching(parentheses):
        stack = []
        par = {')': '(', ']': '[', '}': '{'}
        open = ('([{')
        for i in parentheses:
            if i in open:
                stack.append(i)
            else:
                if not stack or stack.pop() != par[i]:
                    stack.append(i)
        return True if not stack else False


s = "{}()[]()"
print(Marching.isMarching(s))


def balanced(parenthesis):
    open = '({['
    my_dic = {'}': '{', ']': '[', ')': '('}
    stack = []
    for i in parenthesis:
        if i in open:
            stack.append(i)
        else:
            if not stack or stack.pop() != my_dic[i]:
                stack.append(i)
    return True if not stack else False


s = "{}()[]()"


def is_balanced_parentheses(parentheses):
    stack_list = []
    open_par = ['(', '[', '{']
    closed_par = [')', ']', '}']
    item = None
    for i in parentheses:
        if i in open_par:
            stack_list.append(i)
        else:
            item = closed_par.index(i)
            if not stack_list or stack_list.pop() != open_par[item]:
                stack_list.append(i)
    return True if not stack_list else False


s = "{}()[]()"
# print(Marching.isMarching(s))
print(is_balanced_parentheses(s))
