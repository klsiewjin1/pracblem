"""
Followed along to https://www.youtube.com/watch?v=oBt53YbR9Kk&t=12114s&ab_channel=freeCodeCamp.org
"""


def can_sum(target, arr, hash_table=None) -> bool:
    if hash_table is None:
        hash_table = {}
    if target == 0:
        return True
    if target < 0:
        return False
    for elem in arr:
        remainder = target - elem
        hash_table[target] = can_sum(remainder, arr, hash_table)
        return hash_table[target]

    return False


def how_sum(target: int, arr, hash_table=None):
    """
    Brute force:
    Time: O(n^m * m)
    Space: O(m)

    Memoized:
    Time: O(n*m^2)
    Space: O(m^2)
    """
    if hash_table is None:
        hash_table = {}
    if target and target in hash_table:
        return hash_table[target]
    if target == 0:
        return []
    if target < 0:
        return None

    for elem in arr:
        holder = [elem]
        remainder = target - elem
        hash_table[remainder] = how_sum(remainder, arr, hash_table)
        if hash_table.get(remainder) is not None:
            holder.extend(hash_table[remainder])
            return holder


def best_sum(target: int, arr, hash_table=None):
    if hash_table is None:
        hash_table = {}
    if hash_table.get(target):
        return hash_table[target]
    if target == 0:
        return []
    if target < 0:
        return None

    shortest_combination = None
    for elem in arr:
        holder = [elem]
        remainder = target - elem
        result = best_sum(remainder, arr, hash_table)
        if result is not None:
            holder.extend(result)
            if shortest_combination is None or len(holder) < len(shortest_combination):
                shortest_combination = holder
    hash_table[target] = shortest_combination
    return shortest_combination


def all_ways_to_sum(target, arr):
    if target == 0:
        return []
    if target < 0:
        return None
    for elem in arr:
        remainder = target - elem
        remainder_result = how_sum(remainder, arr)
        if remainder_result is not None:
            pass


if __name__ == "__main__":
    print(how_sum(7, [2, 3]))
    print(how_sum(7, [5, 3, 4, 7]))
    print(how_sum(7, [2, 4]))
    print(how_sum(8, [2, 3, 5]))
    print(how_sum(300, [7, 14]))

    print(best_sum(7, [5, 3, 4, 7]))
    print(best_sum(8, [1, 4, 5]))
    print(best_sum(100, [1, 2, 5, 25]))
