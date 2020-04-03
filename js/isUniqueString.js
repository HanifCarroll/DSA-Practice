function isUnique(string) {
  const frequencyTable = {};

  for (let i = 0; i < string.length; i++) {
    if (!frequencyTable[string[i]]) {
      frequencyTable[string[i]] = 1;
    } else {
      return false;
    }
  }

  return true;
}

function isUnique2(string) {
  for (let i = 0; i < string.length - 1; i++) {
    for (let j = i + 1; j < string.length; j++) {
      if (string[i] === string[j]) {
        return false;
      }
    }
  }

  return true;
}

const testString = 'abcdefg';
const testString2 = 'abcdefc';
console.log(isUnique(testString));
console.log(isUnique2(testString));
console.log(isUnique(testString2));
console.log(isUnique2(testString2));