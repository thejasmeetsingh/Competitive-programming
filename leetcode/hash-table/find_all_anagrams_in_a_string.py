class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        if len(p) > len(s):
            return []
        result = []
        hash_of_p = sum(hash(x) for x in p)
        current_hash = 0

        for x in s[:len(p)]:
            current_hash += hash(x)
        if current_hash == hash_of_p:
            result.append(0)

        for i, x in enumerate(s[len(p):]):
            current_hash += hash(x) - hash(s[i])
            if current_hash == hash_of_p:
                result.append(i+1)
        return result