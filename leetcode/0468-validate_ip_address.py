class Solution:
    def validIPAddress(self, IP: str) -> str:
        def isIPv4(s: str):
            try:
                return str(int(s)) == s and 0 <= int(s) <= 255
            except:
                return False

        def isIPv6(s: str):
            try:
                if len(s) > 4:
                    return False
                int(s, 16)
                return True
            except:
                return False

        if IP.count(".") == 3 and all(isIPv4(s) for s in IP.split(".")):
            return "IPv4"
        elif IP.count(":") == 7 and all(isIPv6(s) for s in IP.split(":")):
            return "IPv6"
        else:
            return "Neither"
