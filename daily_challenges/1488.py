# Tc = O(n.logn)
# Sc =O(n)

from bisect import bisect_left


class Solution:
    def avoidFlood(self, rains):
        n = len(rains)
        lake_map = {}  # lake -> last day it was filled
        dry_days = []  # indices of dry days (rains[day] == 0)
        ans = [1] * n  # default all dry days to dry lake 1

        for day in range(n):
            lake = rains[day]

            if lake == 0:
                dry_days.append(day)  # record this dry day
            else:
                ans[day] = -1  # raining day — can't dry any lake

                if lake in lake_map:
                    # lake already filled previously
                    last_filled = lake_map[lake]
                    # find the next dry day after it was last filled
                    i = bisect_left(dry_days, last_filled + 1)

                    if i == len(dry_days):
                        # no dry day available to empty this lake before raining again → flood
                        return []

                    dry_day = dry_days.pop(i)
                    ans[dry_day] = lake  # use this dry day to dry the lake

                lake_map[lake] = day  # record latest day this lake was filled

        return ans
