/**
 * @param {number[]} tasks
 * @return {number}
 */
var minimumRounds = function (tasks) {
    let d = {};
    let res = 0;

    for (const i of tasks) d[i] = d[i] + 1 || 1;

    for (let i of Object.values(d)) {
        if (i <= 1) return -1;
        res += Math.floor((i + 2) / 3);
    }

    return res;
};