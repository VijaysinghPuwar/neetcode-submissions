class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        seen = []
        r = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                r = r + 1     
            else:
                seen.append(r)
                r =0
        seen.append(r)
        return max(seen)
