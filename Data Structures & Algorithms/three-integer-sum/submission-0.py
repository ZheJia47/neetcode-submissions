class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()


        for i,item in enumerate(nums):
            if item>0:
                break
            if i>0 and item==nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l<r:
                if item+nums[l]+nums[r] > 0:
                    r-=1
                elif item+nums[l]+nums[r] < 0:
                    l+=1
                else:                    
                    res.append([item,nums[l],nums[r]])
                    r-=1
                    l+=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res