/* Intersection - Given 2 singly linked lists, determine if they intersect.  If they do, return the
intersecting node (the reference, not the value).  
i.e. If the kth node in the first list is the same as the jth node of the second list, then return that node. */

function areIntersectingLists(list1, list2) {
  let list1Current = list1;
  let list2Current = list2;

  while (list1Current) {
    while (list2Current) {
      if (list1Current === list2Current) return list1Current;
      list2Current = list2Current.next;
    }

    list1Current = list1Current.next;
    list2Current = list2;
  }

  return false;
}

function areIntersectingLists2(list1, list2) {
  const list1LastNode = getLastNode(list1);
  const list2LastNode = getLastNode(list2);
  
  return list1LastNode === list2LastNode ? list1LastNode : false;
}

function getLastNode(list) {
  let current = list;
  while (current.next) {
    current = current.next;
  }

  return current;
}

class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

const list1 = new Node(1);
list1.next = new Node(2);
list1.next.next = new Node(3);
list1.next.next.next = new Node(4);

const list2 = new Node(1);
list2.next = new Node(2);
list2.next.next = new Node(3);
// list2.next.next.next = list1.next.next.next;
list2.next.next.next = new Node(4);

console.log(areIntersectingLists2(list1, list2));