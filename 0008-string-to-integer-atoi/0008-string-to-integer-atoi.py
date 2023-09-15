class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        sign = 1
        index = 0
        res = 0

        while index < len(s) and s[index] == " ":
            index += 1
        if index < len(s) and s[index] == "-":
            sign = -1
            index += 1
        elif index < len(s) and s[index] == "+":
            index += 1
        
        while index < len(s) and s[index].isdigit():
            res = res * 10 + int(s[index])
            index += 1
        
        if MIN_INT<res*sign<MAX_INT:
            return res*sign
        else:
            return MAX_INT if sign == 1 else MIN_INT
        

        