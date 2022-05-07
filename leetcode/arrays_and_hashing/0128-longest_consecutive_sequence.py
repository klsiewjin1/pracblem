from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tmp = set()
        for num in nums:
            tmp.add(num)
        max_sequence = 0
        while len(tmp) > 0:
            holder = []
            for elem in tmp:
                ori_elem = elem
                holder.append(elem)
                while elem+1 in tmp:
                    elem += 1
                    holder.append(elem)
                while ori_elem-1 in tmp:
                    ori_elem -= 1
                    holder.append(ori_elem)
                break
            tmp -= set(holder)
            max_sequence = max(max_sequence, len(holder))
        return max_sequence
