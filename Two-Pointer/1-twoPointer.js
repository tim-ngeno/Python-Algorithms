// Two-pointer algorithm in javascript

const twoPointer = (lst, target) => {
  let start = 0;
  let end = lst.length - 1;

  while (start < end) {
    const left = lst[start];
    const right = lst[end];

    const sum = left + right;

    if (sum === target) {
      return [left, right];
    } else if (sum < target) {
      start += 1;
    } else if (sum > target) {
      end -= 1;
    }
  }
  return 'No pair found';
};

const arr = [1, 3, 4, 5, 7, 8, 9, 12];
const sum = 12;
console.log(twoPointer(arr, sum));
