/* String Compression
   Count the repetitions of the characters.  
   Ex. 'aabccccaaa' -> a2b1c4a3
   If the 'compressed' string is not smaller than the original, return the original.
*/

function stringCompression(originalString) {
  if (originalString == '') { return originalString; }

  let compressedString = '';
  let prevLetter = originalString[0];
  let count = 0;

  for (letter of originalString) {
    if (letter === prevLetter) {
      count++;
    } else {
      compressedString += `${prevLetter}${count}`;
      count = 1;
      prevLetter = letter;
    }
  }
  compressedString += `${prevLetter}${count}`;

  return compressedString.length < originalString.length
    ? compressedString
    : originalString;
}

console.log(stringCompression('aabccccaaa'));