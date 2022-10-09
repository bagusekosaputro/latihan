def find_max_cluster(processingPower: list, bootingPower: list, powerMax: int) -> int:
    k = 1
    cluster = 0
    print(powerMax)
    while k > 0:
        if k <= 1:
            max_processing = processingPower[0] * k
            max_booting = bootingPower[0]
        else:
            max_processing = sum(processingPower[:k-1]) * k
            max_booting = max(bootingPower[:k-1])
        total = max_processing + max_booting
        print(total)
        if total > powerMax:
            break
        cluster = k
        k += 1
    print(cluster)
    return cluster


if __name__ == "__main__":
    processingPower = [8, 8, 5, 3]
    bootingPower = [4, 1, 4, 5]
    power_max = 35

    find_max_cluster(processingPower, bootingPower, power_max)

