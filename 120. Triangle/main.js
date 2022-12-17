/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function (triangle) {
  const lenTri = triangle.length;
  for (let i = 1; i < lenTri; i++) {
    const lenI = triangle[i].length;
    triangle[i][0] += triangle[i - 1][0];
    triangle[i][lenI - 1] += triangle[i - 1][lenI - 2];
    for (let j = 1; j < lenI - 1; j++) {
      triangle[i][j] += Math.min(triangle[i - 1][j - 1], triangle[i - 1][j]);
    }
  }

  return Math.min(...triangle[lenTri - 1]);
};
