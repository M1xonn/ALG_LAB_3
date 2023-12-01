class Node:
    def __init__(self, data, left: 'Node' = None, right: 'Node' = None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 1

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, root: Node = None):
        self.root = root

    def _dfs_in(self, root):
        if root:
            self._dfs_in(root.left)
            if self.root == root:
                print(root, 'root')
            else:
                print(root)
            self._dfs_in(root.right)

    def _dfs_pr(self, root):
        if root:
            if self.root == root:
                print(root, 'root')
            else:
                print(root)
            self._dfs_pr(root.left)
            self._dfs_pr(root.right)

    def _dfs_po(self, root):
        if root:
            self._dfs_po(root.left)
            self._dfs_po(root.right)
            if self.root == root:
                print(root, 'root')
            else:
                print(root)

    def _bfs(self):
        queue = [self.root]
        while len(queue) != 0:
            cur_node = queue.pop(0)

            if cur_node is not None:
                if self.root == cur_node:
                    print(cur_node.data, 'root')
                else:
                    print(cur_node.data)
            else:
                print("null")
                continue

            if cur_node.left:
                queue.append(cur_node.left)

            if cur_node.right:
                queue.append(cur_node.right)

    def _iterative_in(self):
        stack = [self.root]
        while stack[0]:
            curr = stack[-1]
            if curr is not None:
                stack.append(curr.left)
                continue
            else:
                stack.pop()
                node = stack.pop()
                stack.append(node.right)
                if node == self.root:
                    print(node, "root")
                else:
                    print(node)

    def _iterative_pr(self):
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node == self.root:
                print(node, "root")
            else:
                print(node)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

    def _iterative_po(self):
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node.left is not None:
                stack.append(node.left)
            if node == self.root:
                print(node, "root")
            else:
                print(node)
            if node.right is not None:
                stack.append(node.right)




    def show(self):
        self._iterative_in()
        print('-------------------------------')
        self._iterative_pr()
        print('-------------------------------')
        self._iterative_po()
        print('-------------------------------')
        print("Обход дерева в ширину")
        self._bfs()
