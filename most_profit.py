# Most Profit

def most_profit(inp):
    max_profit = 0

    # use nested loop to find most profit value
    # outer loop iterate each element
    # inner loop iterate element after current index
    # in child track the most profit by doing substraction current index in root with each element in child root
    for i in inp:
        for j in inp:
            if abs(j - i) > max_profit:
                max_profit = abs(j-1)
        

    return max_profit

if __name__ == "__main__":

    input1 = [1,2,3,4,5,6]
    output = 5

    input2 = [5, 15, 30, 50]
    output = 45
    input3 = [7,1,2,3,4,5,6]

    print(most_profit(input2))
