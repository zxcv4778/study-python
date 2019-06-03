# 배열 스택


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


# 연결 리스트 스택

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


if __name__ == "__main__":
    ns = NodeStack()
    ns.push("a")
    ns.push("b")
    ns.peek()
    ns.push("c")
    # ns.pop()
    ns.peek()
    ns.pop()
    ns.peek()
    ns.pop()
    ns.peek()
