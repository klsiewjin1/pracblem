def min_deletions(s: str, i, j):
    if i >= j:  # pointers are at each other, done
        return 0
    if s[i] == s[j]:  # do not remove if first and last characters are the same
        return min_deletions(s, i + 1, j - 1)
    return 1 + min(min_deletions(s, i + 1, j), min_deletions(s, i, j - 1))


def memoized_min_deletions(s: str, i, j, memo=None):
    if memo is None:
        memo = {}

    if i >= j:  # pointers are at each other, done
        return 0
    key = f"{i},{j}"
    if key not in memo:
        if s[i] == s[j]:  # do not remove if first and last characters are the same
            memo[key] = min_deletions(s, i + 1, j - 1)
        else:
            memo[key] = 1 + min(min_deletions(s, i + 1, j), min_deletions(s, i, j - 1))
    return memo[key]


if __name__ == "__main__":
    X = "ACBCDBAA"
    n = len(X)
    result = memoized_min_deletions(X, 0, n - 1)
    print(result)
