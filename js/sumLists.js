/* Sum Lists - A number is represented as a linked list where each node contains a digit.  The nodes are stored in reverse order so that 7->1->6 = 617.
Given 2 numbers, add them, and return the total.
7-1-6 + 5-9-2 corresponds to 617 + 295.  The answer is 912, so return 2-1-9. */

class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

const a = new Node(7);
a.next = new Node(1);
a.next.next = new Node(6);
const b = new Node(5);
b.next = new Node(9);
b.next.next = new Node(2);

console.log(sum2Lists(a, b));

function sum2Lists(a, b) {
  const num1 = revListToNum(a);
  const num2 = revListToNum(b);
  return strToRevList((num1 + num2).toString());
}

function revListToNum(node) {
  const arr = [];
  let current = node;

  while (current) {
    arr.push(current.data);
    current = current.next;
  }

  let result = '';

  // for (let i = arr.length - 1; i >= 0; i--) {
  for (let i = 0; i < arr.length; i++) {
    result += arr[i].toString();
  }

  return parseInt(result);
}

function strToRevList(string) {
  if (!string || !string.length) { return null; }

  const arr = [];

  // for (let i = string.length - 1; i >= 0; i--) {
  for (let i = 0; i < string.length; i++) {
    arr.push(new Node(string[i]));
  }

  const head = arr.shift();
  let current = head;
  
  while (arr.length) {
    const val = arr.shift();
    current.next = val;
    current = val;
  }

  return head;
}