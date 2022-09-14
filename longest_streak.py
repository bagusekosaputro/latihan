def longestStreak(a: list, grace_point: int):
    idx = len(a) - 1
    count_deployment = {}
    for i in a:
        count_deployment[i] = count_deployment.get(i, 0) + 1

    print(count_deployment)


if __name__ == "__main__":
    deployments = [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0]
    k = 2

    longestStreak(deployments, k)
