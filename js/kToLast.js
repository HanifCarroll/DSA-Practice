/* Kth to last
   Return the kth to last element of a singly linked list.
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
const d = new Node('d');
const e = new Node('e');
const f = new Node('f');
a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;

function getKToLast(node, k) {
  count = 0;
  slow = node;
  fast = node;

  while (fast) {
    if (count >= k) slow = slow.next;

    fast = fast.next;
    count++;
  }

  return count < k ? null : slow;
}

console.log(getKToLast(a, 3));