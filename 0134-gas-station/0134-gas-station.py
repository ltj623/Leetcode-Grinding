class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas): return -1

        count, res = 0, 0
        for i in range(len(gas)):
            count += gas[i] - cost[i]
            if count < 0:
                count = 0
                res = i + 1
        return res