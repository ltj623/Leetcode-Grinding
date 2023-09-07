class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        tmp = set()

        for k, v in cnt.items():
            if v in tmp:
                return False
            tmp.add(v)
        return True
        