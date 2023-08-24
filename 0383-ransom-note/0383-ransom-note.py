class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False
        cnt_r, cnt_m = Counter(ransomNote), Counter(magazine)

        for c in ransomNote:
            if cnt_r[c] > cnt_m[c]: return False
        return True
