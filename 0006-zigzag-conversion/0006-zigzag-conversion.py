class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Only one line, just return s
        if numRows == 1: return s
        res = ""

        # Say we have 3 rows, we iterate through each row
        for r in range(numRows):
            # for 0th row and 2nd row, the character in each line follow the increment
            # 3 rows => (3 - 1) * 2 = 4
            increment = (numRows - 1) * 2
            for i in range(r, len(s), increment):
                # cases for the first row and the last row
                res += s[i]
                # cases for not the first and the last row, the increment should be increment - 2 * r
                if 0 < r < numRows - 1 and i + increment - 2 * r < len(s):
                    res += s[i + increment - 2 * r]
        return res
