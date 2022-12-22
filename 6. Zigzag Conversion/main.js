/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function (s, numRows) {
  let arr = [];
  for (let i = 0; i < numRows; i++) arr.push("");

  const modulo = numRows + Math.max(numRows - 2, 0);

  for (let i = 0; i < s.length; i++) {
    let lugar = i % modulo;
    if (numRows <= lugar) lugar = numRows - 2 - (lugar % numRows);
    arr[lugar] += s[i];
  }

  return arr.join("");
};
