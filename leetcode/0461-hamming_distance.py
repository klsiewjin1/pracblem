class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_str = str(bin(x))[2:]
        x_str = "0" * (32 - len(x_str)) + x_str
        y_str = str(bin(y))[2:]
        y_str = "0" * (32 - len(y_str)) + y_str
        counter = 0
        for i in range(len(x_str)):
            if x_str[i] != y_str[i]:
                counter += 1
        return counter

    def hammingDistance_2(self, x: int, y: int) -> int:
        """
        Running XOR on x and y to get 1s if bits are not equal (difference) and counting them
        """
        return str(x ^ y).count("1")
