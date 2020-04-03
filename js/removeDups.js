/* Remove duplicates from an unsorted linked list.
   Ex. Given 1->2->3->2->4, return 1->2->3->4
*/

class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

const a = new Node('a');
const b = new Node('b');
const c = new Node('c');
const a2 = new Node('a');
const d = new Node('d');
a.next = b;
b.next = c;
c.next = a2;
a2.next = d;

function removeDuplicates(node) {
  const unique = [];
  let current = node;
  let prev = null;

  while (current) {
    if (unique.includes(current.data)) {
      prev.next = current.next;
      current = current.next;
    } else {
      unique.push(current.data);
      const temp = current;
      prev = current;
      current = temp.next;
    }
  }
  console.log('unique', unique);
}

function printLinkedList(node) {
  let current = node;

  while (current !== null) {
    console.log(current.data);
    current = current.next;
  }
}
printLinkedList(a);
console.log('=================================');
removeDuplicates(a);
printLinkedList(a);