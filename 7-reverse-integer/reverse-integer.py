class Solution(object):
    def reverse(self, x):
        min = -2147483648
        max = 2147483647

        sign = -1 if x < 0 else 1
        x = abs(x)

        res = 0

        while x != 0:
            digit = x % 10
            x //= 10

            if res > max // 10:
                return 0

            res = res * 10 + digit

        res = res * sign

        if res < min or res > max:
            return 0

        return res