

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insert_value(self.root, data)
        return self.root is not None

    def insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self.insert_value(node.left, data)
            else:
                node.right = self.insert_value(node.right, data)

        return node

    def find(self, key):
        return self.find_value(self.root, key)

    def find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self.find_value(root.left, key)
        else:
            return self.find_value(root.right, key)

    def delete(self, key):
        self.root, deleted = self.delete_value(self.root, key)
        return deleted

    def delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                parent = node
                child = node.right

                while child.left is not None:
                    parent = child
                    child = child.left

                child.left = node.left

                if parent != node:
                    parent.left = child.right
                    child.right = node.right

                node = child

            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None

        elif key < node.data:
            node.left, deleted = self.delete_value(node.left, key)
        else:
            node.right, deleted = self.delete_value(node.right, key)

        return node, deleted

    def pre_order(self):
        self.__pre_travel(self.root)

    def __pre_travel(self, root):
        if root is None:
            pass
        else:
            print(root.data, end=' ')
            self.__pre_travel(root.left)
            self.__pre_travel(root.right)

    def in_order(self):
        self.__in_travel(self.root)

    def __in_travel(self, root):
        if root is None:
            pass
        else:
            self.__in_travel(root.left)
            print(root.data, end=' ')
            self.__in_travel(root.right)

    def post_order(self):
        self.__post_travel(self.root)

    def __post_travel(self, root):
        if root is None:
            pass
        else:
            self.__post_travel(root.left)
            self.__post_travel(root.right)
            print(root.data, end=' ')

    def level_order(self):
        self.__lv_travel(self.root)

    @staticmethod
    def __lv_travel(root):
        queue = [root]

        while queue:
            root = queue.pop(0)

            if root is not None:
                print(root.data, end=' ')
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)


if __name__ == "__main__":
    arr = [2, 20, 3, 441, 21, 99, 4, 9, 1, 1, 30]

    bst = BinarySearchTree()

    for e in arr:
        bst.insert(e)

    bst.pre_order()
    # bst.in_order()
    # bst.post_order()
    # bst.level_order()


