from typing import List 
deftwoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                l=i
                r=j
                return [l, r]
