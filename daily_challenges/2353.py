from collections import defaultdict
import heapq

class FoodRatings(object):
    def __init__(self, foods, cuisines, ratings):
        self.food_cuisine = {}
        self.food_rating = {}
        self.cuisine_heap = defaultdict(list)  # cuisine -> heap of (-rating, food)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_cuisine[food] = cuisine
            self.food_rating[food] = rating
            heapq.heappush(self.cuisine_heap[cuisine], (-rating, food))

    def changeRating(self, food, newRating):
        cuisine = self.food_cuisine[food]
        self.food_rating[food] = newRating
        # Push the new rating onto the heap
        heapq.heappush(self.cuisine_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        heap = self.cuisine_heap[cuisine]
        # Pop outdated entries
        while heap:
            rating, food = heap[0]
            # Check if the rating matches current rating
            if -rating == self.food_rating[food]:
                return food
            else:
                heapq.heappop(heap)
        return None  # If no food found (should not happen if input is valid)
