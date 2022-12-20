/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function (t) {
  let res = Array(t.length).fill(0);
  let stack = [[0, t[0]]];
  let lenS = 0;

  for (let i = 0; i < t.length; i++) {
    while (lenS != -1 && stack[lenS][1] < t[i]) {
      let n = stack.pop();
      res[n[0]] = i - n[0];
      lenS--;
    }

    stack.push([i, t[i]]);
    lenS++;
  }

  return res;
};
