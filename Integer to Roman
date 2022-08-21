class Solution:
    def intToRoman(self, num: int) -> str:

        translator_dict = {
            1000:'M',
            900:'CM',
            500:'D',
            400:'CD',
            100:'C',
            90:'XC',
            50:'L',
            40:'XL',
            10:'X',
            9:'IX',
            5:'V',
            4:'IV',
            1:'I'
        }

        # max number of occurances
        n_occurances_dict = {
            'I':3,
            'V':1,
            'IV':1,
            'IX':1,
            'X':3,
            'XL':1,
            'L':1,
            'XC':1,
            'C':3,
            'CD':1,
            'D':1,
            'CM':1,
            'M':3
        }

        rom_text = ''
        for div_num in list(translator_dict.keys()):
            division = num/div_num 
            whole = int(division)
            if whole >= 1 and whole <= n_occurances_dict[translator_dict[div_num]]:
                num = num - whole*div_num
                rom_text = rom_text + whole*translator_dict[div_num]

        return rom_text
