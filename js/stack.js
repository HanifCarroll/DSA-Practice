class StackNode {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class MyStack {
  constructor(node) {
    this.top = node;
  }

  pop() {
    if (!this.top) throw new Error('Can\'t pop empty stack.');
    const top = this.top.data;
    this.top = this.top.next;
    return top;
  }

  push(data) {
    const node = new StackNode(data);
    node.next = this.top;
    this.top = node;
  }

  peek() {
    if (!this.top) throw new Error('Can\'t peek empty stack.')
    return this.top;
  }

  isEmpty() {
    return Boolean(this.top);
  }
}