/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  let len = nums.length;
  if (len == 1) {
    return nums[0];
  }
  if (len == 2) {
    return Math.max(nums[0], nums[1]);
  }

  if (len == 3) {
    return Math.max(nums[0] + nums[2], nums[1]);
  }

  nums[2] = nums[2] + nums[0];

  for (let i = 3; i < nums.length; i++) {
    nums[i] = nums[i] + Math.max(nums[i - 2], nums[i - 3]);
  }

  return Math.max(nums[len - 1], nums[len - 2]);
};
