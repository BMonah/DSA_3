'''Output numbers from 1 to x. if the number is divisible by 3, replace it with "Fizz".
if it is divisible by 3 and 5, replace it with FizzBuzz'''


class Fizzbuzz:
    def __init__(self, num):
        self.num = num

    def fizz(self):
        arr = []
        dict = {}
        for i in range(0, self.num):
            if i % 5 == 0 and i % 3 == 0:
                arr.append("FizzBuzz")
                dict[i] = ("FizzBuzz")
            elif i % 3 == 0:
                arr.append("Fizz")
                dict[i] = ("Fizz")
            elif i % 5 == 0:
                arr.append("Buzz")
                dict[i] = ("Buzz")
            else:
                arr.append("not divisible")
                dict[i] = ("not divisible")
        return dict


'''
def fizz():
    for i in range(0, 5):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizz()
'''
number = 15
result = Fizzbuzz(number)
# print(Fizzbuzz.fizz(result))


def fixxbuxx(number):
    my_dic = {}
    for i in range(1, number+1):
        if i % 3 == 0 and i % 5 == 0:
            my_dic[i] = ('Fizzbuzz')
        elif i % 3 == 0:
            my_dic[i] = ('Fizz')
        elif i % 5 == 0:
            my_dic[i] = ('buzz')

        else:
            my_dic[i] = ("not Fizzbuzz")
    return my_dic


print(fixxbuxx(15))
