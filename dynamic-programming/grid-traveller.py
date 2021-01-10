"""
Followed along to https://www.youtube.com/watch?v=oBt53YbR9Kk&t=12114s&ab_channel=freeCodeCamp.org
Extended from https://www.techiedelight.com/reach-bottom-right-corner-matrix-exactly-k-turns/
"""


def grid_traveller(row, col, hash_table=None):
    if hash_table is None:
        hash_table = {}
    key = str(row) + "," + str(col)

    if key in hash_table:
        return hash_table[key]

    if row == 0 or col == 0:
        return 0
    if row == 1 and col == 1:
        return 1

    hash_table[key] = grid_traveller(row - 1, col, hash_table) + grid_traveller(row, col - 1, hash_table)

    return hash_table[key]


def valid_grid(i, j):
    return 0 <= i < M and 0 <= j < N


def grid_traveller_with_k_turns(row, col, k, direction_y: bool):
    """
    Returns number of ways to traverse a grid from top left to bottom right with exactly k turns
    """
    if row == 0 or col == 0:
        return 0
    if row == 1 and col == 1 and k == 0:
        return 1
    if direction_y:
        return grid_traveller_with_k_turns(row, col - 1, k - 1, not direction_y) + \
               grid_traveller_with_k_turns(row - 1, col, k, direction_y)
    else:
        return grid_traveller_with_k_turns(row - 1, col, k - 1, not direction_y) + \
               grid_traveller_with_k_turns(row, col - 1, k, direction_y)


def get_total_ways(M, N, k):
    return grid_traveller_with_k_turns(M - 1, N, k, True) + grid_traveller_with_k_turns(M, N - 1, k, False)


if __name__ == "__main__":
    # print(grid_traveller(3, 2))
    # print(grid_traveller(18, 18))
    M = N = 3

    res = get_total_ways(3, 3, 4)
    print(res)
