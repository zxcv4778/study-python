Queue
============

- FIFO ( First In - First Out ) 형태.
- 줄 서있을 때 새치기하면 기분이 나쁘다. 순서를 지켜서 들어온 순서대로 내보내는게 이성적이다.

주요 기능
-------
1. enqueue(item): 아이템을 뒤에 추가한다.
2. dequeue: 맨 앞의 아이템을 지운다.
3. peek: 맨 앞의 아이템을 출력한다.

> 리스트를 이용하여 큐 생성

<pre><code>
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
    
# 출력 결과
1
1
2
False
</code></pre>

> linked list를 이용하여 큐 생성

<pre><code>
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

# 출력 결과
1
2
3
4
Q가 비어있음
None
</code></pre>