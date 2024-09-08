# GFG: 136. Single Number

class Solution:
    def singleNumber(self, nums) -> int:
        bag = set()
        for i in nums:
            if i in bag: bag.remove(i)
            else: bag.add(i)
        return bag.pop()