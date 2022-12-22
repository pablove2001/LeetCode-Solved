/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  let menor = x < 0;

  x = Math.abs(x);

  x = "" + x;
  let arr = x.split("");
  arr = arr.reverse();

  x = menor ? -1 : 1;
  x *= parseInt(arr.join(""));

  if (-(2 ** 31) <= x && x <= 2 ** 31 - 1) return x;
  return 0;
};
