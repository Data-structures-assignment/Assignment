class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current, data):
        if data < current.data:
            if current.left:
                self._insert_recursive(current.left, data)
            else:
                current.left = Node(data)
        elif data > current.data:
            if current.right:
                self._insert_recursive(current.right, data)
            else:
                current.right = Node(data)

    def display(self):
        if not self.root:
            return "Empty tree"
        
        lines = []
        level = [self.root]
        count = 0
        max_width = 80
        
        while level and count < 10:
            count += 1
            next_level = []
            line1 = []
            line2 = []
            
            for node in level:
                if node:
                    line1.extend([' ' * 3 + f'({node.data})' + ' ' * 3])
                    if node.left and node.right:
                        line2.extend(['  /' + ' ' * 5 + '\\  '])
                    elif node.left:
                        line2.extend(['  /' + ' ' * 7])
                    elif node.right:
                        line2.extend([' ' * 7 + '\\  '])
                    else:
                        line2.extend([' ' * 9])
                    next_level.extend([node.left if node else None, 
                                    node.right if node else None])
                else:
                    line1.extend([' ' * 9])
                    line2.extend([' ' * 9])
                    next_level.extend([None, None])
            
            if len(''.join(line1)) > max_width:
                break
                
            lines.append(''.join(line1))
            if any(next_level):
                lines.append(''.join(line2))
            
            level = next_level
        
        return '\n'.join(lines)

def main():
    tree = BinarySearchTree()
    print("Welcome to Binary Search Tree Visualizer!")
    print("This program will show you a tree with circular nodes connected by lines.")
    
    while True:
        print("\nBinary Search Tree Operations:")
        print("1. Insert value")
        print("2. Insert multiple values")
        print("3. Display tree")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            try:
                value = int(input("Enter a value to insert: "))
                tree.insert(value)
                print("\nTree after insertion:")
                print(tree.display())
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == '2':
            try:
                values = input("Enter multiple values separated by spaces: ")
                for value in values.split():
                    tree.insert(int(value))
                print("\nTree after inserting all values:")
                print(tree.display())
            except ValueError:
                print("Please enter valid numbers!")
                
        elif choice == '3':
            if tree.root is None:
                print("\nThe tree is empty!")
            else:
                print("\nCurrent tree structure:")
                print(tree.display())
                
        elif choice == '4':
            print("Thank you for using the Binary Search Tree Visualizer!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
