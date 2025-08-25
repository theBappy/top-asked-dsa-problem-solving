class Solution {
public:
    int singleNumber(vector<int>& nums) {
        
        int result = 0;
        
        for(int i = 0; i<32; i++) {
            
            int temp = (1 << i);
            
            int countOne  = 0;
            int countZero = 0;
            
            for(int &num : nums) {
                
                if((num&temp) == 0) {
                    countZero++;
                } else {
                    countOne++;
                }
                
            }
            
            if(countOne % 3 == 1) {
                result = (result | temp);
            }
            
        }
        
        return result;
        
    }
};