class Solution:
    def numSpecialEquivGroups(self, A):
        if not A:
            return 0
        
        d = {}
        
        for word in A:
            odd = []
            even = []
            
            for i,letter in enumerate(word):
                if i % 2 == 0:
                    even.append(letter)
                else:
                    odd.append(letter)
            
            odd = tuple(sorted(odd))
            even = tuple(sorted(even))
            x = tuple([odd,even])
            d[x] = d.get(x,0) + 1
            
        return len(d)
