def twoSum(a: list,target: int) -> list:
    left, right = 0, len(a) - 1
    while left < right:
        sum = a[left] + a[right]
        if sum > target:
            right -= 1
        elif sum < target:
            left += 1
        else:
            return [left + 1, right + 1]


if __name__ == "__main__":
    target = 7
    values = list(sorted([1, 5, 6, 3, 8, 10, 9, 12]))

    print(twoSum(values, target))
