def magicSquare(square):
    for row, rv in enumerate(square):
        for col, cv in enumerate(rv):
            print(row, col)


if __name__ == "__main__":
    s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
    magicSquare(s)
