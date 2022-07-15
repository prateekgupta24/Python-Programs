#README
#Algorithm Engineering Project 4
#Group Members:
#Prateek Gupta - CWID:888625282 – Email: pgupta24@csu.fullerton.edu
#Heidar Rahmanian - CWID:889144713 – Email: heidar84@csu.fullerton.edu
#Algorithm 2 – Dynamic Programming
# ⁃ Instructions on how to run submitted code:
# ⁃ 1. Save PartB.py file to desktop
# ⁃ 2. Open terminal (macOS) or command command prompt(Windows)
# ⁃ 3. Enter “ cd Desktop ” cmd and press enter
# ⁃ 4. Enter “ ls Desktop ” (macOS) or “ dir “ (Windows)
# ⁃ 5. Enter “ python PartB.py ”

# import random

# def generate(N):
#     items = []
#     for i in range(N):
#         items.append([round(random.random() * 1000), round(random.random() * 1000)])
#     return items

# calculate of total investment value of a candidate subset
def total_value(items, candidate):
    total_investment_value = 0
    for itemId in candidate:
        total_investment_value += items[itemId][1]
    return total_investment_value

# calculate of total number of stocks of a candidate subset
def total_num_of_stocks(items, candidate):
    total = 0
    for itemId in candidate:
        total += items[itemId][0]
    return total

# dynamic programming
def stock_maximization (M, items):
    N = len(items)
    if(N <= 0): return []

    # use DP to find the subset of items with total sum of investment value <= M and the total number of stocks is maximized
    max_num_of_stocks = [[0 for _ in range(M + 1)] for _ in range(N)]

    # calculate dp[0][j]
    if(items[0][1] <= M):
        max_num_of_stocks[0][items[0][1]] = items[0][0]

    # from dp[i][j] -> update for dp[i + 1][j']
    for i in range(0, N - 1):
        for j in range(M + 1):
            # not add items[i] to the current subset
            max_num_of_stocks[i + 1][j] = max(max_num_of_stocks[i + 1][j], max_num_of_stocks[i][j])
            # add items[i] to the current subset
            if(j + items[i + 1][1] <= M):
                max_num_of_stocks[i + 1][j + items[i + 1][1]] = max(max_num_of_stocks[i + 1][j + items[i + 1][1]], max_num_of_stocks[i][j] + items[i + 1][0])

    # trace the best  result

    # find the best total investment sum of the best subset
    bestJ = 0
    for j in range(M + 1):
        if(max_num_of_stocks[N - 1][j] > max_num_of_stocks[N - 1][bestJ]):
            bestJ = j

    # trace back through all items to find the best subset
    best = []
    for i in range(N - 1, -1, -1):
        # from (i,bestJ) -> decide if items[i] should be added to the best subset or not
        if(i <= 0):
            if(max_num_of_stocks[i][bestJ] > 0):
                best.append(i)
        else:
            if(max_num_of_stocks[i][bestJ] == max_num_of_stocks[i - 1][bestJ]):
                continue
            else:
                best.append(i)
                bestJ -= items[i][1]

    best.reverse()

    return best

if __name__ == "__main__":
    items = [[1, 2], [3, 3], [5, 6], [6, 7]]
    M = 10

    # items = generate(20)
    # M = round(random.random() * 1000)
    # print(items, M)

    best_combination = stock_maximization(M, items)
    print(f"Best combination : {best_combination}", end = ' => ')
    for itemId in best_combination:
        print(items[itemId], end = ' ')
    print()
    print('Number of stocks = ', total_num_of_stocks(items, best_combination))
    print('Total value = ', total_value(items, best_combination))
