class SSLNode {
    constructor(val) {
        this.value = val;
        this.next = null;
    }
}

// Add Front
class SLL {
    constructor() {
        this.head = null;
    }
    addFront(value) {
        var newnode = new SSLNode(value);
        newnode.next = this.head;
        this.head = newnode;
    }
    removeFront() {
        if (this.head == null) {
            return this.head;
        }
        var removeNode = this.head;
        this.head = removeNode.next;
        removeNode.next = null;
        return this.head;
    }
 }


var SLL1 = new SLL()
SLL1.addFront(18) 
SLL1.addFront(5)
SLL1.addFront(73)

console.log(SLL1)

// => Node { data: 18, next: null }
// => Node { data: 5, next: Node { data: 18, next: null } }
// => Node { data: 73, next: Node { data: 5, next: Node { data: 18, next: null } } }

// Remove Front

 SLL1.removeFront() 
 console.log(SLL1)
 SLL1.removeFront()
 console.log(SLL1)
 
//  => Node { data: 5, next: Node { data: 18, next: null } }
//  => Node { data: 18, next: null }