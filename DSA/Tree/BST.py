# -----------------------------
# Node Class
# -----------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# -----------------------------
# Binary Search Tree Class
# -----------------------------
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert Node
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert(current.left, data)

        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert(current.right, data)

        else:
            print("Duplicate values are not allowed.")

    # Search
    def search(self, data):
        return self._search(self.root, data)

    def _search(self, current, data):
        if current is None:
            return False

        if current.data == data:
            return True

        elif data < current.data:
            return self._search(current.left, data)

        else:
            return self._search(current.right, data)

    # Find Minimum
    def find_min(self):
        current = self.root

        if current is None:
            return None

        while current.left:
            current = current.left

        return current.data

    # Find Maximum
    def find_max(self):
        current = self.root

        if current is None:
            return None

        while current.right:
            current = current.right

        return current.data

    # Inorder Traversal
    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, current):
        if current:
            self._inorder(current.left)
            print(current.data, end=" ")
            self._inorder(current.right)

    # Preorder Traversal
    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, current):
        if current:
            print(current.data, end=" ")
            self._preorder(current.left)
            self._preorder(current.right)

    # Postorder Traversal
    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self, current):
        if current:
            self._postorder(current.left)
            self._postorder(current.right)
            print(current.data, end=" ")

    # Level Order Traversal
    def level_order(self):
        if self.root is None:
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)
            print(current.data, end=" ")

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        print()

    # Height of Tree
    def height(self):
        return self._height(self.root)

    def _height(self, current):
        if current is None:
            return -1

        left = self._height(current.left)
        right = self._height(current.right)

        return max(left, right) + 1

    # Count Nodes
    def count_nodes(self):
        return self._count_nodes(self.root)

    def _count_nodes(self, current):
        if current is None:
            return 0

        return (
            1
            + self._count_nodes(current.left)
            + self._count_nodes(current.right)
        )

    # Delete Node
    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, current, data):
        if current is None:
            return current

        if data < current.data:
            current.left = self._delete(current.left, data)

        elif data > current.data:
            current.right = self._delete(current.right, data)

        else:
            # Case 1: No Child
            if current.left is None and current.right is None:
                return None

            # Case 2: One Child
            if current.left is None:
                return current.right

            if current.right is None:
                return current.left

            # Case 3: Two Children
            successor = self._find_min_node(current.right)
            current.data = successor.data
            current.right = self._delete(current.right, successor.data)

        return current

    def _find_min_node(self, node):
        while node.left:
            node = node.left
        return node


# -----------------------------
# Driver Program
# -----------------------------
tree = BinarySearchTree()

while True:
    print("\n====== Binary Search Tree ======")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Inorder")
    print("5. Preorder")
    print("6. Postorder")
    print("7. Level Order")
    print("8. Find Minimum")
    print("9. Find Maximum")
    print("10. Height")
    print("11. Count Nodes")
    print("12. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        tree.insert(value)

    elif choice == 2:
        value = int(input("Enter value to search: "))
        if tree.search(value):
            print("Element Found")
        else:
            print("Element Not Found")

    elif choice == 3:
        value = int(input("Enter value to delete: "))
        tree.delete(value)
        print("Deleted Successfully")

    elif choice == 4:
        print("Inorder Traversal:")
        tree.inorder()

    elif choice == 5:
        print("Preorder Traversal:")
        tree.preorder()

    elif choice == 6:
        print("Postorder Traversal:")
        tree.postorder()

    elif choice == 7:
        print("Level Order Traversal:")
        tree.level_order()

    elif choice == 8:
        print("Minimum:", tree.find_min())

    elif choice == 9:
        print("Maximum:", tree.find_max())

    elif choice == 10:
        print("Height:", tree.height())

    elif choice == 11:
        print("Total Nodes:", tree.count_nodes())

    elif choice == 12:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")