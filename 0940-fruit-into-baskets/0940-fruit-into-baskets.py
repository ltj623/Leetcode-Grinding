class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        res = 0
        cnt = {}
        for r, num in enumerate(fruits):
            cnt[num] = cnt.get(num, 0) + 1
            while len(cnt) > 2:
                cnt[fruits[l]] -= 1
                if cnt[fruits[l]] == 0:
                    del(cnt[fruits[l]])
                l += 1
            res = max(res, r - l + 1)
        return res


        