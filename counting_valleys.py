def count_valleys(steps: int, path: str):
    result = {
        "S": 0,
        "D": 0,
        "U": 0
    }
    valley = 0
    for i in range(steps):
        if path[i] == "D":
            if result["S"] == 0:
                result["D"] += 1
                valley += 1
            result["S"] -= 1
            result["U"] -= 1
        else:
            result["D"] -= 1
            result["S"] += 1
            result["U"] += 1

    return valley


if __name__ == "__main__":
    s = "DUDDDUUDUU"
    p = 10
    # s = "UDDDUDUU"
    # p = 8
    """
    _/\      _
       \    /
        \/\/
    """
    count_valleys(p, s)
