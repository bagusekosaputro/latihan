def min_window_string(s: str, search: str) -> str:
    if t == "":
        return ""

    count_t, window = {}, {}
    for c in search:
        count_t[c] = 1 + count_t.get(c, 0)

    have, need = 0, len(count_t)
    res, res_len = [-1, -1], float("infinity")
    left = 0
    for right in range(len(s)):
        c = s[right]
        window[c] = 1 + window.get(c, 0)

        if c in count_t and window[c] == count_t[c]:
            have += 1

        while have == need:
            # update result
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = (right - left + 1)

            # pop from the left of the window
            window[s[left]] -= 1
            if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                have -= 1
            left += 1

        first, last = res
        return s[first:last+1] if res_len != float("infinity") else ""


if __name__ == "__main__":
    values = "ADOBECODEBANC"
    t = "ABC"
    result = min_window_string(values, t)
    print(result)
