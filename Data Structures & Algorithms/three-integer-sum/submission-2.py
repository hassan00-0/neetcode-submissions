class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []
        for i in range(len(nums)):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            j = i + 1
            k = len(nums) - 1
            while k > j:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    solution.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while k > j and nums[j] == nums[j - 1]:
                        j += 1
                    while k > j and nums[k + 1] == nums[k]:
                        k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        return solution