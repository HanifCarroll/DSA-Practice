/* Palindrome - Check if a linked list is a palindrome. */

class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

const a = new Node(1);
a.next = new Node(2);
a.next.next = new Node(3);
a.next.next.next = new Node(2);
// a.next.next.next = new Node(3);
a.next.next.next.next = new Node(1);

console.log(isPalindromeLinkedList(a));

function isPalindromeLinkedList(node) {
  const string = linkedListToString(node);

  for (let i = 0, j = string.length - 1; i <= j; i++, j--) {
    if (string[i] !== string[j]) return false
  }

  return true;
}

function linkedListToString(node) {
  if (!node) return '';

  let string = '';
  let current = node;

  while (current) {
    string += current.data.toString();
    current = current.next;
  }

  return string;
}
