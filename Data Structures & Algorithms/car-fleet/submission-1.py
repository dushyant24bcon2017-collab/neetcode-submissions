class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pos_to_speed = [0] * target
        for p, s in zip(position, speed):
            pos_to_speed[p] = s

        fleets = 0
        max_time = 0.0
        for pos in range(target - 1, -1, -1):  # walk from target backward
            s = pos_to_speed[pos]
            if s == 0:
                continue  # no car at this position
            time = (target - pos) / s
            if time > max_time:
                fleets += 1
                max_time = time
        return fleets