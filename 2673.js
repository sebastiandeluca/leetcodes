// Make Costs of Paths Equal in a Binary Tree
// 5ms beats 100%. 62.83MB beats 100%

/**
 * @param {number} n
 * @param {number[]} cost
 * @return {number}
 */
var minIncrements = function(n, cost) {
    ans = 0;
    for (let i = ( n + 1) / 2 - 2; i >= 0; i--) {
        ans += Math.abs(cost[2*i+1] - cost[2*i+2]);
        cost[i] += Math.max(cost[2*i+1], cost[2*i+2]);
    }
    return ans;
};
