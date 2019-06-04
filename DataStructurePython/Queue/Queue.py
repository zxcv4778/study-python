# Array queue


class AQueue:

    queue_list = []

    def enqueue(self, item):
        self.queue_list.append(item)

    def dequeue(self):
        if self.is_empty() is False:
            return self.queue_list.pop(0)
        else:
            print("Q가 비었어욥")
            return None

    def is_empty(self):
        if self.queue_list.__len__() > 0:
            return False
        else:
            return True

    def peek(self):
        print(self.queue_list[0])


if __name__ == "__main__":
    aq = AQueue()

    aq.enqueue(1)
    aq.enqueue(2)
    aq.enqueue(3)
    aq.enqueue(4)
    aq.peek()
    print(aq.dequeue())
    aq.peek()
    print(aq.is_empty())


# list queue

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def enqueue(self, item):
        if self.is_empty() is True:
            self.head = Node(item)
        else:
            new_node = Node(item)

            if self.head.next is None:
                self.head.next = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node

    def dequeue(self):
        if self.is_empty() is True:
            print("Q가 비어있음")
            return None
        else:
            result = self.head.data
            self.head = self.head.next
            return result

    def peek(self):
        print(self.head.data)


if __name__ == "__main__":
    lq = LQueue()
    lq.enqueue(1)
    lq.enqueue(2)
    lq.enqueue(3)
    lq.enqueue(4)
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
