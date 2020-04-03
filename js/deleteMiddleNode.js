/* Delete Middle Node
   Delete a node in the middle (i.e. not the first or the last node) of a linked list 
   given only acccess to that node.  Don't return anything, just modify the linked list.
*/

function deleteMiddleNode(node) {
  node.data = node.next.data;
  node.next = node.next.next;
}

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

function printLinkedList(node) {
  let current = node;

  while (current !== null) {
    console.log(current.data);
    current = current.next;
  }
}

printLinkedList(a);
console.log('=========');
deleteMiddleNode(c);
printLinkedList(a);