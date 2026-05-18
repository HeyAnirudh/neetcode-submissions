class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        for i in range(0,len(nums)):
            for j in range(i,len(nums)-1):
                if nums[i]+nums[j]==target:
                   return [i,j]