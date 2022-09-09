Add Front

class SLL {
// constructor, other methods, removed for brevity
    addFront(value) {
        
    }
}

SLL1 = new SLL()
SLL1.addFront(18) => Node { data: 18, next: null }
SLL1.addFront(5) => Node { data: 5, next: Node { data: 18, next: null } }
SLL1.addFront(73) => Node { data: 73, next: Node { data: 5, next: Node { data: 18, next: null } } }


Remove Front

class SLL {
    // constructor, other methods, removed for brevity
    removeFront() {
    	
    }
 }

 SLL1.removeFront() => Node { data: 5, next: Node { data: 18, next: null } }
 SLL1.removeFront() => Node { data: 18, next: null }

Front
class SLL {
    // constructor, other methods, removed for brevity
    front() {
    	
    }
 }

 SLL1.front() => 18
 SLL1.removeFront() => null
 SLL1.front() => null