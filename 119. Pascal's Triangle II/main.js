/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function (rowIndex) {
  let res = [1];

  for (let i = 1; i < rowIndex + 1; i++) {
    for (let j = 0; j < i - 1; j++) {
      res[j] += res[j + 1];
    }
    res.unshift(1);
  }

  return res;
};
