class Solution:
    def reverse(self, x: int) -> int:
        
        if x == 0:
            return 0
        

        x_str = str(x)
        x_str = x_str[::-1]

        while x_str[0] == '0':
            x_str = x_str[1:]

        if x_str[-1] == '-':
            x_str = '-' + x_str[:-1]

        reversed_x = int(x_str)
        
        if reversed_x > 2147483647 or reversed_x< -2147483648:
            return 0
        
        return int(x_str)
