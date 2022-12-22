/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  if (x < 0) return false;

  x = x.toString();

  let m = parseInt(x.length / 2);
  for (let i = 0; i < m; i++) if (x[i] != x[x.length - 1 - i]) return false;
  return true;
};
