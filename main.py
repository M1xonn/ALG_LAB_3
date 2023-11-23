import random
from Tree import Node, BinaryTree
from AVLTree import AVLTree


def binary_to_AVL(root: Node):
    data = []
    dfs(root, data)
    return data


def dfs(root: Node, data):
    if root:
        data.append(root.data)
        dfs(root.left, data)
        dfs(root.right, data)


def parse(tree_str):
    stack = []
    buffer = ''
    symbols = ('(', ' ', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    root = None
    for elem in tree_str:
        if elem not in symbols:
            return None
        if elem == '(':
            stack.append(elem)
        elif elem.isdigit():
            buffer += elem
        elif elem == ' ' and buffer:
            stack.append(Node(int(buffer)))
            buffer = ''
        elif elem == ')':
            if buffer:
                stack.append(Node(int(buffer)))
                buffer = ''
            children = []
            while stack and stack[-1] != '(':
                children.append(stack.pop())
            stack.pop()
            if stack:
                if len(children) == 1:
                    node = children[0]
                    if not stack[-1].left:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
                else:
                    return None
            else:
                root = children[0]
    if stack:
        return None
    return BinaryTree(root)


if __name__ == "__main__":
    with open('Tree.txt') as file:
        data = file.read()
    tree = parse(data)
    data = binary_to_AVL(tree.root)
    avl = AVLTree()
    for elem in data:
        avl.insert(elem)
    avl.show()
    for i in range(10):
        avl.insert(random.randint(-1000, 100))
    avl.show()
    avl.show()
