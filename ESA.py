#README
#Algorithm Engineering Project 4
#Group Members:
#Prateek Gupta - CWID:888625282 – Email: pgupta24@csu.fullerton.edu
#Heidar Rahmanian - CWID:889144713 – Email: heidar84@csu.fullerton.edu
#Algorithm 1 – Exhaustive Search Approach
#  ⁃ Instructions on how to run submitted code:
#  ⁃ 1. Save PartA.py file to desktop
# ⁃ 2. Open terminal (macOS) or command command prompt(Windows)
#  ⁃ 3. Enter “ cd Desktop ” cmd and press enter
#  ⁃ 4. Enter “ ls Desktop ” (macOS) or “ dir “ (Windows)
#  ⁃ 5. Enter “ python PartA.py ”

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

def stocks_combinations(items):
    if(len(items) <= 0):
        return [ [] ]
    prev_combinations = stocks_combinations(items[:-1])
    combinations = []

    for combination in prev_combinations:
        combinations.append(combination)

        new_combination = list(combination)
        new_combination.append(len(items) - 1)

        combinations.append(new_combination)

    return combinations

def stock_maximization (M, items):
    best = None
    all_combinations = stocks_combinations(items)
    # print(len(all_combinations))
    # print(all_combinations)
    for candidate in all_combinations:
        if total_value(items, candidate) <= M:
            if best is None or total_num_of_stocks(items, candidate) > total_num_of_stocks(items, best):
                best = candidate
    return best

if __name__ == "__main__":
    items = [[1, 2], [3, 3], [5, 6], [6, 7]]
    M = 10

    # items = [[22, 563], [595, 12], [985, 533], [642, 804], [252, 184], [86, 851], [318, 232], [354, 802], [73, 984], [250, 552], [366, 660], [831, 584], [505, 847], [289, 107], [468, 554], [547, 294], [655, 408], [432, 139], [889, 45], [646, 583]]
    # M = 294

    best_combination = stock_maximization(M, items)
    print(f"Best combination : {best_combination}", end = ' => ')
    for itemId in best_combination:
        print(items[itemId], end = ' ')
    print()
    print('Number of stocks = ', total_num_of_stocks(items, best_combination))
    print('Total value = ', total_value(items, best_combination))
