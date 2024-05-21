/**
 * Checks if a given string is a valid palindrome
 * @param {string} s - The input string to be checked
 * @ returns {boolean} - True if hte string is a valid palindrome, false otherwise
 */
const isPalindrome = (s) => {
  // Remove non-alphanumeric characters and convert to lowercase
  s = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();

  left = 0;
  right = s.length - 1;

  while (left < right) {
    if (s[left] !== s[right]) {
	  return false;
    }
    left++;
    right--;
  }
  return true;
};

console.log(isPalindrome('A man, a plan. a canal: Panama'));
console.log(isPalindrome('race a car'));
console.log(isPalindrome('Was it a car or a cat i saw?'));
