class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict_s = {}
        dict_t = {}

        for char in t:
            if char not in dict_t:
                dict_t[char] = 1
            else:
                dict_t[char] += 1

        for char in s:
            dict_s[char] = 0

        left = 0
        right = -1
        total = 0
        t_len = len(t)
        s_len = len(s)
        mmin = None
        mmin_len = 2147483647
        while right < s_len:
            if total == t_len:
                if right-left+1 < mmin_len:
                    mmin = s[left:right+1]
                    mmin_len = right-left+1
                char = s[left]

                if char in dict_t:
                    dict_s[char] -= 1
                    if dict_s[char] < dict_t[char]:
                        total -= 1
                left += 1

            elif total < t_len:
                right += 1
                if right >= s_len:
                    break
                char = s[right]
                if char in dict_t:
                    dict_s[char] += 1
                    if dict_s[char] <= dict_t[char]:
                        total += 1
            else:
                char = s[left]
                if char in dict_t:
                    dict_s[char] -= 1
                    if dict_s[char] >= 0:
                        total -= 1
                    else:
                        dict_s[char] = 0
                left += 1
        if mmin:
            return mmin
        return ""

if __name__ == '__main__':
    wds= Solution()
    print wds.minWindow('adobecodebancbbcaa','abc')

