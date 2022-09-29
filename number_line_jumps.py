def number_line_jump(x1: int, v1: int, x2: int, v2: int) -> str:
    possible = (x2 - x1) // v1 < v1
    gap = (x2+v2)//v1
    gap2 = (x2+v2)%(x1+v1)
    print(gap2)
    if gap > v1:
        return "NO"
    else:
        return "YES"


if __name__ == "__main__":
    print(number_line_jump(0, 3, 4, 2))
    print(number_line_jump(0, 2, 5, 3))
    print(number_line_jump(21, 6, 47, 3))
    print(number_line_jump(14, 4, 98, 2))
