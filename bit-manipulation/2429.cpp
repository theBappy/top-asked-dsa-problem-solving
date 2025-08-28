/*
# Netflix, Instagram

# Facts needs to solve this problem
# Unset bit to Set
# num | (1 << bit)

# Set bit to Unset
# num = num & (~(1 << bit))

# Check if a bit is set
# num = num & (1 << i)

# Approach-1
# Tc = O(log.n)
# Sc = O(1)

*/
class Solution {
public:
    bool isSet(int &x, int bit){
        return x & (1 << bit);
    }
    bool setBit(int &x, int bit){
        return x |= (1 << bit);
    }
    bool unsetBit(int &x, int bit){
        return x &= ~(1 << bit);
    }
    int minimizeXor(int num1, int num2) {
        int x = num1;

        int requiredSetbitsCount = __builtin_popcount(num2);
        int currentSetbitsCount = __builtin_popcount(x);

        int bit = 0; // position of bit
        if (currentSetbitsCount < requiredSetbitsCount) {
            while (currentSetbitsCount < requiredSetbitsCount) {
                if (!isSet(x, bit)) {
                    setBit(x, bit);
                    currentSetbitsCount++;
                }
                bit++;
            }
        } else if (currentSetbitsCount > requiredSetbitsCount) {
            while (currentSetbitsCount > requiredSetbitsCount) {
                if (isSet(x, bit)) {
                    unsetBit(x, bit);
                    currentSetbitsCount--;
                }
                bit++;
            }
        }
        return x;
    }
};


// Approach-2
// insert bit from most significant position
// insert where num1 has set bit -> cancel out each other
// Tc = O(log.n) => for loop is running 31 times constant O(1) can be said and built_inpopcount -> log.n
// Sc = O(1)
class Solution {
public:
    bool isSet(int &x, int bit) {
        return x & (1 << bit);
    }

    bool setBit(int &x, int bit) {
        return x |= (1 << bit);
    }

    bool isUnset(int x, int bit) {
        return (x & (1 << bit)) == 0;
    }

    int minimizeXor(int num1, int num2) {
        int x = 0;

        int requiredSetBitCount = __builtin_popcount(num2);

        for(int bit = 31; bit >= 0 && requiredSetBitCount > 0; bit--) {
            if(isSet(num1, bit)) {
                setBit(x, bit); //Or you can write x |= (1 << bit);
                requiredSetBitCount--;
            }
        }

        for(int bit = 0; bit < 32 && requiredSetBitCount > 0; bit++) {
            if(isUnset(num1, bit)) {
                setBit(x, bit); //Or you can write x |= (1 << bit);
                requiredSetBitCount--;
            }
        }

        return x;
        
    }
};
