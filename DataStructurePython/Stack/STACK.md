Stack
==========

- FILO ( First In - Last Out ) 구조.
- 쉽게 생각하자면 프링글스에 들어있는 친구들도 먼저 들어간 순서가 아닌 나중에 들어간 순서대로 꺼내 먹는다.
- 주요 기능으로는 push(데이터 추가), pop(데이터 삭제), peek(마지막 위치에 해당하는 데이터 읽기) 등이 있다.

배열을 이용하여 구현
----------------

<pre><code>
class Stack:
    stackList = []

    def push(self, item):
        self.stackList.append(item)

    def peek(self):
        if self.is_empty() is False:
            print(self.stackList[-1])

    def pop(self):
        if self.is_empty() is False:
            result = self.stackList.pop(-1)
            print(result)
            return result
        else:
            print("Stack is empty.")

    def is_empty(self):
        if self.stackList.__len__() > 0:
            return False
        else:
            return True


</code></pre>

연결 리스트를 이용하여 구현
----------------------

<pre><code>
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class NodeStack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, item):
        if self.head is None:
            self.head = Node(item)
        else:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty() is True:
            print("비어있음")
            return None
        else:
            result = self.head.data
            self.head = self.head.next
            return result

    def peek(self):
        print(self.head.data)
        
     
 </code></pre>
 
 