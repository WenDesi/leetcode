import re
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_str = str(num)[::-1]
        print_list = ['','','Hundred','Thousand','','Hundred','Million','','Hundred','Billion','']
        ww = []

        for i in range(len(num_str)):
            print_tmp = print_list[i]
            if print_tmp != '':
                ww.append(print_tmp)
            ww.append(num_str[i])

        tt = ww[::-1]
        wds = ' '.join(tt)

        print wds

        wds = wds.replace('0 Hundred 0 0 Thousand','')
        wds = wds.replace('0 Hundred','')
        wds = wds.replace('0 Million','')

        wds = wds.replace('1 0','Ten')
        wds = wds.replace('1 1','Eleven')
        wds = wds.replace('1 2','Twelve')
        wds = wds.replace('1 3','Thirteen')
        wds = wds.replace('1 4','Fourteen')
        wds = wds.replace('1 5','Fifteen')
        wds = wds.replace('1 6','Sixteen')
        wds = wds.replace('1 7','Seventeen')
        wds = wds.replace('1 8','Eighteen')
        wds = wds.replace('1 9','Nineteen')

        wds = wds.replace('0 0','')
        wds = wds.replace('0 1','One')
        wds = wds.replace('0 2','Two')
        wds = wds.replace('0 3','Three')
        wds = wds.replace('0 4','Four')
        wds = wds.replace('0 5','Five')
        wds = wds.replace('0 6','Six')
        wds = wds.replace('0 7','Seven')
        wds = wds.replace('0 8','Eight')
        wds = wds.replace('0 9','Nine')

        print wds

        llist = wds.split(' ')

        i = 0
        trans = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
        trans_s = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        while i < len(llist):
            try:
                int_i = int(llist[i])
            except:
                i += 1
                continue

            try:
                int_i_next = int(llist[i+1])
            except:
                llist[i] = trans[int_i]
                i += 1
                continue

            llist[i] = trans_s[int_i]
            if int_i_next != 0:
                llist[i+1] = trans[int_i_next]
            else:
                llist[i+1] = ''
            i += 2

        wds = ' '.join(llist)
        wds = re.sub(" +$",'',wds)
        wds = re.sub(" +", " ", wds)
        return wds

if __name__ == '__main__':
    fs = [-4,-3,-2]
    wds = Solution()
    print wds.numberToWords(2147483647)



