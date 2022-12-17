/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function (numRows) {
  let res = [[1]];

  for (let i = 1; i < numRows; i++) {
    res.push([1]);
    for (let j = 0; j < i - 1; j++) {
      res[i].push(res[i - 1][j] + res[i - 1][j + 1]);
    }
    res[i].push(1);
  }

  return res;
};
