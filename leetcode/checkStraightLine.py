'''
Check If It Is a Straight Line
You are given an array coordinates, coordinates[i] = [x, y],
where [x, y] represents the coordinate of a point.
Check if these points make a straight line in the XY plane.
'''


class Solution:
    def checkStraightLine(self, coordinates: List) -> bool:
        nums = len(coordinates)
        if nums <= 2:
            return True
        else:
            x1 = coordinates[1][0]
            x0 = coordinates[0][0]

            collinearity = x0 == x1

            for i in range(2, len(coordinates)):
                if not collinearity:
                    slope = (coordinates[1][1] - coordinates[0][1]) / (x1 - x0)
                    intercept = coordinates[1][1] - slope * coordinates[1][0]
                    values_expected = (slope * coordinates[i][0] + intercept)
                    real_v = coordinates[i][1]
                else:
                    real_v = x1
                    values_expected = coordinates[i][0]

                if real_v != values_expected:
                    return False

            return True
