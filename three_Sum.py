
def threeSum(nums):
    # Sort the input list to simplify duplicate handling and two-pointer traversal
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n - 2):
        # Skip duplicate values for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                # Found a valid triplet
                res.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for the second number
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # Skip duplicates for the third number
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move both pointers inward
                left += 1
                right -= 1

            elif total < 0:
                # Sum too small, move left pointer to increase total
                left += 1
            else:
                # Sum too large, move right pointer to decrease total
                right -= 1

    return res


# Sample Usage
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
# Output: [[-1, -1, 2], [-1, 0, 1]]






# uploaded on leetcode 
class Solution:
    def threeSum(self, nums):
        # Sort the input list to simplify duplicate handling and two-pointer traversal
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    # Found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the second number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the third number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers inward
                    left += 1
                    right -= 1

                elif total < 0:
                    # Sum too small, move left pointer to increase total
                    left += 1
                else:
                    # Sum too large, move right pointer to decrease total
                    right -= 1

        return res


