def romanToInt(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    solution = 0
    for i in range(len(s)):
        if i+1 < len(s) and roman[s[i]] < roman[s[i-1]]:
            solution -= roman[s[i]]
        else:
            solution += roman[s[i]]
    return solution


print(romanToInt("MCMXCIV"))
