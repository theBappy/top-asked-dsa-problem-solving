var threeSum = function (nums) {
  const n = nums.length;
  let res = []
  nums.sort((a, b) => a - b);
  for (let i = 0; i < n - 1; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let left = i + 1,
      right = n - 1;
    while (left < right) {
      let sum = nums[i] + nums[left] + nums[right];

      if(sum === 0){
        res.push([nums[i], nums[left], nums[right]])
        left++
        right--
        while(left < right && nums[left] === nums[left+1]) left++
        while(left < right && nums[right] === nums[right-1]) right--
      }else if(sum < 0){
        left++
      }else{
        right--
      }
    }
  }
  return res
};
