// 120, 165, 166, 611, 812, 976, 1039, 2221

var triangularSum = function (nums) {
  let n = nums.length;
  for (let size = n - 1; size >= 1; size--) {
    for (let i = 0; i < size; i++) {
        nums[i] = (nums[i] + nums[i+1]) % 10
    }
  }
  return nums[0]
};
