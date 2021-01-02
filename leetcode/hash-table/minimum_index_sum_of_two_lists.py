class Solution:
    def findRestaurant(self, list1: list, list2: list) -> list:
        common_interests = {}
        total_array = list1 + list2
        min_index = float("inf")
        result_name = []

        for idx, value in enumerate(total_array):
            if value not in common_interests:
                common_interests[value] = idx
            else:
                common_interests[value] += idx
                if common_interests[value] < min_index:
                    min_index = common_interests[value]
                    result_name = [value]
                elif common_interests[value] == min_index:
                    result_name.append(value)

        return result_name