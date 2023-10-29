class Solution:
    def addDigits(self, num: int) -> int:
        def helper(num):
            output = 0
            while num != 0:
                digit = num % 10
                output += digit
                num //= 10
            return output


        if num == 0: return 0
        while len(str(num)) != 1:
            num = helper(num)
        return num
        