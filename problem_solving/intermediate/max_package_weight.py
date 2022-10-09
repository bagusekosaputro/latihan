def maxPackageWeights(packageWeights: list):
    pos = 0
    result = []
    if len(packageWeights) == 1:
        return packageWeights[0]

    if pos < len(packageWeights) - 1:
        left = pos + 1
        if left < len(packageWeights) - 1:
            right = left + 1
            curr_max = packageWeights[left] + packageWeights[right]
            if curr_max > packageWeights[left]:
                result.append(packageWeights[pos])
                result.append(curr_max)
            else:
                maxPackageWeights(result)
        else:
            pass

    # while pos < len(packageWeights) - 1:
    #     left = pos + 1
    #     if left < len(packageWeights) - 1:
    #         right = left + 1
    #         curr_max = packageWeights[left] + packageWeights[right]
    #         print(curr_max)
    #         if curr_max > packageWeights[left]:
    #             result.append(packageWeights[pos])
    #             result.append(curr_max)
    #             pos = right
    #         else:
    #             pos += 1

    print(result)
    return result


if __name__ == "__main__":
    packageWeights = [2, 9, 10, 3, 7]

    maxPackageWeights(packageWeights)
