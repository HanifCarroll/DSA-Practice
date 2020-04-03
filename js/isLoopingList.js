/* Loop Detection - Given a circular linked list, return the node at the beginning of the loop.
In - A-B-C-D-E-C
Out - C */

class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

const a = new Node('a');
a.next = new Node('b');
a.next.next = new Node('c');
a.next.next.next = new Node('d');
a.next.next.next.next = new Node('e');
// a.next.next.next.next.next = a.next.next;
a.next.next.next.next.next = new Node('f');

console.log(isLoopingList(a));

function isLoopingList(node) {
  const seen = [];
  let current = node;

  while (current) {
    if (seen.includes(current)) return current;
    seen.push(current);
    current = current.next;
  }
  return null;
}
