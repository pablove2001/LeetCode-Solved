/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function (n) {
  if (n <= 1) {
    return n;
  }

  let n1 = 0;
  let n2 = 1;
  let n3 = 1;

  for (let i = 0; i < n - 2; i++) {
    let presta = n1;
    n1 = n2;
    n2 = n3;
    n3 = n2 + n1 + presta;
  }

  return n3;
};
