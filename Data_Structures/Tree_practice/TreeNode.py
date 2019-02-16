class TreeNode:
    def __init__(self, value):
        # print('Instantiating node ' + '\"' + value + '\"')
        self.value = value
        self.children = []

    def add_child(self, child_node):
        print("Adding {0}".format(child_node.value))
        self.children.append(child_node)

    def remove_child(self, child_node):
        print("Removing {0} from {1}".format(child_node.value, self.value))
        """new_children = []
        for i in self.children:
            if i != child_node:
                ew_children.append(i)
            self.children = new_children"""
        # comparative functionality using list comprehension(less code)
        self.children = [i for i in self.value if i != child_node]

    def traverse(self):
        print("Traversing...")
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit = current_node.children


root1 = TreeNode("CEO")
first_child = TreeNode("Vice-President")
second_child = TreeNode("Head of Marketing")
third_child = TreeNode("Marketing Assistant")

root1.add_child(first_child)
root1.add_child(second_child)
second_child.add_child(third_child)
root1.traverse()
root1.remove_child(second_child)

root = TreeNode("I am Root")
child = TreeNode("a wee sappling")
bad_seed = TreeNode("Root Rot!")


root.add_child(child)
root.add_child(bad_seed)
root.remove_child(bad_seed)
"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self, level=0):
        # HELPER METHOD TO PRINT TREE!
        ret = "--->" * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret

    def add_child(self, child_node):
        self.children.append(child_node)
"""
