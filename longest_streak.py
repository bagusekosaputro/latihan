def longestStreak(deployment: list, grace_point: int):
    count_deployment = {}
    result = 0

    for i in deployment:
        count_deployment[i] = count_deployment.get(i, 0) + 1
    left = 0
    right = count_deployment.get(1) - 1
    while len(deployment) - 1 >= right >= left:
        print(left, right)
        if deployment[left] == 0:
            count_deployment[0] = count_deployment.get(0) - 1
        else:
            result += 1

        print(count_deployment.get(0))
        left += 1

    # print(count_deployment)
    print(result)
    return result


if __name__ == "__main__":
    deployments = [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0]
    # deployments = [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    k = 2

    longestStreak(deployments, k)
