class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        # Result array to store multiplication results
        result = [0] * (len(num1)+len(num2))

        # Reverse both numbers to multiply from least significant digits
        num1, num2 = num1[::-1], num2[::-1]

        # multiply each digit of num1 with each digit of num2
        for i in range(len(num1)):
            for j in range(len(num2)):
                # multiply the digits
                digit_product = int(num1[i])*int(num2[j])
                # Add to the current position in result array
                result[i+j] += digit_product
                # handle the carry
                result[i+j+1] += result[i+j] // 10
                # make sure only the most significant digit remains in the current index
                result[i+j] %= 10

        # remve leading zeros and reverse the result array to form the final number
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        result = [str(i) for i in result]
        result = result[::-1]
        return ''.join(result)


print(Solution().multiply("123", "456"))

m = ['1', '2', '3', '4']
print(''.join(m))
