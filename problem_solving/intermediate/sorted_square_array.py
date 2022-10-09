def sorted_square_array(n: list):
    result = n.copy()
    left = 0
    idx, right = len(n) - 1, len(n) - 1

    while idx >= 0:
        if abs(n[left]) > abs(n[right]):
            result[idx] = n[left] * n[left]
            left += 1
        else:
            result[idx] = n[right] * n[right]
            right -= 1
        idx -= 1
    return result


if __name__ == "__main__":
    # numbers = [-7, -3, 2, 3, 5]
    numbers = [-6, -4, 1, 2, 3, 5]
    res = sorted_square_array(numbers)
    print(res)
