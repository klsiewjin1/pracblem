class Solution:
    def numberOfSteps(self, num: int) -> int:
        def solve(num, counter=0):
            if num == 0:
                return counter
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            counter += 1
            return solve(num, counter)

        return solve(num)
