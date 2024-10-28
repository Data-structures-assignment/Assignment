  from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = str(value)  # Convert value to string
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        value = str(value)  # Convert value to string
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def delete(self, value):
        value = str(value)  # Convert value to string
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if not node:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp_val = self._min_value_node(node.right)
            node.value = temp_val.value
            node.right = self._delete_recursive(node.right, temp_val.value)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    def bfs(self):
        result = []
        if not self.root:
            return result
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result


# User Interaction
bst = BinarySearchTree()

while True:
    action = input("Enter 'insert' to add a value, 'delete' to remove a value, or 'exit' to stop: ").strip().lower()
    
    if action == "insert":
        value = input("Enter a value to insert: ")
        bst.insert(value)
        print("Inserted successfully.")
    elif action == "delete":
        value = input("Enter a value to delete: ")
        bst.delete(value)
        print("Deleted successfully.")
    elif action == "exit":
        print("Exiting...")
        break
    else:
        print("Invalid action. Please enter 'insert', 'delete', or 'exit'.")

    # Display current tree structure
    print("\nCurrent tree traversals:")
    print("Inorder:", bst.inorder())
    print("Preorder:", bst.preorder())
    print("Postorder:", bst.postorder())
    print("BFS:", bst.bfs())
    print("-" * 40)
