

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0

    def get_height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def is_leaf(self):
        return self.height == 0

    def insert(self, data):
        temp = self.node

        new_node = Node(data)

        if temp is None:
            self.node = new_node
            self.node.left = AVLTree()
            self.node.right = AVLTree()

            print("Inserted" + str(data))

        elif data < temp.data:
            self.node.left.insert(data)

        else:
            self.node.right.insert(data)

        self.rebalance()

    def rebalance(self):
        self.update_balances(False)
        self.update_heights(False)

        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.left_rotate()
                    self.update_heights()
                    self.update_balances()

                self.right_rotate()
                self.update_balances()
                self.update_heights()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.right_rotate()
                    self.update_heights()
                    self.update_balances()

                self.left_rotate()
                self.update_balances()
                self.update_heights()

    def right_rotate(self):
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    def left_rotate(self):
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

    def update_heights(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_heights()
                if self.node.right is not None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height, self.node.right.height) + 1

        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_balances()
                if self.node.right is not None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height

        else:
            self.balance = 0

    def delete(self, data):
        if self.node is not None:
            if self.node.data == data:
                if self.node.left.node is None and self.node.right.node is None:
                    self.node = None
                elif self.node.left.node is None:
                    self.node = self.node.right.node
                elif self.node.right.node is None:
                    self.node = self.node.left.node
                else:
                    replacement = self.logical_successor(self.node)

                    if replacement is not None:
                        self.node.data = replacement.data
                        self.node.right.delete(replacement.data)

                self.rebalance()
                return
            elif data < self.node.data:
                self.node.left.delete(data)
            elif data > self.node.data:
                self.node.right.delete(data)

            self.rebalance()

        else:
            return

    def logical_predecessor(self, node):
        node = node.left.node
        if node is not None:
            while node.right is not None:
                if node.right.node is None:
                    return node
                else:
                    node = node.right.node

        return node

    def logical_successor(self, node):
        node = node.right.node
        if node is not None:
            while node.left is not None:
                if node.left.node is None:
                    return node
                else:
                    node = node.left.node

        return node

    def check_balanced(self):
        if self is None or self.node is None:
            return True

        self.update_heights()
        self.update_balances()

        return (abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced()

    def inorder_traverse(self):
        if self.node is None:
            return []

        inlist = []
        l = self.node.left.inorder_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.node.data)

        l = self.node.right.inorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist

    def display(self, lv=0, pref=' '):
        self.update_balances()
        self.update_heights()

        if self.node is not None:
            print('-' * lv * 2, pref, self.node.data, str(self.height) + ":" + str(self.balance))

            if self.node.left is not None:
                self.node.left.display(lv + 1, "<")
            if self.node.right is not None:
                self.node.right.display(lv + 1, ">")


if __name__ == "__main__":
    avlt = AVLTree()

    inlist = [7, 5, 3, 2, 9, 20, 421, 0]

    for i in inlist:
        avlt.insert(i)

    avlt.display()

    avlt.delete(3)
    avlt.delete(421)

    avlt.display()

