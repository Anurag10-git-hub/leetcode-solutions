class Solution:
    def reverse(self, x: int) -> int:
        reverse =0

        if x<0 :
            sign=-1
        else:
            sign=1

        x=abs(x)

        while x!=0:
            d =x%10
            reverse =reverse *10 +d
            x=x//10

        reverse =reverse *sign
        if reverse>(2**31 -1) or reverse < -(2**31):
            return 0
        return reverse