/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    const map = new Map();

    for (let i = 0; i < nums.length; i++) {
        const e = nums[i];
        if (map.get(e) !== undefined) return [map.get(e), i];
        map.set(target - e, i);
    }
};

/*

for (let i = 0; i < nums.length; i++) {
    const e1 = nums[i];
    for (let j = i + 1; j < nums.length; j++) {
        const e2 = nums[j];
        if (e1 + e2 == target) return [e1, e2];
    }
}
return []; 

*/
