/**
 * @param {number} n
 * @return {number}
 */
var nthUglyNumber = function (n) {
  const arr = new Array(n + 1).fill(0);

  arr[1] = 1;
  
  let i2 = 1,
      i3 = 1,
      i5 = 1;

  for (let i = 2; i <= n; i++) {
    const i2UglyNum = arr[i2] * 2;
    const i3UglyNum = arr[i3] * 3;
    const i5UglyNum = arr[i5] * 5;

    const minUglyNum = Math.min(i2UglyNum, i3UglyNum, i5UglyNum);
    arr[i] = minUglyNum;

    if (minUglyNum === i2UglyNum) i2++;
    if (minUglyNum === i3UglyNum) i3++;
    if (minUglyNum === i5UglyNum) i5++;
  }
  return arr[n];
};
