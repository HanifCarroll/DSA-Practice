function isPermutation(str1, str2) {
  if (str1.length <= 1
    || str2.length <= 1
    || str1.length !== str2.length
    || str1 === str2
    ) {
    return false;
  }

  const table1 = {};
  const table2 = {};

  for (let i = 0; i < str1.length; i++) {
    if (!table1[str1[i]]) table1[str1[i]] = 1
    else table1[str1[i]]++

    if (!table2[str2[i]]) table2[str2[i]] = 1
    else table2[str2[i]]++
  }

  const table1Keys = Object.keys(table1).sort();
  const table2Keys = Object.keys(table2).sort();

  if (!arraysAreEqual(table1Keys, table2Keys)) return false;

  for (key of table1Keys) {
    if (table1[key] !== table2[key]) return false;
  }

  return true;
}

function arraysAreEqual(arr1, arr2) {
  for (let i = 0; i < arr1.length; i++) {
    if (arr1[i] !== arr2[i]) {
      return false;
    }
  }

  return true;
}

console.log(isPermutation('qpwoeiruty', 'quwieorpty'));