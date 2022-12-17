/**
 * @param {number[][]} matrix
 * @return {number}
 */
var minFallingPathSum = function (matrix) {
  for (let i = 1; i < matrix.length; i++) {
    for (let j = 0; j < matrix[0].length; j++) {
      let min = matrix[i - 1][j];
      if (j - 1 >= 0) {
        min = Math.min(min, matrix[i - 1][j - 1]);
      }
      if (j + 1 < matrix[0].length) {
        min = Math.min(min, matrix[i - 1][j + 1]);
      }
      matrix[i][j] += min;
    }
  }

  return Math.min(...matrix[matrix.length - 1]);
};
