/* Partition Linked List
   Partition a linked list around a value x such that all nodes
   less than x come before all nodes greater than or equal to x.
   If x is in the list, x only needs to be after the elements less than X.  
   It can appear anywhere in the "right" partition, not just between the two.
   Ex. 3-5-8-5-10-2-1, partition=5 => 3-1-2-10-5-5-8
*/

function partitionLinkedList(node, partitionValue) {
  const greaterValues = [];
  let count = 1;
  let head = node;
  let prev = null;
  let current = node;
  let tail = null;

  while (current) {
    if (count == 1) {
      if (current.data < partitionValue) {
        prev = current;
        current = current.next;
        count ++;
      } else {
        current.next = null;
        greaterValues.push(current);
        head = current.next;
        current = head;
      }
    } else {
      if (current.data < partitionValue) {
        prev = current;
        current = prev.next;
        count++;
      } else {
        current.next = null;
        greaterValues.push(current);
        prev.next = current.next;
        current = current.next;
        count++;
      }
    }
  }

  tail = prev;

  while (greaterValues.length) {
    const val = greaterValues.shift();
    tail.next = val;
    tail = val;
  }

  return head;
}

class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

const a = new Node(3);
const b = new Node(5);
const c = new Node(8);
const d = new Node(5);
const e = new Node(10);
const f = new Node(2);
const g = new Node(1);
a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;
f.next = g;

function printLinkedList(node) {
  let current = node;
  let string = '';

  while (current !== null) {
    string += `${current.data}-`;
    current = current.next;
  }

  console.log(string);
}

printLinkedList(a);
console.log('=========');
const partitionedList = partitionLinkedList(a, 5);
printLinkedList(partitionedList);