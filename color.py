colors = ['R', 'G', 'B']


def isStableColor(A, colPlacements):
    color_r = 0
    color_g = 0
    color_b = 0
    for i in range(len(colPlacements)):
        if colPlacements[i] == 'R':
            color_r += A[i]
        if colPlacements[i] == 'G':
            color_g += A[i]
        if colPlacements[i] == 'B':
            color_b += A[i]

    if color_r == color_g and color_g == color_b and color_r == color_b:
        # found the solution
        return ''.join(colPlacements)
    else:
        return False


def solveColor(A, row, colPlacements, result):
    for i in A:
        pass


def solution(A):
    # lets take one element which can be either R G B ( 3 possibilities)

    colPlacements = []
    result = []

    solveColor(A, 0, colPlacements, result)

    return result


if __name__ == "__main__":
    s = solution([3, 7, 2, 5, 4])
    print(s)  # there might be many possible solutions
