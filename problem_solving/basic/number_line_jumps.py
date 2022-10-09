def number_line_jump(x1: int, v1: int, x2: int, v2: int) -> str:
    jump_count = x2 -x1

    for i in range(jump_count):
        x1 = x1 + v1
        x2 = x2 + v2

        if x1 == x2:
            return "YES"
    return "NO"


if __name__ == "__main__":
    print(number_line_jump(0, 3, 4, 2))
    print(number_line_jump(0, 2, 5, 3))
    print(number_line_jump(21, 6, 47, 3))
    print(number_line_jump(14, 4, 98, 2))
