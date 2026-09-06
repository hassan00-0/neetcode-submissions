class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for key, value in counter.items():
            bucket[value].append(key)

        result = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
            
            if len(result) == k:
                return result
        