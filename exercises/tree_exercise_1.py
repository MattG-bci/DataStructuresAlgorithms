class Node:
    def __init__(self, name, designation) -> None:
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, character):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if character == "name":
            print(prefix + self.name)
            self.traverse_children(character)

        elif character == "designation":
            print(prefix + self.designation)
            self.traverse_children(character)

        elif character == "both":
            print(f"{prefix} {self.name} ({self.designation})")
            self.traverse_children(character)

        else:
            raise BaseException("Wrong character entered.")

    def traverse_children(self, character):
        if self.children:
            for child in self.children:
                child.print_tree(character)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

def build_tree():
    root = Node("Nilupul", "CEO")

    cto = Node("Chinmay", "CTO")

    infra_head = Node("Vishwa", "Infrastructure Head")
    infra_head.add_child(Node("Dhaval", "Cloud Manager"))
    infra_head.add_child(Node("Abhijit", "App Manager"))

    app_head = Node("Aamir", "Application Head")

    hr_head = Node("Gels", "HR Head")
    hr_head.add_child(Node("Peter", "Recruitment Manager"))
    hr_head.add_child(Node("Waqas", "Policy Manager"))

    cto.add_child(infra_head)
    cto.add_child(app_head)

    root.add_child(cto)
    root.add_child(hr_head)

    return root

if __name__ == "__main__":
    root = build_tree()
    root.print_tree("both")

