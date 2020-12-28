"""
Followed along to https://www.youtube.com/watch?v=oBt53YbR9Kk&t=12114s&ab_channel=freeCodeCamp.org
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


if __name__ == "__main__":
    print(grid_traveller(3, 2))
    print(grid_traveller(18, 18))
