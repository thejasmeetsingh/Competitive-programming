class Solution:
    def leastBricks(self, wall: list) -> int:
        sum_map, max_sum = {}, 0
        for i in range(len(wall)):
            curr_sum = 0
            for j in range(len(wall[i])-1):
                curr_sum += wall[i][j]
                if curr_sum not in sum_map:
                    sum_map[curr_sum] = 0
                sum_map[curr_sum] += 1
                max_sum = max(max_sum, sum_map[curr_sum])
        return len(wall) - max_sum
