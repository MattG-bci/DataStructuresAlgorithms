from logging.config import valid_ident


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

    # Exercise functions

    def find_min(self):
        #elements = self.in_order_traversal()
        #return elements[0]
        if self.left is None:
            return self.val
        return self.left.find_min()

    def find_max(self):
        #elements = self.in_order_traversal()
        #return elements[-1]
        if self.right is None:
            return self.val
        return self.right.find_max()

    def calculate_sum(self):
        elements = self.in_order_traversal()
        return sum(elements)

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.val)
        return elements

    def pre_order_traversal(self):
        elements = []

        elements.append(self.val)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements


    def delete(self, val):
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.val:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            max_val = self.left.find_max()
            self.val = max_val
            self.left = self.left.delete(max_val)

        return self

       
def build_tree():
    root = BSTNode(15)
    root.add(BSTNode(14))
    root.add(BSTNode(17))
    root.add(BSTNode(13))

    return root

if __name__ == "__main__":
    root = build_tree()
    #print(root.search(19))
    #print(root.find_min())
    #print(root.find_max())
    #print(root.calculate_sum())
    #print(root.post_order_traversal())
    #print(root.pre_order_traversal())
    root.delete(17)
    print(root.in_order_traversal())