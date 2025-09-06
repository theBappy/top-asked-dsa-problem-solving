// Apple

class Solution {
public:
    int pivotInteger(int n) {
        for(int pivot=1; pivot <= n; pivot++){
            int leftSum = 0;
            int rightSum = 0;
            for(int j = 1; j <= pivot; j++){
                leftSum += j;
            }
            for(int j = pivot; j <= n; j++){
                rightSum += j;
            }
            if(leftSum == rightSum){
                return pivot;
            }
        }
        return -1;
    }
};



class Solution {
public:
    int pivotInteger(int n) {
        int totalSum = n * (n + 1) / 2;
        for (int pivot = 1; pivot <= n; pivot++) {
            int leftSum = pivot * (pivot + 1) / 2;
            int rightSum = totalSum - leftSum + pivot;
            if (leftSum == rightSum) {
                return pivot;
            }
        }
        return -1;
    }
};


class Solution {
public:
    int pivotInteger(int n) {
        int i = 1; 
        int j = n;
        int leftSum = 1;
        int rightSum = n;
        while(i < j){
            if(leftSum < rightSum){
                i++;
                leftSum += i;
            }else{
                j--;
                rightSum += j;
            }
        }
        return leftSum == rightSum ? i : -1;
    }
};


class Solution {
public:
    int pivotInteger(int n) {
        int totalSum = n * (n + 1) / 2;
        int pivot = sqrt(totalSum);

        if (pivot * pivot == totalSum) {
            return pivot;
        }
        return -1;
    }
};



class Solution {
public:
    int pivotInteger(int n) {
        int totalSum = n * (n + 1) / 2;
        int left = 1;
        int right = n;
        while (left <= right) {
            int mid_pivot = left + (right - left) / 2;
            if (mid_pivot * mid_pivot == totalSum) {
                return mid_pivot;
            } else if (mid_pivot * mid_pivot < totalSum) {
                left = mid_pivot + 1;
            } else {
                right = mid_pivot - 1;
            }
        }
        return -1;
    }
};
