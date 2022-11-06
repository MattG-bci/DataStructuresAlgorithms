class BSTNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

    def add(self, node):
        if node.val == self.val: # BST cannot hold duplicates.
            return

        if node.val < self.val:
            if self.left:
                self.left.add(node)
            else:
                self.left = node

        elif node.val > self.val:
            if self.right:
                self.right.add(node)
            else:
                self.right = node

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.val)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.val == val:
            return True

        if val < self.val:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.val:
            if self.right:
                return self.right.search(val)
            else:
                return False

def build_tree():
    root = BSTNode(15)
    root.add(BSTNode(14))
    root.add(BSTNode(17))
    root.add(BSTNode(13))

    return root

if __name__ == "__main__":
    root = build_tree()
    #print(root.in_order_traversal())
    #print(root.left)
    print(root.search(19))