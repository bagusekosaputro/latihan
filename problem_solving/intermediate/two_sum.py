def twoSum(a: list, target: int) -> list:
    sub_count = {}
    result = []
    for i in range(len(a)):

        if a[i] <= target:
            sub_val = target - a[i]
        else:
            sub_val = a[i]
        if a[i] in sub_count:
            result = [sub_count.get(a[i]), i]
            break
        sub_count[sub_val] = i

    return result


if __name__ == "__main__":
    target = 9
    values = list(sorted([1, 5, 7, 2]))

    print(twoSum(values, target))
