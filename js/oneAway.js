/* One Away
   Given 2 strings, determine if one is '1 edit away' from the other.
   An edit is either removing one character, adding one character, or replacing one character.
   pale, ple -> true
   pale, bake -> false
*/

function isOneAway(string1, string2) {
  if (Math.abs(string1.length - string2.length) > 1) {
    return false;
  }

  const table1 = getFrequencyTable(string1);
  const table2 = getFrequencyTable(string2);
  let differenceCount = 0;
  
  for (letter of Object.keys(table1)) {
    const string1Frequency = table1[letter] || 0;
    const string2Frequency = table2[letter] || 0;
    const difference = Math.abs(string1Frequency - string2Frequency);

    if (difference > 1) {
      return false;
    }

    if (difference === 1) {
      differenceCount++;
    }
  }

  if (differenceCount === 0 || differenceCount > 2) return false;

  return true;
}

function getFrequencyTable(string) {
  const table = {};

  for (letter of string) {
    table[letter] ? table[letter]++ : table[letter] = 1;
  }

  return table;
}

console.log(isOneAway('pale', 'pele'));