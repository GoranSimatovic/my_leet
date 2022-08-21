class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
                
        phone_dict = {
            '1':[''],
            '2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z'],
            '0':[' ']
        }
        
        
        res = []

        for i in digits:
            
            if res == []:
                res = phone_dict[i]
                continue
            
            temp_res = []
            for j in phone_dict[i]:
                temp_res = temp_res + [(x+j) for x in res]
            
            res = temp_res
            
        return res
