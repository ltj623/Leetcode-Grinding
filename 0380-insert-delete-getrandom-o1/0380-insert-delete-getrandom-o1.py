class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            # make a hashMap. Key -> val, value -> the index
            self.numMap[val] = len(self.numList)
            # append the val into the list
            self.numList.append(val)

        return res

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            # find the index of the value
            idx = self.numMap[val]
            # get the last value in the numList
            lastVal = self.numList[-1]
            # replace the deleted element with the last value
            self.numList[idx] = lastVal
            self.numList.pop()
            # update the new hashmap
            # the lastVal should be put in new index
            # since it replace the deleted element
            self.numMap[lastVal] = idx
            # delete the key-value pair of the old val in hashmap
            del self.numMap[val]

        return res
        
    def getRandom(self) -> int:
        return random.choice(self.numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()