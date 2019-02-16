######
# TREENODE CLASS
######


class TreeNodeStory:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    def add_child(self, node):
        self.choices.append(node)

    def traverse(self):
        story_node = self
        print(story_node.story_piece)
        while len(story_node.choices) > 0:
            choice = input("Enter 1 or 2 to continue the story: ")
            if choice not in ["1", "2"]:
                print("Invalid input, try again")
            else:
                chosen_index = int(choice)
                chosen_index -= 1
                chosen_child = story_node.choices[chosen_index]
                print(chosen_child.story_piece)
                story_node = chosen_child


######
# VARIABLES FOR TREE
######

user_choice = input("What is your name? ")
# print(user_choice)

story_root = TreeNodeStory(user_choice + """ is in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")
choice_a = TreeNodeStory("""
The bear is startled by """ + user_choice + """'s voice 
and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")
choice_b = TreeNodeStory(user_choice + """ comes across 
a clearing full of flowers. 
The bear follows and asks, 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")
choice_a_1 = TreeNodeStory("""
The bear returns and tells """ + user_choice + """, 'It's been a rough week.' 
After making peace with a talking bear, he shows them the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")
choice_a_2 = TreeNodeStory("""
The bear returns and tells """ + user_choice + """, 
'Bullying is not okay! I'm off to tell the Mayor of Bearsville.' 
meanwhile leaving our adventurer alone
in the wilderness.

YOU REMAIN LOST...
""")
choice_b_1 = TreeNodeStory("""
The bear is unamused. After smelling the flowers, it turns around and leaves """ + user_choice + """ alone.

YOU REMAIN LOST....
""")
choice_b_2 = TreeNodeStory("""
The bear understands and apologizes for the rough introduction. """ + user_choice + """'s new friend 
leads them to a path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")
story_root.add_child(choice_a)
story_root.add_child(choice_b)
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)
######
# TESTING AREA
######
print("Our story begins...")
story_root.traverse()

