class FoodRatings {
public:
    unordered_map<string, set<pair<int, string>>> cuisine_ratings_food;
    unordered_map<string, string> food_cuisine;
    unordered_map<string, int> food_rating;
    FoodRatings(vector<string>& foods, vector<string>& cuisines,
                vector<int>& ratings) {
        int n = foods.size();

        for (int i = 0; i < n; i++) {
            string food = foods[i];
            string cuisine = cuisines[i];
            int rating = ratings[i];

            cuisine_ratings_food[cuisine].insert({-rating, food});
            food_cuisine[food] = cuisine;
            food_rating[food] = rating;
        }
    }

    void changeRating(string food, int newRating) {
        string cuisine = food_cuisine[food];
        int oldRating = food_rating[food];

        cuisine_ratings_food[cuisine].erase({-oldRating, food});
        cuisine_ratings_food[cuisine].insert({-newRating, food});
        food_rating[food] = newRating;
    }

    string highestRated(string cuisine) {
        return begin(cuisine_ratings_food[cuisine])->second;
    }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */