class SSLNode {
    constructor(val) {
        this.value = val;
        this.next = null;
    }
}

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
    display() {
        var listStr = "";
        if (this.head == null) {
            return listStr;
        }
        listStr += this.head.value;
        var runner = this.head.next;
        while (runner != null) {
            listStr += "," + runner.value;
            runner = runner.next;
        }
        return listStr;
    }
 }




//  Examples:
SLL1 = new SLL()
SLL1.addFront(76)
SLL1.addFront(2)
console.log(SLL1.display())
// SLL1.addFront(11.41) => Node { data: 11.41, next: Node { data: 2, next: Node { data: 76, next: null } } }
// SLL1.display() => "11.41, 2, 76"