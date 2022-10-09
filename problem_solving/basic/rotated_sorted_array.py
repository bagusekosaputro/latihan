def searchRotatedSortedArray(nums: list, target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        middle = (left + right) // 2
        if target == nums[middle]:
            return middle

        # left portion
        if nums[left] <= nums[middle]:
            if target > nums[middle] or target < nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        else:
            if target > nums[middle] or target > nums[right]:
                right = middle + 1
            else:
                left = middle - 1
    return -1

if __name__ == "__main__":
    target = 0
    nums = [4, 5, 6, 7, 0, 1, 2]

    print(searchRotatedSortedArray(nums, target))
