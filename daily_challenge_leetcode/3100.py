class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        bottleDrunk = numBottles
        emptyBottles = numBottles

        while emptyBottles >= numExchange:
            emptyBottles -= numExchange
            numExchange += 1
            bottleDrunk += 1
            emptyBottles += 1
        return bottleDrunk


import math


# Sridhara Acharya’s / quadratic formula
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        return int(
            numBottles
            + (
                (
                    -2 * numExchange
                    + 3
                    + math.sqrt(
                        4 * numExchange * numExchange
                        + 8 * numBottles
                        - 12 * numExchange
                        + 1
                    )
                )
                / 2
            )
        )
