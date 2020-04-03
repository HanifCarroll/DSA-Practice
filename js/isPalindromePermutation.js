/* Given a string, check if it's a permutation of a palindrome, not limited to real words.
   ex. tact coa should return true because it can be rearranged to atco cta
*/

function isPalindromePermutation(str) {
  const string = str.split(' ').join('');
  const isEvenLength = string.length % 2 === 0;
  const frequencyTable = getFrequencyTable(string);
  const tableValues = Object.values(frequencyTable);

  if (isEvenLength) {
    for (let i = 0; i <= tableValues.length; i++) {
      if (tableValues[i] % 2) return false;
    }
  } else {
    let oddCount = 0;
    for (let i = 0; i <= tableValues.length; i++) {
      if (tableValues[i] % 2) oddCount++;
    }
    if (oddCount !== 1) return false;
  }

  return true;
}

function getFrequencyTable(string) {
  const table = {};

  for (let i = 0; i < string.length; i++) {
    if (!table[string[i]]) table[string[i]] = 1;
    else table[string[i]]++;
  }
  
  return table;
}

console.log(isPalindromePermutation('tacta'));