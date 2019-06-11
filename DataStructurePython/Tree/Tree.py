# binary tree


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def make_left(self, item):
        new_node = item
        self.left = new_node

    def make_right(self, item):
        new_node = item
        self.right = new_node

    def get_data(self):
        print(self.data)

    def get_left(self):
        print(self.left.data)

    def get_right(self):
        print(self.right.data)


if __name__ == "__main__":
    t = TreeNode(1)
    t1 = TreeNode(2)
    t2 = TreeNode(3)
    t3 = TreeNode(4)

    t.make_left(t1)
    t.make_right(t2)
    t1.make_right(t3)

    t.get_right()
    t.get_left()

    t1.get_right()


