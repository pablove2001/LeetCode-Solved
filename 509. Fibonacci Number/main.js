/**
 * @param {number} n
 * @return {number}
 */
var fib = function (n) {
  if (n <= 1) {
    return n;
  }
  let n1 = 0;
  let n2 = 1;

  for (let i = 0; i < n - 1; i++) {
    let pass = n1;
    n1 = n2;
    n2 = n1 + pass;
  }

  return n2;
};
