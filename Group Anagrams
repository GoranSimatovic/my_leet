class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        def are_same(x,y):
            return sorted(x) == sorted(y)

        output_list = []

        counter = 0

        for word_length in set([len(x) for x in strs]):

            temp_strs = [x for x in strs if len(x) == word_length]

            while temp_strs != []:
                round_list = []

                for i in temp_strs:

                    if round_list == []:
                        round_list.append(i)
                        continue
                    elif are_same(round_list[0], i):
                        round_list.append(i)

                output_list.append(round_list)
                temp_strs = [x for x in temp_strs if x not in round_list]

        return output_list
