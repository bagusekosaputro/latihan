def maxProfit(M, prices):
    eligible = []
    earn = 0
    for i in range(len(prices)):
        if prices[i] < 0:
            eligible.append(abs(prices[i]))

    if not eligible:
        return earn

    arr_length = len(eligible)
    left = 0
    # while left < arr_length - 1:
    #     curr = eligible[left]
    #     right = left + 1
    #     if eligible[left] > eligible[right]:
    #         eligible[left] = eligible[right]
    #         eligible[right] = curr
    #
    #     left += 1

    for k, v in enumerate(eligible):
        for x, y in enumerate(eligible):
            t = v
            if x > y:
                eligible[x] = y
                eligible[y] = t
            else:
                break

    print(eligible)
    for k in eligible[M*-1:]:
        earn += k

    return earn


def minimumDolls(dollSizes):
    left = 0
    right = len(dollSizes) - 1
    remainingDolls = 0

    while left < right:
        print(left,right)
        if dollSizes[left] > dollSizes[right]:
            left += 1
        else:
            right -= 1
            left += 1
            remainingDolls += 1

    return remainingDolls


if __name__ == "__main__":
    print(maxProfit(2, [-30, -10, -40, -20]))

    # print(minimumDolls([4, 2, 2, 3, 3]))
    # print(minimumDolls([1, 2, 2, 3, 4, 5]))



