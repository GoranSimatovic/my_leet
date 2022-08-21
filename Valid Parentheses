class Solution:
    def isValid(self, s: str) -> bool:
        
        s_len = len(s)
        
        if s_len%2 !=0:
            return False
        
        brackets = ['()', '[]', '{}']
        
        for i in range(int(s_len/2)):
            for b in brackets:
                s = s.replace(b,'')
                
        if s == '':
            return True
        else:
            return False
            
