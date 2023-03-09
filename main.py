def twoSum(self, nums: List[int], target: int) -> List[int]:
    index = []
    for i, n in enumerate(nums):
        tmp = target - n
        if tmp in nums[i + 1:]:
            return nums.index(n), nums[i + 1:].index(tmp) + (i + 1)

