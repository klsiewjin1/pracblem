from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(n lg n) + O(n) = O(n lg n) - bottleneck is sorting every word N times
        result_holder = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in result_holder:
                result_holder[sorted_word].extend([word])
            else:
                result_holder[sorted_word] = [word]
        return result_holder.values()