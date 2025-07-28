class Solution:
    def findNthDigit(self, n: int) -> int:
        length=1
        count=9
        start_num=1

        while n>length*count:
            n-=length*count
            length+=1
            count*=10
            start_num*=10

        target_number=start_num+(n-1)//length
        digit_index_in_num=(n-1)%length
        return int(str(target_number)[digit_index_in_num])
        