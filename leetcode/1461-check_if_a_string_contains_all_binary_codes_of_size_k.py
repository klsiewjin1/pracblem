class Solution:
    # def hasAllCodes(self, s: str, k: int) -> bool:
    #     holder = []
    #     tmp = 0
    #     while tmp < (2 ** k):
    #         binary = "{:032b}".format(tmp)
    #         holder.append(binary[len(binary) - k:])
    #         tmp += 1
    #     for elem in holder:
    #         if s.find(elem) < 0:
    #             return False
    #     return True

    def hasAllCodes(self, s: str, k: int) -> bool:
        """
        Iterate through s, adding elements of length k into a set
        This determines the number of unique elements within s of length k
        """
        codes = set()
        for i in range(len(s) - k + 1):
            codes.add(s[i:i + k])
        return len(codes) == 2 ** k
