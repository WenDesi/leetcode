class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True

        if num < 4:
            return False

        while num > 4:
            tmp = num & 3
            if tmp != 0:
                return False
            num = num >> 2
        if num == 4:
            return True
        return False