/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function (cost) {
  let len = cost.length;

  for (let i = 2; i < len; i++) {
    if (cost[i - 1] < cost[i - 2]) {
      cost[i] = cost[i] + cost[i - 1];
    } else {
      cost[i] = cost[i] + cost[i - 2];
    }
  }

  if (cost[len - 1] < cost[len - 2]) {
    return cost[len - 1];
  } else {
    return cost[len - 2];
  }
};
