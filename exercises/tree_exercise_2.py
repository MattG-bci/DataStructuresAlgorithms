from hashlib import new


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

def build_tree():
    root = Node("Global")

    india = Node("India")

    gujarat = Node("Gujarat")
    gujarat.add_child(Node("Ahmedabad"))
    gujarat.add_child(Node("Baroda"))
    
    karnataka = Node("Karnataka")
    karnataka.add_child(Node("Bangluru"))
    karnataka.add_child(Node("Mysore"))

    usa = Node("USA")

    new_jersey = Node("New Jersey")
    new_jersey.add_child(Node("Princeton"))
    new_jersey.add_child(Node("Trenton"))

    california = Node("California")
    california.add_child(Node("San Francisco"))
    california.add_child(Node("Mountain View"))
    california.add_child(Node("Palo Alto"))

    usa.add_child(new_jersey)
    usa.add_child(california)

    india.add_child(gujarat)
    india.add_child(karnataka)

    root.add_child(india)
    root.add_child(usa)

    return root

if __name__ == "__main__":
    root = build_tree()
    root.print_tree(3)

