/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function (tokens) {
  let stack = [];

  for (let i = 0; i < tokens.length; i++) {
    if (tokens[i] == "+") {
      num1 = stack.pop();
      num2 = stack.pop();
      stack.push(num2 + num1);
    } else if (tokens[i] == "-") {
      num1 = stack.pop();
      num2 = stack.pop();
      stack.push(num2 - num1);
    } else if (tokens[i] == "*") {
      num1 = stack.pop();
      num2 = stack.pop();
      stack.push(num2 * num1);
    } else if (tokens[i] == "/") {
      num1 = stack.pop();
      num2 = stack.pop();
      stack.push(parseInt(num2 / num1));
    } else {
      stack.push(parseInt(tokens[i]));
    }
  }

  return stack.pop();
};
