class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        if not paths:
            return ""
        
        _dict = dict()
        cities = set()
        
        for path in paths:
            _dict[path[0]] = path[1]
            cities.add(path[0])
            cities.add(path[1])
        
        for city in cities:
            if city not in _dict:
                return city
        
        return ""
