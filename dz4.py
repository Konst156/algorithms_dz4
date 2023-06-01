class RedBlackTreeNode:
    def __init__(self, val):
        self.val = val
        self.color = "RED"
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.root = None

    def left_rotate(self, node):  # Реализация левого поворота
        right_child = node.right
        node.right = right_child.left
        if right_child.left:
            right_child.left.parent = node
        right_child.parent = node.parent
        if not node.parent:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def right_rotate(self, node):  # Реализация правого поворота
        left_child = node.left
        node.left = left_child.right
        if left_child.right:
            left_child.right.parent = node
        left_child.parent = node.parent
        if not node.parent:
            self.root = left_child
        elif node == node.parent.left:
            node.parent.left = left_child
        else:
            node.parent.right = left_child
        left_child.right = node
        node.parent = left_child

    def insert(self, val):  # Реализация вставки с балансировкой
        new_node = RedBlackTreeNode(val)
        self._insert_node(new_node)

    def _insert_node(self, new_node): # Реализация вставки нового узла
        current_node = self.root
        parent_node = None
        while current_node:
            parent_node = current_node
            if new_node.val < current_node.val:
                current_node = current_node.left
            else:
                current_node = current_node.right

        new_node.parent = parent_node

        if not parent_node:
            self.root = new_node
        elif new_node.val < parent_node.val:
            parent_node.left = new_node
        else:
            parent_node.right = new_node

        self._balance_insert(new_node)

    def _balance_insert(self, node):  # Реализация балансировки при вставке
        while node.parent and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle_node = node.parent.parent.right

                if uncle_node and uncle_node.color == "RED":
                    node.parent.color = "BLACK"
                    uncle_node.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.right_rotate(node.parent.parent)
            else:
                uncle_node = node.parent.parent.left

                if uncle_node and uncle_node.color == "RED":
                    node.parent.color = "BLACK"
                    uncle_node.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.left_rotate(node.parent.parent)

        self.root.color = "BLACK"        



    def inorder_traversal(self, node):  # Выводecho "# algorithms_dz4" >> README.md элементов дерева в порядке возрастания
        if node:
            self.inorder_traversal(node.left)
            print(node.val, end=' ')
            self.inorder_traversal(node.right)

# Пример использования
tree = RedBlackTree()

elements = [7, 3, 18, 10, 22, 8, 11, 26, 2, 6, 13]
for element in elements:
    tree.insert(element)

tree.inorder_traversal(tree.root)
