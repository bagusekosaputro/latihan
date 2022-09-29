def migratoryBirds(arr):
    count_seen = {}
    lowest_seen = max(arr)
    highest_freq = 2
    for i in arr:
        count_seen[i] = count_seen.get(i, 0) + 1
        if count_seen[i] > highest_freq:
            highest_freq = count_seen[i]

    for k, v in count_seen.items():
        if k < lowest_seen and v == highest_freq:
            lowest_seen = k
    return lowest_seen


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]

    result = migratoryBirds(arr)
    print(result)
