def climb_stairs(s: int) -> int:
    one, two = 1, 1

    for i in range(s-1):
        temp = one
        one = one + two
        two = temp

    return one


if __name__ == "__main__":
    n = 5
    climb_stairs(n)
