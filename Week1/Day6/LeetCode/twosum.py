# twosum.py - Given an array of integers nums and a target integer, return the indices of the two numbers such that they add up to the target

# Examples
nums = [4, 7, 11, 2]
target = 9

# for i in range(0, len(nums)):
#     complement = target - nums[i]
#     if not complement in nums:
#         continue
#     else:
#         print([i, nums.index(complement)])
#         break

def two_sum(nums, target):
    seen = {}  # stores number -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]  # return the two indices
        seen[num] = i
    return []  # return empty if no solution found

print(two_sum(nums, target))