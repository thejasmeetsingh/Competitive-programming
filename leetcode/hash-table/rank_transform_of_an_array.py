class Solution:
    def arrayRankTransform(self, arr: list) -> list:
        if not arr:
            return []
        
        if len(set(arr)) == 1:
            return [1] * len(arr)
        
        sorted_arr = sorted(arr)
        rank_el_map = dict()
        rank = 0

        for element in sorted_arr:
            if element not in rank_el_map:
                rank += 1
                rank_el_map[element] = rank

        return [rank_el_map[el] for el in arr]
