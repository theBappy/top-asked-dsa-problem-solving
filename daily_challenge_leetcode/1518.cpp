
// Tc = O(numBottles) // O(n)
// Sc = O(1)
class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int consumed = 0;
        while (numBottles >= numExchange) {
            consumed += numExchange;
            numBottles -= numExchange;
            numBottles += 1;
        }
        return consumed + numBottles;
    }
};

// Tc = O(log.n)
class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int consumed = numBottles;
        int emptyBottles = numBottles;
        while (emptyBottles >= numExchange) {
            int extraFullBottles = emptyBottles / numExchange;
            int remain = emptyBottles % numExchange;
            consumed += extraFullBottles;
            emptyBottles = remain + extraFullBottles;
        }
        return consumed;
    }
};

// Tc = O(1)
class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        return numBottles + ((numBottles - 1) / (numExchange - 1));
    }
};