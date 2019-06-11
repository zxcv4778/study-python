import heapq
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

        return self.queue_list[0]


# if __name__ == "__main__":
# aq = AQueue()
#
# aq.enqueue(1)
# aq.enqueue(2)
# aq.enqueue(3)
# aq.enqueue(4)
#
# while not aq.is_empty():
#     print(aq.dequeue())


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
        if self.is_empty() is True:
            return None

        print(self.head.data)

        return self.head.data


# if __name__ == "__main__":
# lq = LQueue()
# lq.enqueue(1)
# lq.enqueue(2)
# lq.enqueue(3)
# lq.enqueue(4)
#
# while not lq.is_empty():
#     print(lq.dequeue(), end=' ')


# Circular queue


class CircularQ:
    def __init__(self, max_idx):
        self.max = max_idx
        self.c_list = [None] * self.max
        self.size = self.rear = self.front = 0

    def is_full(self):
        return (self.rear + 1) % self.max == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Q가 꽉 찼어욥!")
        else:
            self.rear = (self.rear + 1) % self.max
            self.c_list[self.rear] = item
            self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Q가 비어있어욥!")
            return None
        else:
            self.front = (self.front + 1) % self.max
            result = self.c_list[self.front]
            self.c_list[self.front] = None
            self.size -= 1

            return result

    def peek(self):
        if self.size == 0:
            print("Q가 비어있어욥!")
            return None

        return self.c_list[self.front]


# if __name__ == "__main__":
# cq = CircularQ(4)
# cq.enqueue('a')
# cq.enqueue('b')
# cq.enqueue('c')
# cq.enqueue('d')
# cq.enqueue('e')
# cq.enqueue('f')

# while cq.size != 0:
#     print(cq.dequeue(), end=' ')


# priority queue

if __name__ == "__main__":
    pq = []
    heapq.heappush(pq, (3, 'a'))
    heapq.heappush(pq, (4, 'b'))
    heapq.heappush(pq, (1, 'c'))
    heapq.heappush(pq, (100, 'd'))

    print(pq)

    while pq.__len__() > 0:
        print(heapq.heappop(pq))
