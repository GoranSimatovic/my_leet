class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        
        
        result = 0
        
        
        if dividend == 0:
            return 0
        
        
        dividend_sign = dividend < 0
        divisor_sign = divisor < 0
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        two_ten_divisor = divisor
        for i in range(10):
            two_ten_divisor = two_ten_divisor + two_ten_divisor
        
        
        while dividend >= two_ten_divisor:
            dividend = dividend - two_ten_divisor
            result +=1024
        
        while dividend >= divisor+divisor+divisor+divisor+divisor:
            dividend = dividend - (divisor+divisor+divisor+divisor+divisor)
            result +=5
    
        
        while dividend >= divisor:
            dividend = dividend - divisor
            result +=1
        
        if (dividend_sign and divisor_sign) or (not dividend_sign and not divisor_sign):
            return min(2**31-1, result)
        else:
            return max(-2**31, -result)
                
                
