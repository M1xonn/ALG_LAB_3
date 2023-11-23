from Tree import Node, BinaryTree


class AVLNode(Node):
    def __init__(self, data, left: 'AVLNode' = None, right: 'AVLNode' = None):
        super().__init__(data, left, right)


class AVLTree(BinaryTree):
    def __init__(self, root: AVLNode = None):
        super().__init__(root)

    def insert(self, data):
        if self.root is None:
            self.root = AVLNode(data)
        else:
            self.root = self.__insert(data, self.root)

    def __insert(self, data, node: AVLNode):
        if node is None:
            node = AVLNode(data)
        elif data < node.data:
            node.left = self.__insert(data, node.left)
            balance = self.get_balance(node)
            if balance > 1:
                if data < node.left.data:
                    node = self.__rotate_right(node)
                else:
                    node = self.__rotate_left_right(node)
        else:
            node.right = self.__insert(data, node.right)
            balance = self.get_balance(node)
            if balance < -1:
                if data >= node.right.data:
                    node = self.__rotate_left(node)
                else:
                    node = self.__rotate_right_left(node)
        node.height = 1 + max(self.get_height(node.right), self.get_height(node.left))
        return node

    def delete(self, data):
        if self.root is None:
            print('tree is Empty')
            return
        else:
            self.root = self.__delete(data, self.root)

    def __find_replacement(self, node):
        if node is None or node.left is None:
            return node
        return self.__find_replacement(node.left)

    def __delete(self, data, node: AVLNode):
        if node is None:
            return None
        if data < node.data:
            node.left = self.__delete(data, node.left)
        elif data > node.data:
            node.right = self.__delete(data, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            replacement = self.__find_replacement(node.right)
            node.data = replacement.data
            node.right = self.__delete(node.data, node.right)
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        if node.height < 3:
            return node
        balance = self.get_balance(node)
        if balance > 1:
            if data < node.left.data:
                node = self.__rotate_right(node)
            else:
                node = self.__rotate_left_right(node)
        if balance < -1:
            if data >= node.right.data:
                node = self.__rotate_left(node)
            else:
                node = self.__rotate_right_left(node)
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        return node

    def __rotate_left(self, node: AVLNode):
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        right_child.height = 1 + max(self.get_height(right_child.left), self.get_height(right_child.right))
        return right_child

    def __rotate_right(self, node: AVLNode):
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        left_child.height = 1 + max(self.get_height(left_child.left), self.get_height(left_child.right))
        return left_child

    def __rotate_right_left(self, node: AVLNode):
        node.right = self.__rotate_right(node.right)
        return self.__rotate_left(node)

    def __rotate_left_right(self, node: AVLNode):
        node.left = self.__rotate_left(node.left)
        return self.__rotate_right(node)

    def get_height(self, root: AVLNode):
        if root:
            return root.height
        return 0

    def get_balance(self, root: AVLNode):
        if root:
            return self.get_height(root.left) - self.get_height(root.right)
